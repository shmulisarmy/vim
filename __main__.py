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
    if len(inp) == 1:
        #letter
        if input == ' ':
            wordTree.insert(c.get_current_word())
        b.write_char(inp)
        return
    if len(inp) == 2:
        if inp[0] == 'm':
            for command in vimMacros[inp[1]]:
                process_command(command)
            return
        if inp[0] == 'r':
            for letter in vimregisters[inp[1]]:
                b.write_char(letter)
            return

        #motion
        amount, command = inp
        #will go into temperary command mode when working off single input
        vimMotionMap[command](int(amount))
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
    'ggg': c.enterGrabMode,
    'bbb': b.backSpace,
    'ccc': b.commandEnter,
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




exit()
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
    b.display()
    clearScreen()
    currentChar = sys.stdin.read(1)
    print(f"{currentChar = }")
    if currentChar == '\x03':  # Handle Ctrl+C to exit the loop gracefully
        break
    clearScreen()
    process_command(currentChar)
