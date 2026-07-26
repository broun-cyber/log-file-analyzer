# 🔍 Security Log File Analyzer
A Python-based log analyzer for learning security monitoring and basic cybersecurity log analysis.

## 🚀 Features

- Reads and analyzes log files
- Counts total log entries
- Detects failed login attempts
- Extracts IP addresses from failed login events
- Counts failed login attempts by IP address
- Flags IP addresses with multiple failed login attempts
- Handles missing log files
- Includes a sample log file for testing

## 🛠️ Technologies Used

- Python 3
- Python File Handling
- Dictionaries
- String Processing
- Log Analysis
- Git & GitHub

## ⚙️ How It Works

1. The user provides the name of a log file.
2. The program reads all log entries from the file.
3. It identifies failed login attempts.
4. It extracts the source IP address from each failed login event.
5. It counts failed login attempts for each IP address.
6. An IP address with **2 or more failed login attempts** is flagged as suspicious.

## ▶️ How to Run

Run the program using:

    python log_analyzer.py

When prompted, enter:

    sample.log

Example output:

    Total log entries: 6
    Failed login attempts: 3

    Failed login attempts by IP:
    192.168.1.25: 2
    10.0.0.15: 1

    Suspicious IPs:
    [WARNING] 192.168.1.25 - 2 failed login attempts

    ## 🧠 What I Learned

Through this project, I practiced:

- Reading files with Python
- Processing log file entries
- Using loops and conditional statements
- Working with dictionaries
- Extracting data from strings
- Counting failed login attempts by IP address
- Basic security log analysis
- Identifying suspicious activity using simple rules
- Git commits and GitHub workflow

## 🔒 Security Note

This project is designed for educational purposes and demonstrates basic security log analysis.

The suspicious IP detection uses a simple rule based on repeated failed login attempts. A flagged IP does not automatically mean that the activity is malicious.

## 🔮 Future Improvements

- Analyze successful and failed login events separately
- Support different log formats
- Allow configurable suspicious-activity thresholds
- Add timestamps to detected events
- Export analysis results to a file
- Add severity levels for alerts
- Analyze larger log files

## 👨‍💻 Author

**Broun Verma**

Recruiter | BCA Student | Cybersecurity Learner
