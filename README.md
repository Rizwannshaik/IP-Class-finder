# 🌐 IP Class Finder (IP Classifier) Tool Version 1.0
A robust Python-based command-line tool that identifies the class and type of an IP address or domain name with strong input validation and error handling.

---

## 🚀 Features

* 🔍 Accepts both **IP addresses** and **domain names**
* 🌐 Automatically resolves domain → IP
* 🧠 Identifies IP Class:

  * Class A, B, C, D, E
* 🔒 Detects IP Type:

  * Public, Private, Loopback
* 🛡️ Built with **crash-proof error handling**
* 🔁 Interactive CLI (runs continuously until user exits)
* ⚠️ Handles:

  * Invalid IPs (e.g., 999.999.999.999)
  * Non-existent domains
  * Empty input

---

## 🧠 IP Classification Logic

| Class    | Range     | Description          |
| -------- | --------- | -------------------- |
| A        | 1 – 126   | Large networks       |
| B        | 128 – 191 | Medium networks      |
| C        | 192 – 223 | Small networks       |
| D        | 224 – 239 | Multicast            |
| E        | 240 – 255 | Experimental         |
| Loopback | 127.x.x.x | Local system testing |

---

## 🔐 Private IP Ranges

* 10.0.0.0 – 10.255.255.255
* 172.16.0.0 – 172.31.255.255
* 192.168.0.0 – 192.168.255.255

---

## 🛠️ Installation

```bash
git clone https://github.com/Rizwannshaik/ip-classifier-tool.git
cd ip-classifier-tool
```

---

## ▶️ Usage

```bash
python3 IP_Class_Finder.py
```

### 💡 Example

```
Enter IP address or domain: google.com

🔍 Result:
IP Address : 142.250.183.206
IP Class   : Class B
IP Type    : Public
```

---

## 🔁 Interactive Mode

After each result, the tool prompts:

```
Do you want to continue? (y/n):
```

* Press **y** to continue
* Press **n** to exit

---

## 📦 Requirements

* Python 3.x
* No external dependencies

---

## 🛡️ Error Handling

This tool is designed to be **fully crash-resistant**:

* Prevents runtime crashes from invalid input
* Handles DNS resolution failures gracefully
* Validates IP format before processing
* Catches unexpected exceptions

---

## 🎯 Project Purpose

This project demonstrates:

* Networking fundamentals (IP classification)
* Python scripting and CLI design
* Input validation and exception handling
* Domain-to-IP resolution using sockets

---

## 🚀 Future Enhancements - In Upcoming Verisons. 

* 🌍 Geo-IP location lookup 
* 📡 WHOIS information integration
* 🔎 DNS record enumeration (A, MX, TXT)
* 🚪 Port scanning module
* 🖥️ Web-based UI (Flask / FastAPI)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed as part of a cybersecurity-focused portfolio project.
