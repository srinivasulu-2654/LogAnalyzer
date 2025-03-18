import os
from datetime import datetime

# Ask user for log file name (default: sample.log)
log_file = input("Enter the log file name (default: sample.log): ") or "sample.log"

# Log categories to filter
log_levels = {
    "info": "info_logs.txt",
    "warning": "warning_logs.txt",
    "error": "error_logs.txt",
    "critical": "critical_logs.txt"
}

try:
    # Open the log file and read contents
    with open(log_file, "r", errors="ignore") as f:
        logs = f.readlines()

    # Process logs for each level and add timestamps
    for level, file_name in log_levels.items():
        with open(file_name, "w") as f:
            filtered_logs = [
                f"{datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')} {line}"
                for line in logs if level in line.lower()
            ]
            f.writelines(filtered_logs)

    # Print summary
    print("✅ Log filtering completed! Files created:")
    for level, file_name in log_levels.items():
        print(f"  - {level.upper()} logs saved in {file_name}")

except FileNotFoundError:
    print("⚠️ Log file not found. Make sure the log file path is correct.")
except PermissionError:
    print("⚠️ Permission denied. Try running with Administrator privileges.")
except Exception as e:
    print(f"❌ An error occurred: {e}")
