import time
import webbrowser

def fake_bios_cleaner():
    print("\033[91m=== ОПАСНАЯ УТИЛИТА ОЧИСТКИ BIOS ===")  # Красный
    print("\033[93mИнициализация доступа к системным разделам...\n")  # Желтый
    
    for i in range(10, 0, -1):
        print(f"\033[96m[!] До полной очистки BIOS: {i} сек...")  # Голубой
        time.sleep(1)
    
    print("\033[91m\n[CRITICAL] Стираем BIOS...")  # Красный
    print("\033[92m████████████████████ 100%")  # Зеленый
    time.sleep(1.5)
    
    print("\033[95m\nJust kidding! Here's a fun song instead :)")  # Фиолетовый
    webbrowser.open("https://www.youtube.com/watch?v=EkWIGzbqSSI&t=60s")

if __name__ == "__main__":
    fake_bios_cleaner()
