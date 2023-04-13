
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

#colors

color1 = '#3b3b3b' # black
color2 = '#ffffff' # white
color3 = '#48b3e0' # blue

janela = Tk()
janela.title('')
janela.geometry('650x260')
janela.configure(bg=color1)

# Window Frames

frame_up = Frame(janela, width=450, height=50, bg=color2, pady=0, padx=3, relief='flat')
frame_up.place(x=2, y=2)

frame_left = Frame(janela, width=450, height=220, bg=color2, pady=0, padx=3, relief='flat')
frame_left.place(x=2, y=55)

frame_right = Frame(janela, width=198, height=260, bg=color2, pady=0, padx=3, relief='flat')
frame_right.place(x=455, y=2)

# Window Style

style = ttk.Style(janela)
style.theme_use("clam")

# Up Frame Config

l_app_name = Label(frame_up, text='Unit Calculator', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=color2, fg=color3)
l_app_name.place(x=80, y=10)

# Button Weight

w=130 #buttun width

img_0 = Image.open('icons/weight.png')
img_0 = img_0.resize((50,50), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)
button0 = Button(frame_left, text='Weight', image=img_0, compound=LEFT, width=125, height=50, overrelief='solid', relief='flat', anchor='center', font=('Ivy 10 bold'), bg=color3, fg=color2)
button0.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)

# Button Time
img_1 = Image.open('icons/time.png')
img_1 = img_1.resize((50,50), Image.ANTIALIAS)
img_1 = ImageTk.PhotoImage(img_1)
button1 = Button(frame_left, text='Time', image=img_1, compound=LEFT, width=w, height=50, overrelief='solid', relief='flat', anchor='center', font=('Ivy 10 bold'), bg=color3, fg=color2)
button1.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5)

# Button Length
img_2 = Image.open('icons/length.png')
img_2 = img_2.resize((50,50), Image.ANTIALIAS)
img_2 = ImageTk.PhotoImage(img_2)
button2 = Button(frame_left, text='Length', image=img_2, compound=LEFT, width=w, height=50, overrelief='solid', relief='flat', anchor='center', font=('Ivy 10 bold'), bg=color3, fg=color2)
button2.grid(row=0, column=2, sticky=NSEW, padx=5, pady=5)

# Button Area
img_3 = Image.open('icons/area.png')
img_3 = img_3.resize((50,50), Image.ANTIALIAS)
img_3 = ImageTk.PhotoImage(img_3)
button3 = Button(frame_left, text='  Area', image=img_3, compound=LEFT, width=w, height=50, overrelief='solid', relief='flat', anchor='center', font=('Ivy 10 bold'), bg=color3, fg=color2)
button3.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)

# Button Volume
img_4 = Image.open('icons/volume.png')
img_4 = img_4.resize((50,50), Image.ANTIALIAS)
img_4 = ImageTk.PhotoImage(img_4)
button4 = Button(frame_left, text='Volume', image=img_4, compound=LEFT, width=w, height=50, overrelief='solid', relief='flat', anchor='center', font=('Ivy 10 bold'), bg=color3, fg=color2)
button4.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5)

# Button Speed
img_5 = Image.open('icons/speed.png')
img_5 = img_5.resize((50,50), Image.ANTIALIAS)
img_5 = ImageTk.PhotoImage(img_5)
button5 = Button(frame_left, text='Speed', image=img_5, compound=LEFT, width=w, height=50, overrelief='solid', relief='flat', anchor='center', font=('Ivy 10 bold'), bg=color3, fg=color2)
button5.grid(row=1, column=2, sticky=NSEW, padx=5, pady=5)

# Button Temperature
img_6 = Image.open('icons/temperature.png')
img_6 = img_6.resize((50,50), Image.ANTIALIAS)
img_6 = ImageTk.PhotoImage(img_6)
button6 = Button(frame_left, text='Temperature', image=img_6, compound=LEFT, width=w, height=50, overrelief='solid', relief='flat', anchor='center', font=('Ivy 9 bold'), bg=color3, fg=color2)
button6.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)

# Button Energy
img_7 = Image.open('icons/energy.png')
img_7 = img_7.resize((50,50), Image.ANTIALIAS)
img_7 = ImageTk.PhotoImage(img_7)
button7 = Button(frame_left, text='Energy', image=img_7, compound=LEFT, width=w, height=50, overrelief='solid', relief='flat', anchor='center', font=('Ivy 10 bold'), bg=color3, fg=color2)
button7.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)

# Button Pressure
img_8 = Image.open('icons/pressure.png')
img_8 = img_8.resize((50,50), Image.ANTIALIAS)
img_8 = ImageTk.PhotoImage(img_8)
button8 = Button(frame_left, text='Pressure', image=img_0, compound=LEFT, width=w, height=50, overrelief='solid', relief='flat', anchor='center', font=('Ivy 10 bold'), bg=color3, fg=color2)
button8.grid(row=2, column=2, sticky=NSEW, padx=5, pady=5)

janela.mainloop()

#Right Frame