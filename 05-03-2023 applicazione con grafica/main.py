import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text="Hello, Tkinter",#scrivo in una posizione indefinita
    foreground="white",  # setto il colore delle scritte
    background="black"  # setto lo sfondo
)
label.pack()
window.mainloop()