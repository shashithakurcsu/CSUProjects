import numpy as np
import pandas as pd
import time
import yfinance as yf
import matplotlib.pyplot as plt


# Basic DTW Implementation
def dtw(x, y):
    distances = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):  # Corrected typo: removed extra closing parenthesis
            distances[i, j] = abs(x[i] - y[j])

    cost = np.zeros((len(x), len(y)))
    cost[0, 0] = distances[0, 0]

    for i in range(1, len(x)):
        cost[i, 0] = cost[i - 1, 0] + distances[i, 0]

    for j in range(1, len(y)):
        cost[0, j] = cost[0, j - 1] + distances[0, j]

    for i in range(1, len(x)):
        for j in range(1, len(y)):
            cost[i, j] = distances[i, j] + min(cost[i - 1, j], cost[i, j - 1], cost[i - 1, j - 1])

    path = []
    i, j = len(x) - 1, len(y) - 1
    while i > 0 and j > 0:
        path.append((i, j))
        i, j = min((i - 1, j), (i, j - 1), (i - 1, j - 1), key=lambda k: cost[k])
    path.append((0, 0))
    path.reverse()

    return cost[-1, -1], path


# Optimized DTW Implementation with Pruning
def dtw_with_pruning(x, y, window):
    distances = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(max(0, i - window), min(len(y), i + window)):
            distances[i, j] = abs(x[i] - y[j])

    cost = np.full((len(x), len(y)), np.inf)
    cost[0, 0] = distances[0, 0]

    for i in range(1, len(x)):
        for j in range(max(1, i - window), min(len(y), i + window)):
            cost[i, j] = distances[i, j] + min(cost[i - 1, j], cost[i, j - 1], cost[i - 1, j - 1])

    path = []
    i, j = len(x) - 1, len(y) - 1
    while i > 0 and j > 0:
        path.append((i, j))
        i, j = min((i - 1, j), (i, j - 1), (i - 1, j - 1), key=lambda k: cost[k])
    path.append((0, 0))
    path.reverse()

    return cost[-1, -1], path


# Function to fetch financial data
def fetch_financial_data(ticker, period='1mo'):
    data = yf.download(ticker, period=period)
    return data['Close'].values


# Function to generate synthetic data
def generate_synthetic_data(length):
    t = np.linspace(0, 2 * np.pi, length)
    series = np.sin(t) + np.random.normal(0, 0.1, length)
    return series


# Function to measure execution time
def measure_execution_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


# Test and collect empirical data
def collect_data():
    lengths = [100, 200, 300, 400, 500]
    window = 50
    results = {
        "Length": [],
        "Basic DTW Time": [],
        "Optimized DTW Time": []
    }

    for length in lengths:
        series_a = generate_synthetic_data(length)
        series_b = generate_synthetic_data(length)

        # Print synthetic data
        print(f"Synthetic Series A (Length {length}): {series_a[:10]} ...")
        print(f"Synthetic Series B (Length {length}): {series_b[:10]} ...")

        basic_time = measure_execution_time(dtw, series_a, series_b)
        optimized_time = measure_execution_time(dtw_with_pruning, series_a, series_b, window)

        results["Length"].append(length)
        results["Basic DTW Time"].append(basic_time)
        results["Optimized DTW Time"].append(optimized_time)

    return results


# Run the data collection and print results
if __name__ == "__main__":
    # Fetch financial data for additional testing
    financial_series_a = fetch_financial_data('AAPL', '1mo')
    financial_series_b = fetch_financial_data('MSFT', '1mo')

    # Perform empirical data analysis with synthetic data
    empirical_data = collect_data()

    # Print synthetic data results
    print("Synthetic Data Results:")
    for i in range(len(empirical_data["Length"])):
        print(f"Length: {empirical_data['Length'][i]}")
        print(f"Basic DTW Time: {empirical_data['Basic DTW Time'][i]:.6f} seconds")
        print(f"Optimized DTW Time: {empirical_data['Optimized DTW Time'][i]:.6f} seconds")
        print()

    # Example of using financial data with DTW
    basic_financial_time = measure_execution_time(dtw, financial_series_a, financial_series_b)
    optimized_financial_time = measure_execution_time(dtw_with_pruning, financial_series_a, financial_series_b, 50)
    print(f"Financial Data Basic DTW Time: {basic_financial_time:.6f} seconds")
    print(f"Financial Data Optimized DTW Time: {optimized_financial_time:.6f} seconds")

    # Create a DataFrame to display results
    df_synthetic = pd.DataFrame({
        "Length": empirical_data["Length"],
        "Basic DTW Time (s)": empirical_data["Basic DTW Time"],
        "Optimized DTW Time (s)": empirical_data["Optimized DTW Time"]
    })

    df_financial = pd.DataFrame({
        "Series": ["AAPL", "MSFT"],
        "Length": [len(financial_series_a), len(financial_series_b)],
        "Basic DTW Time (s)": [basic_financial_time, basic_financial_time],
        "Optimized DTW Time (s)": [optimized_financial_time, optimized_financial_time]
    })

    # Display the data tables
    print("\nSynthetic Data Execution Times:")
    print(df_synthetic)

    print("\nFinancial Data Execution Times:")
    print(df_financial)

    # Plot the execution times for better visualization
    plt.figure(figsize=(10, 5))
    plt.plot(df_synthetic["Length"], df_synthetic["Basic DTW Time (s)"], marker='o', label='Basic DTW')
    plt.plot(df_synthetic["Length"], df_synthetic["Optimized DTW Time (s)"], marker='x', label='Optimized DTW')
    plt.title("Execution Time vs. Time Series Length (Synthetic Data)")
    plt.xlabel("Time Series Length")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()
