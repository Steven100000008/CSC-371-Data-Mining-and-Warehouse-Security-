import pandas as pd

# CSC 371 - Assignment 3
# Fictional Student Dataset

data = {
    "Student ID": ["CSC/001", "CSC/002", "CSC/003", "CSC/004", "CSC/005",
                   "CSC/006", "CSC/007", "CSC/008", "CSC/009", "CSC/010"],
    "Department": ["Computer Science"] * 10,
    "Level": [200, 200, 300, 200, 300, 200, 300, 200, 300, 200],
    "Attendance Percentage": [95, 88, 76, 92, 65, 98, 80, 70, 85, 90],
    "Average Examination Score": [78.5, 72.0, 65.5, 81.0, 55.0, 88.5, 68.0, 60.5, 74.0, 82.5]
}

df = pd.DataFrame(data)
print(df)
print("\nTotal Students:", len(df))
print("Average Attendance:", df["Attendance Percentage"].mean())
print("Average Exam Score:", df["Average Examination Score"].mean())
