import time
import webbrowser
from colorama import Fore, init

init(autoreset=True)  # Для цветного вывода

def fake_bios_cleaner():
    print(Fore.RED + "=== ОПАСНАЯ УТИЛИТА ОЧИСТКИ BIOS ===")
    print(Fore.YELLOW + "Инициализация доступа к системным разделам...\n")
    time.sleep(2)
    
    for i in range(10, 0, -1):
        print(Fore.CYAN + f"[!] До полной очистки BIOS: {i} сек...")
        time.sleep(1)
    
    print(Fore.RED + "\n[CRITICAL] Стираем BIOS...")
    print(Fore.GREEN + "████████████████████ 100%")
    time.sleep(1.5)
    
    print(Fore.MAGENTA + "\nJust kidding! Here's a fun song instead :)")
    webbrowser.open("https://www.youtube.com/watch?v=EkWIGzbqSSI&t=60s")

if __name__ == "__main__":
    fake_bios_cleaner()