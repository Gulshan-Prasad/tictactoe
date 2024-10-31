import tkinter as tk

window = tk.Tk()
window.title("My Tic Tac Toe Game")
window.geometry("700x600")

label = tk.Label(window, text="TIC TAC TOE GAME", font=("Arial", 25))
label.place(x=180,y=40)

frame = tk.Frame(window, width=300, height=300, bg="grey")
frame.place(x=200,y=220)

frame1 = tk.Frame(window, width=565, height=50, bg="#FFF8B2")
frame1.place(x=60,y=155)

player=1

flag=0


#Turn for players
def turn():
    if player % 2 == 0:
        Players.config(text="Player 2 turn: (X) ")
        Players.place(x=330,y=1)
    else:
        Players.config(text="Player 1 turn: (O) ")
        Players.place(x=10,y=1)
    game_over()
    move=player-1
    print(move)
    if move==9:
        if flag==0:
            game_tie()
            print("tie")
            

#command for all buttons to show "O" or "X"
def b11():
    global player
    if player % 2 == 0:
        button11.config(text="X")
    else:
        button11.config(text="O")
    player=player+1
    turn()
def b12():
    global player
    if player % 2 == 0:
        button12.config(text="X")
    else:
        button12.config(text="O")
    player=player+1
    turn()
def b13():
    global player
    if player % 2 == 0:
        button13.config(text="X")
    else:
        button13.config(text="O")
    player=player+1
    turn()
def b21():
    global player
    if player % 2 == 0:
        button21.config(text="X")
    else:
        button21.config(text="O")
    player=player+1
    turn()
def b22():
    global player
    if player % 2 == 0:
        button22.config(text="X")
    else:
        button22.config(text="O")
    player=player+1
    turn()
def b23():
    global player
    if player % 2 == 0:
        button23.config(text="X")
    else:
        button23.config(text="O")
    player=player+1
    turn()
def b31():
    global player
    if player % 2 == 0:
        button31.config(text="X")
    else:
        button31.config(text="O")
    player=player+1
    turn()
def b32():
    global player
    if player % 2 == 0:
        button32.config(text="X")
    else:
        button32.config(text="O")
    player=player+1
    turn()
def b33():
    global player
    if player % 2 == 0:
        button33.config(text="X")
    else:
        button33.config(text="O")
    player=player+1
    turn()

#winning UX
def player1_won():
    global endf
    global restartB
    endf=tk.Canvas(window, bg="lime", width=580, height=110)
    endf.place(x=40,y=95)
    tk.Label(endf, text="Player 1(O) Won!!", font=("Arial", 38), bg="lime", fg="magenta").place(x=70,y=20)
    restartB=tk.Button(window, text="RESTART",font=("Arial", 20),command=restart)
    restartB.place(x=230,y=500)
def player2_won():
    global endf
    global restartB
    endf=tk.Canvas(window, bg="lime", width=580, height=110)
    endf.place(x=40,y=95)
    tk.Label(endf, text="Player 2(X) Won!!", font=("Arial", 38), bg="lime", fg="magenta").place(x=70,y=20)
    restartB=tk.Button(window, text="RESTART",font=("Arial", 20),command=restart)
    restartB.place(x=230,y=500)
def game_tie():
    global endf
    global restartB
    global winL
    winL=tk.Canvas(window,width=0, height=0, bg="#E53434")
    winL.place(x=1,y=1)
    endf=tk.Canvas(window, bg="yellow", width=580, height=110)
    endf.place(x=40,y=95)
    tk.Label(endf, text="GAME TIE!!", font=("Arial", 38), bg="yellow", fg="red").place(x=100,y=20)
    restartB=tk.Button(window, text="RESTART",font=("Arial", 20),command=restart)
    restartB.place(x=230,y=500)


#all cases to win
def game_over():
    global flag
    global winL
    if button11["text"]==button12["text"] and button12["text"]==button13["text"] and button11["text"]!="":
        winL=tk.Canvas(window,width=250, height=4, bg="#E53434")
        winL.place(x=180,y=255)
        if button11["text"] == "O":
            player1_won()
        if button11["text"] == "X":
            player2_won()
        flag=1
    if button21["text"]==button22["text"] and button22["text"]==button23["text"] and button21["text"]!="":
        winL=tk.Canvas(window,width=250, height=4, bg="#E53434")
        winL.place(x=180,y=330)
        if button21["text"] == "O":
            player1_won()
        if button21["text"] == "X":
            player2_won()
        flag=1
    if button31["text"]==button32["text"] and button32["text"]==button33["text"] and button31["text"]!="":
        winL=tk.Canvas(window,width=250, height=4, bg="#E53434")
        winL.place(x=180,y=404)
        if button31["text"] == "O":
            player1_won()
        if button31["text"] == "X":
            player2_won()
        flag=1
    if button11["text"]==button21["text"] and button21["text"]==button31["text"] and button11["text"]!="":
        winL=tk.Canvas(window,width=4, height=250, bg="#E53434")
        winL.place(x=230,y=205)
        if button11["text"] == "O":
            player1_won()
        if button11["text"] == "X":
            player2_won()
        flag=1
    if button12["text"]==button22["text"] and button22["text"]==button32["text"] and button12["text"]!="":
        winL=tk.Canvas(window,width=4, height=250, bg="#E53434")
        winL.place(x=300,y=205)
        if button12["text"] == "O":
            player1_won()
        if button12["text"] == "X":
            player2_won()
        flag=1
    if button13["text"]==button23["text"] and button23["text"]==button33["text"] and button13["text"]!="":
        winL=tk.Canvas(window,width=4, height=250, bg="#E53434")
        winL.place(x=370,y=205)
        if button12["text"] == "O":
            player1_won()
        if button12["text"] == "X":
            player2_won()
        flag=1
    if button11["text"]==button22["text"] and button22["text"]==button33["text"] and button11["text"]!="":
        winL=tk.Canvas(window,width=0, height=0, bg="#E53434")
        winL.place(x=1,y=1)
        if button11["text"] == "O":
            player1_won()
        if button11["text"] == "X":
            player2_won()
        flag=1
    if button13["text"]==button22["text"] and button22["text"]==button31["text"] and button13["text"]!="":
        winL=tk.Canvas(window,width=0, height=0, bg="#E53434")
        winL.place(x=1,y=1)
        if button13["text"] == "O":
            player1_won()
        if button13["text"] == "X":
            player2_won()
        flag=1


#for restart the game
def restart():
    global player
    global endf
    global winL
    player=1
    Players.config(text="Player 1 turn: (O) ")
    Players.place(x=10,y=1)
    button11.config(text="")
    button12.config(text="")
    button13.config(text="")
    button21.config(text="")
    button22.config(text="")
    button23.config(text="")
    button31.config(text="")
    button32.config(text="")
    button33.config(text="")
    winL.place_forget()
    endf.place_forget()
    restartB.place_forget()


Players= tk.Label(frame1,text="Player 1 Turn: (O) ", font=("Arial",20), bg="#FFF8B2", width=14, height=1)
Players.place(x=10,y=1)  


button11 = tk.Button(frame, text="",command=b11, height=4, width=8)
button11.grid(row=1,column=1, padx=2, pady=2)
button12 = tk.Button(frame, text="",command=b12, height=4, width=8)
button12.grid(row=1,column=2, padx=2, pady=2)
button13 = tk.Button(frame, text="",command=b13, height=4, width=8)
button13.grid(row=1,column=3, padx=2, pady=2)
button21 = tk.Button(frame, text="",command=b21, height=4, width=8)
button21.grid(row=2,column=1, padx=2, pady=2)
button22 = tk.Button(frame, text="",command=b22, height=4, width=8)
button22.grid(row=2,column=2, padx=2, pady=2)
button23 = tk.Button(frame, text="",command=b23, height=4, width=8)
button23.grid(row=2,column=3, padx=2, pady=2)
button31 = tk.Button(frame, text="",command=b31, height=4, width=8)
button31.grid(row=3,column=1, padx=2, pady=2)
button32 = tk.Button(frame, text="",command=b32, height=4, width=8)
button32.grid(row=3,column=2, padx=2, pady=2)
button33 = tk.Button(frame, text="",command=b33, height=4, width=8)
button33.grid(row=3,column=3, padx=2, pady=2)



window.mainloop()

