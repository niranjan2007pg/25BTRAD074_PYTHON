# Lab Exercise 13: CSV-Based Payroll Management System
# Student: Niranjan P G | USN: 25BTRAD074
import csv

def generate_csv(file):
    rows = [
        ["EmpID", "Name", "Dept", "Basic", "Allowance"],
        ["EMP101", "Niranjan P G", "Data Engg", 75000, 15000],
        ["EMP102", "Deepak Rao", "AI Research", 68000, 12000],
        ["EMP103", "Ananya Sen", "IT Ops", 55000, 10000]
    ]
    with open(file, "w", newline="") as f:
        csv.writer(f).writerows(rows)

def process_payroll(file):
    print(f"{'EmpID':<8} {'Name':<14} {'Gross':<12} {'Deductions':<12} {'Net Salary':<10}")
    print("-" * 58)
    with open(file, "r") as f:
        for r in csv.DictReader(f):
            gross = float(r["Basic"]) + float(r["Allowance"])
            ded = 0.12 * float(r["Basic"]) + 0.10 * gross
            print(f"{r['EmpID']:<8} {r['Name']:<14} Rs.{gross:<9.2f} Rs.{ded:<9.2f} Rs.{gross - ded:<9.2f}")

if __name__ == "__main__":
    print("=== CSV Payroll Management System ===")
    generate_csv("payroll.csv")
    process_payroll("payroll.csv")
