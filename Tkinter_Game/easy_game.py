from tkinter import *
from random import randint
import threading

#import winsound

def easy_game():
    window = Toplevel()
    window.title("Gameplay")
    window.geometry("800x650")
    w = 800
    h = 650
    x = w // 2
    y = h // 2
    my_canvas = Canvas(window, width=w, height=h)
    my_canvas.pack(pady=0)
    clouds = PhotoImage(file='citybg-3.png')
    cloud_background = my_canvas.create_image(0, 0, anchor=NW, image=clouds)
    img_L = PhotoImage(file='drone2.png')
    my_image_L = my_canvas.create_image(x, y, anchor=NW, image=img_L)
    global stop
    stop = PhotoImage(file='pause-button.png')
    #winsound.PlaySound("Alan-Walker-Force.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
    a = 0
    b = 0
    direction = ""
    global score
    score = 0
    score_label = Label(window, text=(f'Score: {score}'), bg='white', font=('arial', 20))
    score_label.place(x=10, y=10)
    obstacle_img_l = PhotoImage(file='missileleft.png')
    obstacle_img_r = PhotoImage(file='missileright.png')
    obstacle_img_u = PhotoImage(file='missileup.png')
    obstacle_img_d = PhotoImage(file='missiledown.png')

    def check_collision():
        collision = overlapping()
        pos = my_canvas.bbox(my_image_L)
        if pos[3] > h or pos[1] < 0 or pos[2] > w or pos[0] < 0:
            return True
        elif collision == True:
            return True



    global plane_speed_x,plane_speed_y
    plane_speed_x = 0.07
    plane_speed_y = 0.07

    def left(event):
        global score,plane_speed_x,plane_speed_y
        while True:
            try:
                check = check_collision()
                pos = my_canvas.bbox(my_image_L)
                #pos = my_canvas.coords(my_circle)
                if check == True:
                    end_label = Label(window, text=(f'Game over\nScore:{score}'), font=('arial', 15))
                    end_label.place(x=300, y=300)
                    score_label.destroy()
                    break
                #x = -0.05
                #y = 0
                my_canvas.move(my_image_L, -plane_speed_x, 0)
                #my_canvas.move(my_image_L, x, y)
                #my_canvas.move(my_circle, x, y)
                window.update()
            except:
                pass


    def right(event):
        global score,plane_speed_x,plane_speed_y
        while True:
            try:
                check = check_collision()
                pos = my_canvas.bbox(my_image_L)
                #pos = my_canvas.coords(my_circle)
                if check == True:
                    end_label = Label(window, text=(f'Game over\nScore:{score}'), font=('arial', 15))
                    end_label.place(x=300, y=300)
                    score_label.destroy()
                    break
                #x = 0.05
                #y = 0
                my_canvas.move(my_image_L, plane_speed_x, 0)
                #my_canvas.move(my_image_L, x, y)
                #my_canvas.move(my_circle, x, y)
                window.update()
            except:
                pass



    def up(event):
        global score,plane_speed_x,plane_speed_y
        while True:
            try:
                check = check_collision()
                pos = my_canvas.bbox(my_image_L)
                #pos = my_canvas.coords(my_circle)
                if check == True:
                    end_label = Label(window, text=(f'Game over\nScore:{score}'), font=('arial', 15))
                    end_label.place(x=300, y=300)
                    score_label.destroy()
                    break
                #x = 0
                #y = 0.05
                my_canvas.move(my_image_L, 0, plane_speed_y)
                #my_canvas.move(my_image_L, x, y)
                #my_canvas.move(my_circle, x, y)
                window.update()
            except:
                pass


    def down(event):
        global score,plane_speed_x,plane_speed_y
        while True:
            try:
                check = check_collision()
                pos = my_canvas.bbox(my_image_L)
                #pos = my_canvas.coords(my_circle)
                if check == True:
                    end_label = Label(window, text=(f'Game over\nScore:{score}'), font=('arial', 15))
                    end_label.place(x=300, y=300)
                    score_label.destroy()
                    break
                #x = 0
                #y = -0.05
                my_canvas.move(my_image_L, 0, -plane_speed_y)
                #my_canvas.move(my_image_L, x, y)
                #my_canvas.move(my_circle, x, y)
                window.update()
            except:
                pass

    def overlapping():
        for i in range(len(obstaclelist)):
            for j in range(len(obstaclelist[i])):
                pos = my_canvas.bbox(my_image_L)
                #pos = my_canvas.coords(my_circle)
                pos2 = my_canvas.bbox(obstaclelist[i][j])
                if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1]:
                    return True

    global balls
    balls = 10
    obstaclelistup = []
    obstaclelistdown = []
    obstaclelistleft = []
    obstaclelistright = []
    obstaclelist = [obstaclelistup, obstaclelistdown, obstaclelistleft, obstaclelistright]

    def obstacle_creation():
        check = check_collision
        for i in range(balls):
            global startaxis
            startaxis = randint(1, 4)
            if startaxis == 1:
                x = randint(10, 790)
                # xy = [x - 20, 630, x, 650]
                obstaclelistup.append(my_canvas.create_image(x, 650, image=obstacle_img_u))
                # obstaclelistup.append(my_canvas.create_rectangle(xy, fill="yellow"))
                direction = "down"
            if startaxis == 2:
                x = randint(10, 770)
                # xy = [x, 0, x + 20, 20]
                obstaclelistdown.append(my_canvas.create_image(x, 0, image=obstacle_img_d))
                direction = "up"
            if startaxis == 3:
                y = randint(10, 630)
                # xy = [0, y, 20, y + 20]
                obstaclelistright.append(my_canvas.create_image(0, y, image=obstacle_img_r))
                direction = "right"
            if startaxis == 4:
                y = randint(10, 620)

                # xy = [780, y - 20, 800, y]

                obstaclelistleft.append(my_canvas.create_image(800, y, image=obstacle_img_l))
                direction = "left"
        if check != True:
            threading.Timer(18, obstacle_creation).start()
        my_canvas.pack()

    global s
    s = 1
    def obstacle_movement():
        global score
        global s
        check = check_collision()

        for item in obstaclelistup:
            if check == True:
                end_label = Label(window, text=(f'Game over\nScore:{score}'), font=('arial', 15))
                end_label.place(x=300, y=300)
                score_label.destroy()
                break
            my_canvas.move(item, 0, -s)
            pos = my_canvas.bbox(item)
            if pos[3] < 0:
                obstaclelistup.remove(item)
        for item in obstaclelistdown:
            if check == True:
                end_label = Label(window, text=(f'Game over\nScore:{score}'), font=('arial', 15))
                end_label.place(x=300, y=300)
                score_label.destroy()
                break
            my_canvas.move(item, 0, s)
            pos = my_canvas.bbox(item)
            if pos[1] > 650:
                obstaclelistdown.remove(item)

        for item in obstaclelistleft:
            if check == True:
                end_label = Label(window, text=(f'Game over\nScore:{score}'), font=('arial', 15))
                end_label.place(x=300, y=300)
                score_label.destroy()
                break
            my_canvas.move(item, -s*1.23, 0)
            pos = my_canvas.bbox(item)
            if pos[2] < 0:
                obstaclelistleft.remove(item)
        for item in obstaclelistright:
            if check == True:
                end_label = Label(window, text=(f'Game over\nScore:{score}'), font=('arial', 15))
                end_label.place(x=300, y=300)
                score_label.destroy()
                break
            my_canvas.move(item, s*1.23, 0)
            pos = my_canvas.bbox(item)
            if pos[0] > 800:
                obstaclelistright.remove(item)
        my_canvas.after(25, obstacle_movement)


    def game_score():
        global score, s
        if s != 0:
            score += 1
            score_label.config(text=(f'Score:  {score}'))
        elif s == 0:
            score += 0
            score_label.config(text=(f'Score:  {score}'))

        my_canvas.after(1000, game_score)



    def cheat_code_speed(event):
        global s
        s = 0.5

    def cheat_code_speed_undo(event):
        global s
        s = 1

    def cheat_code_balls(event):
        global balls
        balls = 5

    def cheat_code_balls_undo(event):
        global balls
        balls = 10

    global pause_img
    def pause(event):
        global plane_speed_x, plane_speed_y, s,stop, pause_img
        plane_speed_x = 0
        plane_speed_y = 0
        s = 0
        pause_img = my_canvas.create_image(400, 300, anchor='nw', image=stop)

    def play(event):
        global pause_img
        global plane_speed_x, plane_speed_y, s
        plane_speed_x = 0.05
        plane_speed_y = 0.05
        s = 1
        my_canvas.delete(pause_img)

    def score_jump_cheat(event):
        global score
        score += 10

    def leave():
        window.destroy()




    exitButton = Button(window, text = 'Leave Game', command=leave, borderwidth=3, bg='Orange')
    exitButton.place(x=720, y=0)




    window.bind_all("<Left>", left)
    window.bind_all("<Right>", right)
    window.bind_all("<Down>", up)
    window.bind_all("<Up>", down)
    window.bind_all('<=>', cheat_code_speed)
    window.bind_all('<Delete>', cheat_code_speed_undo)
    window.bind_all('<space>', cheat_code_balls)
    window.bind_all('<Key-a>', cheat_code_balls_undo)
    window.bind_all('<Key-c>', pause)
    window.bind_all('<Key-d>', play)
    window.bind_all('<Key-b>', score_jump_cheat)
    while True:
        check = check_collision()
        if check != True:
            game_score()
            obstacle_creation()
            obstacle_movement()
            window.mainloop()