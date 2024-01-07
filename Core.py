from EnemyAgent import *
from MapBuilder import *


class ClientLauncher:

    def __init__(self):
        """ Lansare sarcini de lucru """
        self.clientMap = MapBuilder()
        self.serverMap = MapBuilder(forceInit=False)

        self.serverMap.decodeMap(self.clientMap.getEncodedMap())
        self.agent = EnemyAgent(self.serverMap)

    def getGameState(self):
        px, py = self.clientMap.getPlayerPos()
        ex, ey = self.serverMap.getEnemyPos()
        return px, py, ex, ey, self.clientMap.getMatrix()

    def moveLeft(self):
        px, py = self.clientMap.getPlayerPos()
        m = self.clientMap.getMatrix()

        if px > 0 and m[px - 1][py] != 1:
            px -= 1
            self.clientMap.setPlayerPos(px, py)
            self.serverMap.setPlayerPos(px, py)

    def moveRight(self):
        px, py = self.clientMap.getPlayerPos()
        m = self.clientMap.getMatrix()

        if px < 9 and m[px + 1][py] != 1:
            px += 1
            self.clientMap.setPlayerPos(px, py)
            self.serverMap.setPlayerPos(px, py)

    def moveUp(self):
        px, py = self.clientMap.getPlayerPos()
        m = self.clientMap.getMatrix()

        if py > 0 and m[px][py - 1] != 1:
            py -= 1
            self.clientMap.setPlayerPos(px, py)
            self.serverMap.setPlayerPos(px, py)

    def moveDown(self):
        px, py = self.clientMap.getPlayerPos()
        m = self.clientMap.getMatrix()

        if py < 9 and m[px][py + 1] != 1:
            py += 1
            self.clientMap.setPlayerPos(px, py)
            self.serverMap.setPlayerPos(px, py)

    def isRunning(self):
        if self.IsPlayerDying():
            return False
        else:
            px, py = self.clientMap.getPlayerPos()

            if px == 0 or px == 9 or py == 0 or py == 9:
                return False

        return True

    def BestMove(self):
        self.agent.BestMove()

    def IsPlayerDying(self):
        return self.agent.IsPlayerDying()


launch = ClientLauncher()
