def linear_search(arr, target):
#Search for a target value in an array using linear search.
    # Loop through the array

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
if __name__ == "__main__":
    database = ["item1", "item2", "item3", "item4", "item5"]
    target_item = "item3"
    index = linear_search(database, target_item)
    
    if index != -1:
        print(f"Item '{target_item}' found at index {index}.")
    else:
        print(f"Item '{target_item}' not found in the database.")

