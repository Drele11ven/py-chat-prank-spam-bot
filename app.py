import pyautogui as pg
import time
import tkinter as tk

def start_program():
    time.sleep(5)

    txt = open('animals.txt' , 'r')


    for i in txt:
        pg.write("you are a " + i)
        pg.press('Enter')

window = tk.Tk()


window.resizable(False, False)
window.bind('<Escape>', lambda e, w=window: w.destroy())
window.title("Web InLine Spammer Bot")
window.geometry('600x250')

description_label = tk.Label(window , text="\nA spammer by Dr.ele11ven that will work with ever web social media")
description_label.pack()

description_label = tk.Label(window , text="\n\npress start to lunch attack than click on chat box stay still\n")
description_label.pack()


start_button = tk.Button(window, text="   Start   ", command = start_program)
start_button.pack()

description_label = tk.Label(window , text="\n\npress Esc key to close and stop the attack")
description_label.pack()

window.mainloop()
