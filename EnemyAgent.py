from MapBuilder import *

class EnemyAgent:
    def __init__(self, map: MapBuilder):
        self.px, self.py = map.px, map.py
        self.ex, self.ey = map.ex, map.ey

        self.map = map
        self.m = map.getMatrix()

        self.lx = 0
        self.ly = 0

        self.index = 0
        self.moves = []
        self.minSize = 100

    def IsPlayerDying(self):
        return Util.Manhattan(self.map.px, self.map.py, self.ex, self.ey) <= 2

    def BestMove(self):
        """ jucatorul a schimbat pozitia, prin urmare recalculam drumul optim """
        if self.lx != self.map.px or self.ly != self.map.py:
            self.lx = self.map.px
            self.ly = self.map.py

            self.index = 0
            self.moves = []

            self.minSize = 100
            v = [0] * 100

            parent = [0] * 100
            daddy = 10 * self.ex + self.ey
            self.DFS(v, daddy, parent, 0)

            if self.index < len(self.moves) - 1:
                self.ex, self.ey = int(self.moves[self.index] / 10), int(self.moves[self.index] % 10)
                self.map.ex, self.map.ey = self.ex, self.ey
        else:
            """ trece la urmatoarea mutare """
            if self.index < len(self.moves) - 1:
                self.index += 1
                self.ex, self.ey = int(self.moves[self.index] / 10), int(self.moves[self.index] % 10)
                self.map.ex, self.map.ey = self.ex, self.ey
            else:
                self.index = 0
                self.moves = []
                self.minSize = 100
                v = [0] * 100

                parent = [0] * 100
                daddy = 10 * self.ex + self.ey
                self.DFS(v, daddy, parent, 0)

    def DFS(self, v, node, p, i):
        nx, ny = int(node / 10), int(node % 10)
        v[node] = 1

        """ Se verifica distanta Manhattan dintre jucatori; """
        if Util.Manhattan(self.map.px, self.map.py, nx, ny) <= 2:
            stack = []
            last = node

            while p[last] != 0:
                stack.append(last)
                last = p[last]

            stack.reverse()
            if self.minSize > len(stack):
                self.index = 0
                self.moves = []
                self.minSize = len(stack)

                for k in range(len(stack)):
                    self.moves.append(stack[k])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(len(dx)):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if 0 <= cx <= 9 and 0 <= cy <= 9 and self.m[cx][cy] == 0:
                child = 10 * cx + cy

                if v[child] == 0:
                    p[child] = node

                    if i < len(p) - 1:
                        self.DFS(v, child, p, i + 1)
