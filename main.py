import requests
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "📱 Welcome to Mobile Info Finder 📱")
print(Fore.YELLOW + "-----------------------------------")


mobile = input(Fore.GREEN + "Enter 10-digit mobile number: ")


if not (mobile.isdigit() and len(mobile) == 10):
    print(Fore.RED + "❌ Invalid number! Please enter a 10-digit number.")
    exit()


url = f"https://demon.taitanx.workers.dev/?mobile={mobile}"
print(Fore.BLUE + "\n🔍 Fetching details... please wait...\n")

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        if not data.get("data"):
            print(Fore.RED + "⚠️ No data found for this number.")
        else:
            for person in data["data"]:
                print(Fore.CYAN + "📋 --- User Information ---")
                print(Fore.YELLOW + f"📞 Mobile No      : {person.get('mobile', 'N/A')}")
                print(Fore.YELLOW + f"👨 Name           : {person.get('name', 'N/A')}")
                print(Fore.YELLOW + f"👴 Father Name    : {person.get('fname', 'N/A')}")
                print(Fore.YELLOW + f"🏠 Address        : {person.get('address', 'N/A')}")
                print(Fore.YELLOW + f"🪪 Aadhar ID      : {person.get('id', 'N/A')}")
                print(Fore.YELLOW + f"📧 Gmail          : {person.get('gmail', 'N/A')}")
                print(Fore.YELLOW + f"📱 Alt Number     : {person.get('alt_mobile', 'N/A')}")
                print(Fore.CYAN + "----------------------------\n")
    else:
        print(Fore.RED + f"❌ Server error: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(Fore.RED + f"⚠️ Network error: {e}")

