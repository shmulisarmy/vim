import sys
from typing_extensions import Text
from colors import blue
from searchTree import SearchTree
from utils import clearScreen

#for entering text
import sys
import tty
import termios


fd = sys.stdin.fileno()
tty.setraw(fd)
#for entering text



from __init__ import *


wordTree = SearchTree()








def process_command(inp):
    inp: str # len = 1
    if inp == '+':
        c.previos_mode = c.mode
        c.mode = 'command'
        return
    if inp in [str(i) for i in range(1, 10+1)]:
        c.previos_mode = c.mode
        c.mode = 'motion'
        c.motion_amount = int(inp)
        return

    if c.mode == 'insert':
        if input == ' ':
            wordTree.insert(c.get_current_word())
        b.write_char(inp)
        return
    if c.mode == 'command':
        command_key = inp
        vimCommandMap[command_key]()
        return



    if c.mode == 'motion':
        command_key = inp
        vimMotionMap[command_key](int(c.motion_amount))
        temp = c.mode
        c.mode = c.previos_mode
        c.previos_mode = temp


    # if inp[0] == 'm':
    #     for command in vimMacros[inp[1]]:
    #         process_command(command)
    #     return
    # if inp[0] == 'r':
    #     for letter in vimregisters[inp[1]]:
    #         b.write_char(letter)
    #     return
    #
    #      if len(inp) == 3:
    #         if inp[:-1] == "di":
    #             b.deleteInside((inp[-1]))
    #         else:
    #             vimCommandMap[inp]()







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
    'b': b.backSpace,
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




while True:
    clearScreen()
    print(" - - - - - -")
    clearScreen()
    print(wordTree.root)
    clearScreen()
    print(f"{c.get_current_word() = }")
    clearScreen()
    print(wordTree.firstNThatStartWith(5, c.get_current_word()))
    clearScreen()
    print(" - - - - - -")
    clearScreen()
    print(f"cursor mode = {c.mode}", end='\n')
    b.display()
    clearScreen()
    currentChar = sys.stdin.read(1)
    if currentChar == '\x03':  # Handle Ctrl+C to exit the loop gracefully
        break
    clearScreen()
    process_command(currentChar)
