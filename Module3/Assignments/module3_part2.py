# Ask the user to enter the current time and the number of hours to wait
current_time = int(input("Enter the current time (in hours, 24 hours clock): "))
wait_hours = int(input("Enter the number of hours to wait for the alarm : "))

# Calculate the time when the alarm will go off
alarm_time = (current_time + wait_hours) % 24

# Output the result
print(f"The alarm will go off at {alarm_time:02d}:00.")
