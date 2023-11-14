from tkinter import Tk, Frame

ventana = Tk()
ventana.title("Mi Ventana")
ventana.geometry("450x250")

frame = Frame(ventana, height=250, width=450, bg="red")
frame.pack(padx=5, pady=5)

frame2 = Frame(frame, height=200, width=400, bg = "blue")
frame2.pack(padx=10, pady=10)

frame3 = Frame(frame2, height=150, width=400, bg = "blue")
frame3.pack(padx=10, pady=10)

ventana.mainloop()