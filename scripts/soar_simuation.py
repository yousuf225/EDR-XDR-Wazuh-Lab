alert = "PowerShell Invoke-WebRequest detected"

print("=== SOAR AUTOMATION STARTED ===")

if "Invoke-WebRequest" in alert:
    print("ALERT:", alert)
    print("Action 1: Flag endpoint as suspicious")
    print("Action 2: Simulate blocking IP address")
    print("Action 3: Notify SOC team")
    print("Action 4: Log incident")

print("=== SOAR AUTOMATION COMPLETED ===")