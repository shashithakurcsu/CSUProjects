# Step 1: Dictionary for course room numbers
course_room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}

# Step 2: Dictionary for course instructors
course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

# Step 3: Dictionary for course meeting times
course_meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
}

# Step 4: Prompt the user to enter a course number
course_number = (input("Enter a course number (e.g., CSC101): ")).upper()

# Step 5: Check if the course number exists and display information
if course_number in course_room_numbers:
    print(f"Room number: {course_room_numbers[course_number]}")
    print(f"Instructor: {course_instructors[course_number]}")
    print(f"Meeting Time: {course_meeting_times[course_number]}")
else:
    # Step 6: Course number not found
    print("Course number not found.")
