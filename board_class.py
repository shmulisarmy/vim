from __init__ import *

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
