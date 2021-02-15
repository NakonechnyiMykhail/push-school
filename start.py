from tkinter import *
#from PIL import Image, ImageTk # jpg

def hello():
    print('hello')


root = Tk()

root.geometry("500x500")

bg = PhotoImage(file="space.png") # PNG

img = Label(root, image=bg)
img.image = bg
img.place(x=0, y=0)

btn = Button(root, text="My button", bg='green', fg='blue', font=('times', 20, 'bold'), command=hello)
btn.place(x=200, y=100, width=150, height=50)
#btn.pack() # pady=20

btn1 = Button(root, text="My button 1", bg='green', fg='blue', font=('times', 20, 'bold'), command=hello)
btn1.place(x=50, y=140, width=150, height=50)
#btn1.pack() # pady=20

root.mainloop()





















# root.geometry("500x500")
# bg = PhotoImage(file="space1.png") # PNG
# #load = Image.open("space.jpg")
# #render = ImageTk.PhotoImage(load)
# img = Label(root, image=bg)
# img.image = bg
# img.place(x=0, y=0)

# lbl = Label(root, text="Welcome", bg="#fff000")
# lbl.pack(pady=50)

    # frame = Frame(root, bg="#ffffff") # #000000 = black color
    # frame.pack(pady=20)

    # center 
    # x - ??? 
    # geometry_width = 500 -> / 2 -> 250
    # button_width = 100 -> /2 -> 50
    # center_x = geometry_width - button_width = 200