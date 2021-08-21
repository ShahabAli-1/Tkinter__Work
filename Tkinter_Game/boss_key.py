from tkinter import *
def open_window():
    def boss_key():
        root = Toplevel()
        w = 1550
        h = 1000
        #canvas = Canvas(root, width=800, height=700)
        #canvas.pack()
        #def boss_key():
            #window = Tk()
            #window.title("Gameplay")
            #window.geometry("800x650")
            #canvas = Canvas(root, width=800, height=700)
            #canvas.pack()
        photo = PhotoImage(file='word.PNG')
        imagelabel = Label(root, image=photo)
        imagelabel.pack()
        #boss_key()
        root.mainloop()
    boss_key()
