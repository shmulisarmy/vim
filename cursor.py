from __init__ import *


class Cursor:
    """
        when in mode:
            grab  -> starting pos, current pos
    """
    modes = ['insert', 'command', 'insertNumber', 'one command', 'grab', 'delete']
    mode = 'insert'
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
        self.GrabStartPos_x = x
        self.GrabStartPos_y = y
        self.mode = 'insert'
        self.previos_mode = 'insert'
        self.board_on = None
        self.board = None
        self.motion_amount = 0

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

    def enterDeleteMode(self):
        if self.mode == 'delete':
            self.board.backSpace()
            return
        if self.mode == 'grab':
            self.board.backSpace()
            self.previos_mode = 'insert'
            return
        self.mode = 'delete'

    def set_mode(self, mode):
        self.previos_mode = self.mode
        self.mode = mode
