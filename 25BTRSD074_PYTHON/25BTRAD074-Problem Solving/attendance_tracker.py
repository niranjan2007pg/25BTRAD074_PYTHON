"""
Mini Project - Unit 3: Attendance Tracker
Problem Solving Component - Python Programming Laboratory
Student Name: Niranjan P G
USN: 25BTRAD074
Branch: B.Tech CSE (AI & DE) | Sem: 3rd Sem | Class: CSE-AIDE (B)
Academic Year: 2026 - 2027
"""

def initialize_system():
    """Initializes and returns an empty class attendance dictionary."""
    return {}

def add_student(db, student_id, name):
    """Adds a student record using lists and dictionaries."""
    if student_id not in db:
        db[student_id] = {
            "name": name,
            "history": [],
            "attended": 0,
            "total": 0
        }

def record_session(db, session_name, attendance_map):
    """Records attendance ('P' or 'A') for all enrolled students in a session."""
    for s_id, status in attendance_map.items():
        if s_id in db:
            is_present = (status.upper() == 'P')
            db[s_id]["history"].append("P" if is_present else "A")
            db[s_id]["total"] += 1
            if is_present:
                db[s_id]["attended"] += 1

def update_attendance(db, student_id, session_idx, new_status):
    """Updates a previously recorded attendance status for a student."""
    if student_id in db and 0 <= session_idx < len(db[student_id]["history"]):
        old = db[student_id]["history"][session_idx]
        new_stat = new_status.upper()
        if old != new_stat:
            db[student_id]["history"][session_idx] = new_stat
            if new_stat == "P" and old == "A":
                db[student_id]["attended"] += 1
            elif new_stat == "A" and old == "P":
                db[student_id]["attended"] -= 1
            return True, old, new_stat
    return False, None, None

def calculate_percentage(attended, total):
    """Calculates attendance percentage."""
    return round((attended / total) * 100, 2) if total > 0 else 0.0

def display_report(db, threshold=75.0):
    """Displays attendance details in an organized tabular format."""
    print("=" * 76)
    print(f"{'CLASS ATTENDANCE SUMMARY & ELIGIBILITY REPORT':^76}")
    print("=" * 76)
    print(f"{'ID':<8} | {'Student Name':<20} | {'Attended':<8} | {'Total':<6} | {'Pct (%)':<8} | {'Status'}")
    print("-" * 76)

    shortage = []
    total_pct = 0
    for s_id, data in db.items():
        pct = calculate_percentage(data["attended"], data["total"])
        total_pct += pct
        status = "Eligible [OK]" if pct >= threshold else "SHORTAGE [ALERT]"
        if pct < threshold:
            shortage.append((s_id, data["name"], pct))
        print(f"{s_id:<8} | {data['name']:<20} | {data['attended']:<8} | {data['total']:<6} | {pct:<7.2f}% | {status}")

    print("-" * 76)
    avg_pct = total_pct / len(db) if db else 0.0
    print(f"Total Enrolled: {len(db):<6} | Class Average: {avg_pct:.2f}% | Mandatory Threshold: {threshold:.1f}%")
    print("=" * 76)
    return shortage

def main():
    print("=== Student Attendance Tracking System (Unit 3) ===")
    print("Student: Niranjan P G | USN: 25BTRAD074 | Branch: CSE (AI & DE)\n")

    db = initialize_system()
    students = [
        ("S101", "Aarav Sharma"),   ("S102", "Bhavna Patel"),
        ("S103", "Chirag Verma"),   ("S104", "Deepika Rao"),
        ("S105", "Eshwar Sundaram"),("S106", "Fatima Zehra")
    ]
    for sid, name in students:
        add_student(db, sid, name)
    print(f"[+] Successfully enrolled {len(students)} students in course database.")

    # Record 6 lecture sessions
    sessions = [
        ("L1", {"S101":"P","S102":"P","S103":"P","S104":"P","S105":"P","S106":"P"}),
        ("L2", {"S101":"P","S102":"A","S103":"P","S104":"P","S105":"A","S106":"P"}),
        ("L3", {"S101":"P","S102":"P","S103":"A","S104":"P","S105":"A","S106":"P"}),
        ("L4", {"S101":"P","S102":"P","S103":"A","S104":"P","S105":"P","S106":"A"}),
        ("L5", {"S101":"P","S102":"A","S103":"P","S104":"A","S105":"A","S106":"P"}),
        ("L6", {"S101":"P","S102":"P","S103":"A","S104":"P","S105":"A","S106":"A"})
    ]
    for s_name, mapping in sessions:
        record_session(db, s_name, mapping)
    print(f"[+] Recorded {len(sessions)} class sessions across Unit 3 modules.\n")

    # Initial Report
    shortage = display_report(db, threshold=75.0)
    print(f"[!] Warning: {len(shortage)} student(s) currently below 75.0% threshold.\n")

    # Update Attendance Scenario
    print("[Update Scenario] Approving On-Duty (OD) for Fatima Zehra (S106) for L4:")
    success, old_s, new_s = update_attendance(db, "S106", session_idx=3, new_status="P")
    if success:
        new_pct = calculate_percentage(db["S106"]["attended"], db["S106"]["total"])
        print(f"[✓] Status updated from '{old_s}' to '{new_s}'. New Attendance: {new_pct:.2f}% (Eligible [OK])\n")

    # Post-Update Status
    updated_shortage = [s for s, d in db.items() if calculate_percentage(d["attended"], d["total"]) < 75.0]
    print(f"[✓] Final Evaluation: Shortage list reduced to {len(updated_shortage)} student(s): {', '.join(updated_shortage)}.")

if __name__ == "__main__":
    main()
