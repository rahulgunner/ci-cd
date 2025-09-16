import csv
from datetime import datetime
import os
import sys

LOG_FILE = "merge_logs.csv"

def append_log(date, status, commit, author):
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "status", "commit", "author"])
        writer.writerow([date, status, commit, author])

if __name__ == "__main__":
    # Get environment variables from GitHub Actions
    commit = os.getenv("GITHUB_SHA", "unknown")
    author = os.getenv("GITHUB_ACTOR", "unknown")
    status = "merged"

    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    append_log(now, status, commit, author)
    print(f"Logged merge at {now} by {author} with commit {commit}")
