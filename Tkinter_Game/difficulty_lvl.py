from tkinter import *
def game_difficulty():
    window = Toplevel()
    window.title('DIFFICULTY LEVEL')
    window.geometry('800x650')
    image = PhotoImage(file='lvl-bg.png')
    image_label = Label(window, image=image)
    image_label.pack()
    label = Label(window, text='CHOOSE DIFFICULTY', bg='Grey', font=('times',30))
    label.place(x=250, y=100)
    def easy():
        from easy_game import easy_game
        easy_game()
    def medium():
        from medium_game import medium_game
        medium_game()
    def hard():
        from hard_game import hard_game
        hard_game()

    easy_button = Button(window, text = 'EASY', bg= 'purple',command=easy, font=('Times', 25))
    easy_button.place(x=250, y=170)
    medium_button = Button(window, text='MEDIUM', bg='purple', command=medium, font=('times', 25))
    medium_button.place(x=250, y=250)
    hard_button = Button(window, text='HARD',bg= 'purple', command=hard, font=('times', 25))
    hard_button.place(x=250, y=330)

    def leave():
        window.destroy()


    exitButton = Button(window, text = 'Return', command=leave, bg='Purple',font=('times', 25))
    exitButton.place(x=250, y=410)
    window.mainloop()










