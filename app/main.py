import tkinter as tk
import modules.dexcomReadings as sugar

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Ustawienie okna w rogu ekranu
        self.geometry("-0+0")

        # Ustawienie przezroczystego tła
        self.attributes("-alpha", 0.8, '-topmost', True)
        self.overrideredirect(True)

        # Dodanie widgetu Label z tekstem
        self.label = tk.Label(self, text="Przykładowy tekst")
        self.label.config(font=("Arial", 15))
        self.label.pack()

        # Uruchomienie funkcji odświeżania co minutę
        self.label.configure(text='Loading...')
        self.refresh()

        # Dodanie menu kontekstowego
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Ustawienia", command=self.show_settings)
        self.bind("<Button-3>", self.show_context_menu)

        
    def refresh(self):
        # Funkcja odświeżania co minutę
        try: self.label.configure(text=F'{sugar.level()} {sugar.trendArrow()}')
        except: self.label.configure(text=F'')
        self.after(30000, self.refresh)

    def show_context_menu(self, event):
        # Wyświetlenie menu kontekstowego po kliknięciu prawym przyciskiem myszy
        self.context_menu.post(event.x_root, event.y_root)

    def show_settings(self):
        # Funkcja wyświetlająca okno ustawień
        settings_window = tk.Toplevel(self)
        settings_window.title("Ustawienia")
        # Dodaj widżety do okna ustawień

if __name__ == "__main__":
    app = App()
    app.mainloop()
    import time