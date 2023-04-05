import re
import platform

palindromText = "зараз корок хата кіт шалаш"
ip1 = "192.168.0.1"
ip2 = "256.0.0.1"

def validate_ip(ip_address):
    pattern = re.compile("^(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$")
    if pattern.match(ip_address):
        return True
    else:
        return False

def palindrom(text):
    words = [word.strip('.,?!') for word in text.split()]
    palindromes = [word for word in words if word.lower() == word[::-1].lower()]
    return palindromes

def get_os():
    os_name = platform.system()
    if os_name == "Darwin":
        return "Mac"
    elif os_name == "Windows":
        return "Windows"
    elif os_name == "Linux":
        return "Linux"
    else:
        return "Unknown"

print("Test:")
print(palindrom(palindromText))
print(validate_ip(ip1), "|", validate_ip(ip2))
print(get_os())