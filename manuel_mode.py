import tkinter as tk
import subprocess
from ctypes import windll

def show_coordinates(event):
    # PC ekranındaki koordinatları al
    x, y = event.x_root, event.y_root
    print(f"Ekran Koordinatları: ({x}, {y})")

def run_exe():
    exe_file_path = "scrcpy-win64-v2.4//scrcpy.exe"
    
    try:
        # .exe dosyasını çalıştır
        process = subprocess.Popen(
            [
                exe_file_path,
                "--prefer-text",
                "--turn-screen-off",
                "--stay-awake",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print("Exe file executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the exe file: {e}")

def manual_mode():
    run_exe()
    main_window.withdraw()  # Ana pencereyi gizle

    # Şeffaf bir pencere oluştur
    transparent_window = tk.Toplevel()
    transparent_window.title("Koordinatları Al")
    transparent_window.geometry("800x600")  # Pencere boyutu ayarla

    # Şeffaflık ve üstte olma
    transparent_window.attributes("-topmost", True)
    transparent_window.attributes("-transparentcolor", "white")
    transparent_window.configure(bg='white')
    
    # Pencereye tıklama olayını bind et
    transparent_window.bind("<Button-1>", show_coordinates)

def automatic_mode():
    print("Otomatik mod seçildi.")
    main_window.quit()  # Ana pencereyi kapat

# Ana pencere
main_window = tk.Tk()
main_window.title("Mod Seçimi")

manual_button = tk.Button(main_window, text="Manuel", command=manual_mode)
manual_button.pack(padx=10, pady=10)

automatic_button = tk.Button(main_window, text="Otomatik", command=automatic_mode)
automatic_button.pack(padx=10, pady=10)

main_window.mainloop()
