from tkinter import *
def about_game():
    window = Toplevel()
    window.title('About')

    canvas = Canvas(window, width=800, height=650)
    canvas.pack()
    about_bg = PhotoImage(file='About game-0.png')
    about_bg_l = canvas.create_image(0, 0, anchor=NW, image=about_bg)

    window.mainloop()