print("=== Security Log File Analyzer ===")

log_file = input("Enter log file name: ")

try:
    with open(log_file, "r") as file:
        logs = file.readlines()

    print(f"\nTotal log entries: {len(logs)}")

    failed_logins = 0
    failed_ips = {}

    for log in logs:
        if "Failed login attempt" in log:
            failed_logins += 1

            ip_address = log.strip().split()[-1]

            if ip_address in failed_ips:
                failed_ips[ip_address] += 1
            else:
                failed_ips[ip_address] = 1

    print(f"Failed login attempts: {failed_logins}")

    print("\nFailed login attempts by IP:")

    for ip, count in failed_ips.items():
        print(f"{ip}: {count}")

    print("\nSuspicious IPs:")

    suspicious_found = False

    for ip, count in failed_ips.items():
        if count >= 2:
            print(f"[WARNING] {ip} - {count} failed login attempts")
            suspicious_found = True

    if not suspicious_found:
        print("No suspicious IPs detected.")

except FileNotFoundError:
    print("Error: Log file not found.")