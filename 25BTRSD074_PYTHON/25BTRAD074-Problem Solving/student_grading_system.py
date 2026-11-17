# Mini Project Unit 2: Student Grading Automation System
# Student: Niranjan P G | USN: 25BTRAD074

def calculate_grade(score):
    """Returns letter grade and status based on score."""
    if score >= 90:
        return "A", "Pass"
    elif score >= 80:
        return "B", "Pass"
    elif score >= 70:
        return "C", "Pass"
    elif score >= 60:
        return "D", "Pass"
    else:
        return "F", "Fail"

def generate_report(students):
    print("=" * 65)
    print("       STUDENT ACADEMIC GRADING & PERFORMANCE REPORT")
    print("            Student: Niranjan P G | USN: 25BTRAD074")
    print("=" * 65)
    print(f"{'Roll No':<10} {'Name':<18} {'Average':<10} {'Grade':<8} {'Status':<8}")
    print("-" * 65)

    passed = 0
    total_class_score = 0

    for s in students:
        roll = s["roll"]
        name = s["name"]
        scores = s["scores"]
        avg = sum(scores) / len(scores)
        grade, status = calculate_grade(avg)
        if status == "Pass":
            passed += 1
        total_class_score += avg
        print(f"{roll:<10} {name:<18} {avg:<10.2f} {grade:<8} {status:<8}")

    print("-" * 65)
    total_students = len(students)
    class_avg = total_class_score / total_students if total_students > 0 else 0
    pass_pct = (passed / total_students * 100) if total_students > 0 else 0
    print(f"Total Students: {total_students} | Passed: {passed} | Pass Rate: {pass_pct:.1f}%")
    print(f"Class Average Score: {class_avg:.2f}")
    print("=" * 65)

if __name__ == "__main__":
    sample_students = [
        {"roll": "25BTRAD074", "name": "Niranjan P G", "scores": [95, 92, 88, 90]},
        {"roll": "25BTLAD002", "name": "Aarav Sharma", "scores": [82, 78, 85, 80]},
        {"roll": "25BTLAD003", "name": "Priya Patel", "scores": [74, 68, 72, 70]},
        {"roll": "25BTLAD004", "name": "Rohan Gupta", "scores": [58, 62, 55, 60]},
        {"roll": "25BTLAD005", "name": "Ananya Sen", "scores": [91, 89, 94, 92]}
    ]
    generate_report(sample_students)
