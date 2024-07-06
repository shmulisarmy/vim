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
old_settings = termios.tcgetattr(fd)
tty.setraw(fd)
#for entering text



wordTree = SearchTree()

class board:
    def __init__(self) -> None:
        self.TextArea = [[' ' for _ in range(5)] for _ in range(5)]
        self.boardCopy: list[list]|None = None
        self.cursorList = []

    def display(self):
        cursor = self.cursorList[0]
        if cursor.mode == 'grab':
            self.boardCopy =  self.TextArea
            for i, j in cursor.selectedTextInReverse():
                print('i', i, 'j', j)
                self.TextArea[i][j] = blue(self.TextArea[i][j])

        else:
            self.TextArea[c.y][c.x] = blue(str(self.TextArea[c.y][c.x]) if self.TextArea[c.y][c.x] and self.TextArea[c.y][c.x] != ' ' else '…')

        for i, col in enumerate(self.TextArea):
            print(''.join(col))
            # for j, cell in enumerate(self.TextArea):

        if cursor.mode == 'grab':
            self.boardCopy: list[list]
            self.TextArea: list[list] =  self.boardCopy

    def write_char(self, char: str):
        cursor: 'Cursor' = self.cursorList[0]
        self.TextArea[cursor.y].insert(cursor.x, char)
        cursor.x+=1

    def commandEnter(self):
        cursor: 'Cursor' = self.cursorList[0]
        cursor.y += 1
        cursor.x = 0
        self.TextArea.insert(cursor.y, [' '])

    def backSpace(self):
        cursor: 'Cursor' = self.cursorList[0]
        if cursor.mode == 'grab':
            for i, j in cursor.selectedTextInReverse():
                print(f"{i = } {j = }")
                del self.TextArea[i][j]

            cursor.y = cursor.GrabStartPos_y
            cursor.x = min(cursor.GrabStartPos_x, cursor.x)-1
            if cursor.x < 0:
                cursor.y -= 1
                if cursor.y < 0:
                    cursor.y = len(self.TextArea)-1
                cursor.x = len(self.TextArea[cursor.y])-1
            cursor.mode = 'insert'
            return


        cursor.x -= 1
        del self.TextArea[cursor.y][cursor.x]
        if cursor.x < 0:

            cursor.y -= 1
            cursor.x = len(self.TextArea[cursor.y])-1



    def r(self, char):
        cursor: 'Cursor' = self.cursorList[0]
        if Cursor.mode: print()

    def deleteInside(self, charSet: tuple[str]):
        cursor = self.cursorList[0]
        while self.TextArea[cursor.y][cursor.x] != charSet[0]:
            del self.TextArea[cursor.y][cursor.x]
            cursor.x -= 1
            if cursor.x < 0:

                cursor.y -= 1
                cursor.x = len(self.TextArea[cursor.y])-1




class Cursor:
    """
        when in mode:
            grab  -> starting pos, current pos
    """
    modes = ['insert', 'command', 'insertNumber', 'one command', 'grab']
    mode = 'insert'
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
        self.GrabStartPos_x = x
        self.GrabStartPos_y = y
        self.mode = 'insert'
        self.board_on = None

    def enterGrabMode(self):
        self.mode = 'grab'
        self.GrabStartPos_y = self.y
        self.GrabStartPos_x = self.x

    def selectedTextInReverse(self):
        for i in range(max(self.y, self.GrabStartPos_y), min(self.y, self.GrabStartPos_y)-1, -1):
            for j in range(max(self.x, self.GrabStartPos_x), min(self.x, self.GrabStartPos_x)-1, -1):
                yield (i, j)


    """motions"""
    def j(self, times=1):
        self.y += times
    def k(self, times=1):
        self.y -= times
    def l(self, times=1):
        self.x += times
    def h(self, times=1):
        self.x -= times
    def w(self, times=1):
        words_left = times
        while words_left:
            self.x+=1
            if self.board_on[self.y][self.x] ==  ' ':
                words_left-=1
            self.x+=times
    def b(self, times=1):
        words_left = times
        while words_left:
            self.x-=1
            if self.board_on[self.y][self.x] ==  ' ':
                words_left-=1


    def __str__(self) -> str:
        return f"y - {self.y}, x - {self.x}"

    def get_current_word(self):
        tempX = self.x
        letters_in_reverse = []
        tempX-=1
        while self.board_on[self.y][tempX] != ' ':
            if tempX < 0:
                break
            letters_in_reverse.append(self.board_on[self.y][tempX])
            tempX-=1

        return letters_in_reverse[::-1]

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



b = board()
c = Cursor()
b.cursorList.append(c)
c.board_on = b.TextArea




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
    if currentChar == '\x03':  # Handle Ctrl+C to exit the loop gracefully
        break
    clearScreen()
    process_command(currentChar)
