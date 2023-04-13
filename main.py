
from tkinter import *
from tkinter import ttk

#color

color1 = '#3b3b3b'
color2 = '#3b3b3b'

janela = Tk()
janela.title('')
janela.geometry('650x260')
janela.configure(bg=color1)

# Window Frames

frame_up = Frame(janela, width=450, height=50, bg='red', pady=0, padx=3, relief='flat')
frame_up.place(x=2, y=2)

frame_left = Frame(janela, width=450, height=220, bg='green', pady=0, padx=3, relief='flat')
frame_left.place(x=2, y=54)

frame_right = Frame(janela, width=198, height=260, bg='white', pady=0, padx=3, relief='flat')
frame_right.place(x=455, y=2)

janela.mainloop()