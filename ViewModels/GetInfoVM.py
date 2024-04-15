import tkinter as tk
from tkinter import messagebox

class MRPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MRP System")
        
        # labele
        self.labels = ["Czas realizacji =", "Wielkość partii =", "Poziom BOM =", "Na stanie ="]
        self.entries = []

        for i, label in enumerate(self.labels):
            tk.Label(root, text=label).grid(row=i, column=0)
            entry = tk.Entry(root)
            entry.grid(row=i, column=1)
            self.entries.append(entry)

        # przyciski okk i cancel
        self.cancel_button = tk.Button(root, text="Cancel", command=root.quit)
        self.cancel_button.grid(row=len(self.labels), column=0)
        self.ok_button = tk.Button(root, text="OK", command=self.save_data)
        self.ok_button.grid(row=len(self.labels), column=1)

    def save_data(self):
        # zapis cyferek
        self.czas_realizacji = self.entries[0].get()
        self.wielkosc_partii = self.entries[1].get()
        self.poziom_bom = self.entries[2].get()
        self.na_stanie = self.entries[3].get()
        
        # wyswietlanie danych do testow
        # print("Czas realizacji:", self.czas_realizacji)
        # print("Wielkość partii:", self.wielkosc_partii)
        # print("Poziom BOM:", self.poziom_bom)
        # print("Na stanie:", self.na_stanie)

        # message box potwierdzenie
        messagebox.showinfo("Info", "Data saved successfully.")
        
        self.root.destroy()

# Tworzenie okna
# root = tk.Tk()
# root.geometry("400x200")  
# app = MRPApp(root)
# root.mainloop()
