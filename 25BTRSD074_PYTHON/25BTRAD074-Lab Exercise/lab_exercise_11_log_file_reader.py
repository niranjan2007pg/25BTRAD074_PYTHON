# Lab Exercise 11: Log File Reader Program
# Student: Niranjan P G | USN: 25BTRAD074

def analyze_logs(filepath):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    try:
        with open(filepath, "r") as f:
            for line in f:
                for level in counts:
                    if f"[{level}]" in line:
                        counts[level] += 1
                        if level == "ERROR":
                            print(f" Critical: {line.strip()}")
        print("\n=== Log Summary ===")
        for lvl, cnt in counts.items():
            print(f" {lvl:<8}: {cnt} entries")
    except FileNotFoundError:
        print(f"Error: '{filepath}' not found.")

if __name__ == "__main__":
    log_data = """2026-10-29 10:00:00 [INFO] System started.
2026-10-29 10:05:00 [WARNING] High memory usage (84%).
2026-10-29 10:10:00 [ERROR] DB connection timed out.
2026-10-29 10:15:00 [INFO] Backup completed successfully."""
    with open("app.log", "w") as f:
        f.write(log_data)
    print("=== Analyzing Application Log File ===")
    analyze_logs("app.log")
