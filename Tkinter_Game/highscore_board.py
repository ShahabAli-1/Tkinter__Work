from tkinter import *
def leader_board():
    root = Tk()
    root.title('LeaderBoard')
    root.geometry('800x650')

    e1 = Entry(root, width=50)
    e1.pack()
    e2 = Entry(root, width=50)
    e2.pack()
    def showscores():
        name = e1.get()
        score = e2.get()
        score = int(score)
        f = open('leader_board.txt', 'a')
        f.write(name+"."+str(score)+"\n")
        f.close()
        leadlist = []
        with open("leader_board.txt") as f:
            for line in f:
                line = line.rstrip('\n')
                tempo = line.split(".")
                leadlist.append(tempo)
        f.close()
        lst = len(leadlist)
        if len(leadlist)>=1:
            for i in range(0, lst):
                for j in range(0, lst-i-1):
                    if (int(leadlist[j][1]) < int(leadlist[j + 1][1])):
                        temp = leadlist[j]
                        leadlist[j]= leadlist[j + 1]
                        leadlist[j + 1]= temp
            print(leadlist)
        for m in range(5):
            try:
                print(f'{m+1}\t\t{playerlist[m]}\t\t{scorelist[m]}')
            except:
                break
        listbox = Listbox(root, bg="blue")
        listbox.pack(pady=30)
        listbox.insert(END, "  " + "Name" + "          "  + "Score")
        listbox.insert(END, ("1: " + str(leadlist[0][0]) + ("  " * (10-len(leadlist[0][0]))) + str(leadlist[0][1])))
        if len(leadlist) >= 2:
            listbox.insert(END, ("2: " + str(leadlist[1][0]) + ("  " * (10-len(leadlist[1][0])))+ str(leadlist[1][1])))
        if len(leadlist) >= 3:
            listbox.insert(END, ("3: " + str(leadlist[2][0]) + ("  " * (10-len(leadlist[2][0]))) + str(leadlist[2][1])))
        if len(leadlist) >= 4:
            listbox.insert(END, ("4: " + str(leadlist[3][0]) + ("  " * (10-len(leadlist[3][0]))) + str(leadlist[3][1])))
        if len(leadlist) >= 5:
            listbox.insert(END, ("5: " + str(leadlist[4][0]) + ("  " * (10-len(leadlist[4][0]))) + str(leadlist[4][1])))
    myButton = Button(root, text="Submit", command=showscores)
    myButton.pack()
    root.mainloop()
