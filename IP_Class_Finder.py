import socket
import re

def get_ip_from_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return None

def validate_ip(ip):
    pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    if re.match(pattern, ip):
        parts = ip.split(".")
        return all(0 <= int(part) <= 255 for part in parts)
    return False

def get_ip_class(ip):
    try:
        first_octet = int(ip.split(".")[0])

        if first_octet == 127:
            return "Loopback"
        elif 1 <= first_octet <= 126:
            return "Class A"
        elif 128 <= first_octet <= 191:
            return "Class B"
        elif 192 <= first_octet <= 223:
            return "Class C"
        elif 224 <= first_octet <= 239:
            return "Class D (Multicast)"
        elif 240 <= first_octet <= 255:
            return "Class E (Experimental)"
        else:
            return "Invalid / Reserved"

    except:
        return "Invalid IP"

def get_ip_type(ip):
    try:
        first, second, *_ = map(int, ip.split("."))

        if first == 127:
            return "Loopback"
        elif (
            first == 10 or
            (first == 172 and 16 <= second <= 31) or
            (first == 192 and second == 168)
        ):
            return "Private"
        else:
            return "Public"

    except:
        return "Unknown"

def process_input(user_input):
    # If valid IP → use directly
    if validate_ip(user_input):
        return user_input

    # Else try domain → IP
    ip = get_ip_from_domain(user_input)
    return ip

def main():
    print("🌐 IP Classifier Tool \n")

    while True:
        try:
            user_input = input("Enter IP address or domain: ").strip()

            if not user_input:
                print("Empty input. Try again.\n")
                continue

            ip = process_input(user_input)

            if not ip:
                print("Invalid IP or domain.\n")
            else:
                ip_class = get_ip_class(ip)
                ip_type = get_ip_type(ip)

                print("\n🔍 Result:")
                print(f"IP Address : {ip}")
                print(f"IP Class   : {ip_class}")
                print(f"IP Type    : {ip_type}\n")

        except Exception as e:
            print(f"⚠️ Unexpected error: {e}\n")

        # Continue / Exit
        while True:
            choice = input("Do you want to continue? (y/n): ").lower()
            if choice == 'y':
                print()
                break
            elif choice == 'n':
                print("Exiting...")
                return
            else:
                print("⚠️ Enter 'y' or 'n' only.")

if __name__ == "__main__":
    main()