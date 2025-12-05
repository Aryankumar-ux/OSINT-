import requests as r
import json
import time as t
import os
import sys
from colorama import init, Fore, Style, Back

# Initialize colorama for Windows compatibility
init(autoreset=True)

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print colorful banner"""
    banner = f"""
{Fore.CYAN}{'='*60}
{Fore.YELLOW}╔═══════════════════════════════════════════════════════╗
{Fore.GREEN}║        📱 {Fore.MAGENTA}MOBILE NUMBER INFO FINDER{Fore.GREEN} 📱         ║
{Fore.YELLOW}╚═══════════════════════════════════════════════════════╝
{Fore.CYAN}{'='*60}{Style.RESET_ALL}
"""
    print(banner)

def print_loading(text):
    """Print animated loading text"""
    print(f"\n{Fore.YELLOW}[{Fore.CYAN}*{Fore.YELLOW}] {text}", end="", flush=True)
    for _ in range(3):
        print(f"{Fore.CYAN}.{Style.RESET_ALL}", end="", flush=True)
        t.sleep(0.3)
    print()

def print_success(text):
    """Print success message"""
    print(f"{Fore.GREEN}✅ {text}{Style.RESET_ALL}")

def print_error(text):
    """Print error message"""
    print(f"{Fore.RED}❌ {text}{Style.RESET_ALL}")

def print_info(text):
    """Print info message"""
    print(f"{Fore.CYAN}ℹ️  {text}{Style.RESET_ALL}")

def print_warning(text):
    """Print warning message"""
    print(f"{Fore.YELLOW}⚠️  {text}{Style.RESET_ALL}")

def animate_text(text, color=Fore.CYAN, delay=0.03):
    """Animate text character by character"""
    for char in text:
        print(f"{color}{char}{Style.RESET_ALL}", end='', flush=True)
        t.sleep(delay)
    print()

def find():
    clear_screen()
    print_banner()
    
    n = ''
    while True:
        try:
            print(f"\n{Fore.MAGENTA}{'─'*40}")
            num = input(f"{Fore.CYAN}📞 {Fore.YELLOW}Enter Mobile Number: {Fore.GREEN}")
            print(f"{Fore.MAGENTA}{'─'*40}")
            
            if num.lower() == 'exit':
                print(f"\n{Fore.YELLOW}👋 Goodbye! Thanks for using!{Style.RESET_ALL}")
                sys.exit(0)
                
            if num.isnumeric():
                if len(str(num)) <= 12 and len(str(num)) >= 10:
                    if len(str(num)) == 12 and num.startswith('91'):
                        n = num[2:]
                        print_success(f"Number processed: +91-{n}")
                        break
                    else:
                        if len(str(num)) == 10:
                            n = num
                            print_success(f"Number processed: +91-{n}")
                            break
                        else:
                            print_error("🇮🇳 Only Indian numbers allowed (10 digits or 12 starting with 91)")
                else:
                    print_error("📏 Please enter 10 or 12 digit number")
            else:
                print_error("🔢 Only numbers allowed")
                
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}\n👋 Process interrupted!{Style.RESET_ALL}")
            return
    
    if not n:
        return
    
    print_loading(f"{Fore.CYAN}Searching database")
    
    url = f'https://api.b77bf911.workers.dev/mobile?number={int(n)}'
    
    try:
        response = r.get(url, timeout=10)
        text = response.json()
        
        clear_screen()
        print_banner()
        
        if 'data' in text and 'result' in text['data'] and text['data']['result']:
            print_success(f"🎉 {Fore.GREEN}Found {len(text['data']['result'])} record(s) for {Fore.YELLOW}+91-{n}")
            print(f"\n{Fore.MAGENTA}{'═'*60}{Style.RESET_ALL}")
            
            for idx, i in enumerate(text['data']['result'], 1):
                # Animate record header
                animate_text(f"\n📋 Record #{idx}", Fore.YELLOW, 0.02)
                print(f"{Fore.MAGENTA}{'─'*40}")
                
                # Display each field with animation
                fields = [
                    (f"📱 {Fore.CYAN}Mobile Number:", f"{Fore.GREEN}{i.get('mobile', 'N/A')}"),
                    (f"👤 {Fore.CYAN}Name:", f"{Fore.GREEN}{i.get('name', 'N/A')}"),
                    (f"👨 {Fore.CYAN}Father's Name:", f"{Fore.GREEN}{i.get('father_name', 'N/A')}"),
                    (f"🏠 {Fore.CYAN}Address:", f"{Fore.GREEN}{i.get('address', 'N/A')}"),
                    (f"📞 {Fore.CYAN}Alternate Number:", f"{Fore.GREEN}{i.get('alt_mobile', 'N/A')}"),
                    (f"📍 {Fore.CYAN}Circle:", f"{Fore.GREEN}{i.get('circle', 'N/A')}"),
                    (f"🆔 {Fore.CYAN}Aadhar ID:", f"{Fore.GREEN}{i.get('id_number', 'N/A')}"),
                    (f"📧 {Fore.CYAN}Email ID:", f"{Fore.GREEN}{i.get('email', 'N/A')}")
                ]
                
                for label, value in fields:
                    print(f"  {label:25} {value}{Style.RESET_ALL}")
                    t.sleep(0.1)
                
                print(f"{Fore.MAGENTA}{'─'*40}")
                t.sleep(0.3)
                
        else:
            print_error("📭 No data found for this number")
            
    except r.exceptions.Timeout:
        print_error("⏰ Request timeout! Please try again")
    except r.exceptions.ConnectionError:
        print_error("🌐 Connection error! Check your internet")
    except json.JSONDecodeError:
        print_error("📄 Error parsing response data")
    except Exception as e:
        print_error(f"🔴 Error: {str(e)}")
    
    # Ask if user wants to continue
    print(f"\n{Fore.CYAN}{'─'*40}")
    choice = input(f"{Fore.YELLOW}🔄 Search another number? (y/n): {Fore.GREEN}").lower()
    
    if choice not in ['y', 'yes', '']:
        print(f"\n{Fore.YELLOW}🌟 Thank you for using! Goodbye! 🌟{Style.RESET_ALL}")
        sys.exit(0)

def main():
    """Main function with continuous loop"""
    while True:
        try:
            find()
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}\n👋 Thanks for using! Goodbye!{Style.RESET_ALL}")
            break
        except Exception as e:
            print_error(f"Unexpected error: {str(e)}")
            t.sleep(2)

if __name__ == "__main__":
    # Check if colorama is installed
    try:
        from colorama import init, Fore, Style, Back
    except ImportError:
        print("\n⚠️  Please install colorama first: pip install colorama")
        sys.exit(1)
    
    main()