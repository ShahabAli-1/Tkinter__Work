from tkinter import *


window = Tk()
window.title("Python Game")

window.geometry("800x600")

photo = PhotoImage(file="menu--bg.png")
label = Label(image=photo)
label.pack()
play_button = PhotoImage(file='start-png-44887.png')
label2 = Label(image=play_button)
quit_btn = PhotoImage(file='quitbtn5.png')
label3 = Label(image=quit_btn)
highscore_btn = PhotoImage(file='leaderboard-icon-13756.png')
label4 = Label(image=highscore_btn)
about_button = PhotoImage(file='about-2.png')
label5 = Label(image=about_button)
title_image = PhotoImage(file='menu--bg-2.png')
label_text = Label(window, image=title_image, bg='lightgreen')
label_text.place(x=100, y=80)
def close_window():
    window.destroy()
def game_run():
    from difficulty_lvl import game_difficulty
    game_difficulty()
def boss(event):
    from boss_key import open_window
    open_window()
def about_info():
    from about import about_game
    about_game()
def high_score():
    from highscore_board import leader_board
    leader_board()
playButton = Button(window,image = play_button,command=game_run, borderwidth=3, bg='lightblue')
playButton.place(x=400, y=190)
exitButton = Button(window, image=quit_btn, command=close_window, borderwidth=3, bg='black')
exitButton.place(x=400, y=390)
level_btn = Button(window, image=about_button, command=about_info, borderwidth=3, bg='lightblue')
level_btn.place(x=100, y=370)
highscoreButton = Button(window, image=highscore_btn, command=high_score, borderwidth=3, bg='lightblue')
highscoreButton.place(x=100, y=200)
window.bind_all('<Return>', boss)


window.mainloop()