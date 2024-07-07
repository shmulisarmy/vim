import tkinter as tk
from typing_extensions import Text
from colors import blue
from searchTree import SearchTree
from utils import clearScreen


from __init__ import *


wordTree = SearchTree()








def process_command(inp):
    if inp == 'BackSpace':
        c.enterDeleteMode()
        return

    if inp == 'Meta_R':
        c.previos_mode = c.mode
        c.mode = 'command'
        return
    if inp in [str(i) for i in range(1, 10+1)]:
        c.previos_mode = c.mode
        c.mode = 'motion'
        c.motion_amount = int(inp)
        return

    if c.mode == 'insert':
        if inp == 'space':
            wordTree.insert(c.get_current_word())
            b.write_char(' ')
            return
        b.write_char(inp)
        return
    if c.mode == 'command':
        command_key = inp
        vimCommandMap[command_key]()
        return



    if c.mode == 'motion':
        command_key = inp
        if c.previos_mode == 'delete':
            c.enterGrabMode()
            vimMotionMap[command_key](int(c.motion_amount))
            b.backSpace()
            c.mode = 'insert'
            return
        vimMotionMap[command_key](int(c.motion_amount))
        temp = c.mode
        c.mode = c.previos_mode
        c.previos_mode = temp


    if inp[0] == 'm':
        for command in vimMacros[inp[1]]:
            process_command(command)
        return
    if inp[0] == 'r':
        for letter in vimregisters[inp[1]]:
            b.write_char(letter)
        return

         if len(inp) == 3:
            if inp[:-1] == "di":
                b.deleteInside((inp[-1]))
            else:
                vimCommandMap[inp]()







vimMotionMap = {
    'j': c.j,
    'k': c.k,
    'h': c.h,
    'l': c.l,
    'w': c.w,
    'b': c.b
}


vimCommandMap = {
    'g': c.enterGrabMode,
    'b': c.enterDeleteMode,
    'c': b.commandEnter,
}


vimMacros = {
    'd': [
        'ggg',
        '4b',
        'bbb',
    ]
}

vimregisters = {
    't': "hello world how are you doing"
}


def on_key_press(event):
    currentChar = event.keysym
    process_command(currentChar)
    print(f"cursor mode = {c.mode}", end='\n')
    b.display()



root = tk.Tk()
root.geometry("400x200")
root.bind('<KeyPress>', on_key_press)
root.mainloop()
