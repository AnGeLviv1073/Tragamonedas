import tkinter as tk
from tkinter import Label, Button
import random
import threading
from PIL import Image, ImageTk
from slot_model import SlotMachine  # <-- Agregar esta línea

class SlotMachineView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Slot Machine")
        
        # Aumenta el tamaño de la ventana
        self.root.geometry("600x400")  # Establece un tamaño más grande

        # Color de fondo
        self.root.configure(bg="lightblue")  # Color de fondo de la ventana

        # Cambiar el tamaño de las etiquetas y los botones
        self.symbol_images = {}
        for symbol in SlotMachine.SYMBOLS:  # Ahora puede acceder a SlotMachine.SYMBOLS
            # Cargar imágenes PNG desde la carpeta "images"
            img = Image.open(f"images/{symbol}.png").resize((150, 150))  # Aumentar tamaño de imagen
            self.symbol_images[symbol] = ImageTk.PhotoImage(img)
        
        self.reel_labels = [Label(root, bg="lightblue") for _ in range(3)]
        for i, label in enumerate(self.reel_labels):
            label.grid(row=0, column=i, padx=20, pady=20)
            label.config(image=self.symbol_images["cherry"])  # Imagen por defecto

        self.balance_label = Label(root, text=f"Balance: $100", font=("Helvetica", 16), bg="lightblue")
        self.balance_label.grid(row=1, column=0, columnspan=3, pady=10)

        # Aumenta el tamaño y cambia color del botón
        self.spin_button = Button(root, text="SPIN", command=self.controller.handle_spin, font=("Helvetica", 18), bg="green", fg="white", height=2, width=10)
        self.spin_button.grid(row=2, column=1, pady=20)

    def update_reels(self, results):
        # Actualiza las imágenes de los rodillos (reels)
        for i in range(3):
            self.reel_labels[i].config(image=self.symbol_images[results[i]])

    def update_balance(self, balance):
        self.balance_label.config(text=f"Balance: ${balance}")
