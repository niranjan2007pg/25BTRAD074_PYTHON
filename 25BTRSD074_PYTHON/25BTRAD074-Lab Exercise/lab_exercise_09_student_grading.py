# Lab Exercise 9: Student Grading System
# Student: Niranjan P G | USN: 25BTRAD074

def get_grade(pct):
    if pct >= 90: return "A+"
    elif pct >= 80: return "A"
    elif pct >= 70: return "B"
    elif pct >= 60: return "C"
    else: return "F"

students = {
    "Niranjan P G": [95, 92, 88],
    "Aarav Sharma": [82, 78, 85],
    "Priya Patel": [74, 68, 72],
    "Rohan Gupta": [58, 62, 55]
}

def main():
    print("=== Student Academic Grading System ===")
    print(f"{'Student Name':<16} {'Total':<8} {'Percentage':<12} {'Grade':<6} {'Status':<8}")
    print("-" * 52)
    for name, marks in students.items():
        total = sum(marks)
        pct = (total / (len(marks) * 100)) * 100
        grade = get_grade(pct)
        status = "Pass" if grade != "F" else "Fail"
        print(f"{name:<16} {total:<8} {pct:>5.1f}%       {grade:<6} {status:<8}")

if __name__ == "__main__":
    main()
