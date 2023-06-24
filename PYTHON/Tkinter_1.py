import tkinter as tk

mywindow = tk.Tk()
    
mywindow.title("PYTHON + TKINTER GUI")
mywindow.geometry("800x500")
mywindow.resizable(False,False)
mywindow.config(background = "#2798FA")
main_title = tk.Label(text = "Tkinter GUI - JuanD - SebasV - EstebanQ", font = ("Selznick Remix NF", 14), bg = "#ff7763", fg = "black", width = "115", height = "5")
main_title.place(x = 0, y = 50)

mywindow.mainloop()
