# 🔐 XDR Detection & Response Lab using Wazuh

## 🚀 Key Highlights
- Built XDR lab using Wazuh & Sysmon
- Developed custom detection rules
- Mapped detections to MITRE ATT&CK
- Simulated SOAR using Python automation

## 📌 Project Overview

This project demonstrates the design and implementation of an **XDR (Extended Detection and Response) lab** using **Wazuh** and **Sysmon** to monitor endpoint activity, detect threats, and simulate incident response workflows.

The lab replicates a real-world SOC environment by integrating endpoint telemetry, detection rules, MITRE ATT&CK mapping, and basic SOAR concepts.

---

## 🏗️ Lab Architecture

* **Ubuntu Server** → Wazuh Manager, Indexer, Dashboard
* **Windows 10** → Endpoint (monitored system with Sysmon)
* **Kali Linux** → Attacker machine

---

## 🧰 Tools & Technologies Used

* Wazuh (SIEM / XDR)
* Sysmon (Endpoint telemetry)
* Kali Linux (Attack simulation)
* Windows 10 (Target system)
* PowerShell (Attack simulation)
* MITRE ATT&CK Framework

---

## 🔍 Key Features

### ✅ Endpoint Monitoring

* Integrated Sysmon with Wazuh to capture:

  * Process creation
  * Command-line activity
  * System behavior

---

### ✅ Detection Engineering

Developed custom detection rules in Wazuh:

* **Rule 100002** → PowerShell execution
* **Rule 100004** → PowerShell using `secedit`
* **Rule 100005** → PowerShell download activity (`Invoke-WebRequest`)
* **Rule 100006** → PowerShell spawning CMD

---

### ✅ MITRE ATT&CK Mapping

| Technique             | ID        |
| --------------------- | --------- |
| PowerShell Execution  | T1059.001 |
| Ingress Tool Transfer | T1105     |

---

### ✅ Attack Simulation

Simulated real-world attacker behavior using PowerShell:

* Command execution
* Process spawning
* Web requests (simulated payload download)

---

### ✅ Threat Detection

Detected suspicious activities using:

* Sysmon logs
* Wazuh correlation rules
* Custom detection logic

---

### ✅ SOAR (Simulation)

Implemented **basic SOAR concept** using automated workflows:

**Trigger:**

* Detection rule fired (e.g., PowerShell download)

**Automated Actions:**

* Alert generated in Wazuh
* Endpoint flagged as suspicious
* Incident recorded
* Simulated containment (block IP / isolate system)

---

## 📊 Attack Timeline

1. PowerShell execution detected (T1059.001)
2. Suspicious process spawned (cmd.exe)
3. External download attempt detected (T1105)

---

## 🛡️ Incident Response Workflow

### 🔎 Detection

* Suspicious PowerShell activity identified via custom rules

### ⚠️ Analysis

* Command-line inspection
* Process behavior analysis

### 🛑 Containment

* Flag endpoint
* Simulated blocking of malicious activity

### 🔁 Recovery

* System inspection
* Remove suspicious artifacts
* Restore normal operations

---

## 📸 Screenshots

Include:

* Wazuh agent active
* Sysmon logs
* Custom detection alerts
* PowerShell activity detection
* SOAR workflow evidence

---

## 📁 Project Structure

```
EDR-XDR-Lab/
 ├── configs/
 ├── reports/
 ├── screenshots/
 ├── scripts/
 └── README.md
```

---

## 🚀 Key Learnings

* Built an end-to-end XDR lab environment
* Developed custom detection rules using real telemetry
* Mapped detections to MITRE ATT&CK techniques
* Simulated attacker behavior using PowerShell
* Implemented basic SOAR concepts for automated response

---

## 🎯 Future Improvements

* Integrate full SOAR platform (e.g., Shuffle or Cortex XSOAR)
* Add cloud log monitoring (AWS / Azure)
* Implement advanced threat hunting queries
* Develop automated response scripts

---

## 👨‍💻 Author

Syed Yousuf Uddin

---

## 📌 Summary

This project demonstrates practical skills in:

* SIEM/XDR implementation
* Detection engineering
* Threat analysis
* Incident response
* Security automation concepts

---

⭐ This lab reflects real-world SOC workflows and aligns with industry requirements for cybersecurity roles.
