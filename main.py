import tkinter as tk
from calendario_utils import mostrar_calendario

root = tk.Tk()
root.title("Calendario")

año_entry = tk.Entry(root)
año_entry.insert(0, "2024")
año_entry.pack()

mes_entry = tk.Entry(root)
mes_entry.insert(0, "9")
mes_entry.pack()

boton = tk.Button(root, text="Mostrar Calendario", command=lambda: mostrar_calendario(int(año_entry.get()), int(mes_entry.get()), label))
boton.pack()


label = tk.Label(root, text="", font=("Courier", 12))
label.pack()

root.mainloop()