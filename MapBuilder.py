from typing import List
from Util import Util
import random as rand


# noinspection PyAttributeOutsideInit
class MapBuilder:
    def __init__(self, forceInit=True):
        self.m = []

        if forceInit:
            self.encodeMap()

    def setEnemyPos(self, ex, ey):
        self.ex = ex
        self.ey = ey
        # inamicul isi va reseta pozitia;

    def setPlayerPos(self, px, py):
        self.px = px
        self.py = py
        # jucatorul isi va reseta positia in interactiune cu inamicul;

    def getEncodedMap(self):
        return self.buf
        # codificarea hartii

    def getMatrix(self):
        return self.m
        # matricea care contine harta codificata

    def getPlayerPos(self):
        return self.px, self.py

    def getEnemyPos(self):
        return self.ex, self.ey

    def encodeMap(self):
        self.m = Util.ChooseMap()
        self.px, self.py = rand.randint(1, 8), rand.randint(1, 8)
        self.ex, self.ey = 0, 0

        self.ii, self.jj, self.x = [0 for _ in range(4)], [0 for _ in range(4)], 0

        for _ in range(10):
            if self.m[0][_] == 0:
                self.ii.append(0)
                self.jj.append(_)

            if self.m[9][_] == 0:
                self.ii.append(9)
                self.jj.append(_)

            if self.m[_][0] == 0:
                self.ii.append(_)
                self.jj.append(0)

            if self.m[_][9] == 0:
                self.ii.append(_)
                self.jj.append(9)

        # Cauta o pozitie pentru jucator, astfel incat sa nu se afle pe o pozitie-zid si sa nu fie
        # pozitionat random langa iesirile din libirint;
        while self.m[self.px][self.py] != 0:
            self.px, self.py = rand.randint(1, 8), rand.randint(1, 8)

            if Util.Manhattan(self.px, self.py, self.jj[self.x], self.ii[self.x]) >= 3 and self.x < 4:
                self.px, self.py = rand.randint(1, 8), rand.randint(1, 8)
                self.x += 1

            if self.x == 3:
                break

        # cauta o pozitie libera pentru monstru, aflat la distanta minima fata de jucator
        while True:
            self.ex, self.ey = rand.randint(1, 8), rand.randint(1, 8)

            if Util.Manhattan(self.px, self.py, self.ex, self.ey) > 2 and self.m[self.ex][self.ey] == 0:
                break

        # pentru codificarea pozitiilor este suficient sa folosim 1 octet
        # pentru fiecare conversie in caractere a hartii se folosesc cate 2 biti
        buf = [chr(self.px), chr(self.py), chr(self.ex), chr(self.ey)]

        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                buf.append(chr(self.m[i][j]))

        self.buf = ""

        for i in range(len(buf)):
            self.buf += buf[i]

    def decodeMap(self, buffer):
        self.px, self.py = ord(buffer[0]), ord(buffer[1])
        self.ex, self.ey = ord(buffer[2]), ord(buffer[3])

        self.m = []

        for i in range(10):
            v = []

            for j in range(10):
                v.append(ord(buffer[10 * i + j + 4]))

            self.m.append(v)

m = MapBuilder()
m.encodeMap()
