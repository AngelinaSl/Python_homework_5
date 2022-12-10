
# Создайте программу для игры в ""Крестики-нолики"".
#



from tkinter import *
import tkinter.constants
import random
import time

def win_positions(s: str):
    global running
    if running[0] == s and running[1] == s and running[2] == s \
            or running[3] == s and running[4] == s and running[5] == s\
            or running[6] == s and running[7] == s and running[8] == s\
            or running[0] == s and running[3] == s and running[6] == s\
            or running[1] == s and running[4] == s and running[7] == s\
            or running[2] == s and running[5] == s and running[8] == s\
            or running[0] == s and running[4] == s and running [8] == s\
            or running[2] == s and running[4] == s and running[6] == s:
        return True


def stop_game():
    global position_numbers
    for i in position_numbers:
        buttons[i].config(text="☃", bg="#761A1A", state="disabled")
def click(b):
    global running
    global position_numbers
    global turn
    running[b] = "X"
    buttons[b].config(text="X", bg="#761A1A", state="disabled")
    position_numbers.remove(b)
    if b == 4 and turn == 0:
        r = random.choice(position_numbers)
    elif b != 4 and turn == 0:
        r = 4
    if turn > 0:
        r = 8 - b
    if r not in position_numbers:
        try:
            r = random.choice(position_numbers)
        except IndexError:
            label_1["text"] = "Игра окончена"
            stop_game()
    running[r] = "0"
    time.sleep(0.2)
    buttons[r].config(text="0", bg="#761A1A", state="disabled")

    if win_positions("X"):
        label_1["text"] = "Вы победили!"
        stop_game()
    elif win_positions("0"):
        label_1["text"] = "Вы проиграли!"
        stop_game()
    else:
        if len(position_numbers) > 1:

            position_numbers.remove(r)
        else:
            label_1["text"] = "Игра окончена"
            stop_game()
        turn += 1



running = [None] * 9
position_numbers = list(range(9))
turn = 0

game = Tk()
game.title('Крестики-нолики')
game.geometry("376x398+150+150")
game.config(bg="black")

label_1 = Label(game, width=20, text='Игра ❆крестики-нолики☃',
                bg='#830e10', fg='#e9e5e1', padx=10, relief=tkinter.constants.RAISED, font=("Arial", 18, 'italic'))
label_1.grid(row=0, column=0, columnspan=3)

buttons = [Button(game, text="❆", width=5, height=2, bg='#1f3102',
                  activebackground="#60A135", font=("Arial", 28, 'bold'), command=lambda x=i: click(x)) for i in
           range(9)]

rows = 1
columns = 0
for i in range(9):
    buttons[i].grid(row=rows, column=columns)
    columns += 1
    if columns == 3:
        rows += 1
        columns = 0

game.mainloop()
