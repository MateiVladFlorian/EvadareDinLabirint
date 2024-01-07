import socket
from EnemyAgent import *
from MapBuilder import *

# Deseneaza atat jucatorul cat si monstrul;
def GamePaint(ms: MapBuilder):
    m = ms.getMatrix()
    px, py = ms.getPlayerPos()
    ex, ey = ms.getEnemyPos()
    line = ""

    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == px and j == py:
                line += "J"
            elif i == ex and j == ey:
                line += "M"
            else:
                block = '#' if m[i][j] == 1 else ' '
                line += block

        print(line)
        line = ""

def server():
    server_ip = "127.0.0.1"
    port = 65438

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, port))

    server.listen(0)
    print("{", server_ip, ":", port, "}")

    client_socket, client_address = server.accept()
    cmds = ["START", "STOP", "U", "D" "L", "R"]

    ms = MapBuilder()
    en = EnemyAgent(ms)

    newGame = False
    moves = 0

    while True:
        request = client_socket.recv(104)
        request = request.decode("utf-8")

        if request.upper() == "START":
            ms = MapBuilder()
            en = EnemyAgent(ms)

            m = ms.getMatrix()
            px, py = ms.getPlayerPos()
            newGame = True
            GamePaint(ms)

        response = "acceptat" if request.upper() in cmds else "inexistent"

        if newGame:
            if request.upper() == "U":
                if px > 0 and m[px - 1][py] != 1:
                    px -= 1
                    moves += 1
                    response = "OK"
                else:
                    response = "Imposibil, ai lovit un perete. Încearcă altă directie."

            elif request.upper() == "D":
                if px < 9 and m[px + 1][py] != 1:
                    response = "OK"
                    moves += 1
                    px += 1
                else:
                    response = "Imposibil, ai lovit un perete. Încearcă altă directie."
            elif request.upper() == "L":
                if py > 0 and m[px][py - 1] != 1:
                    response = "OK"
                    moves += 1
                    py -= 1
                else:
                    response = "Imposibil, ai lovit un perete. Încearcă altă directie."
            elif request.upper() == "R":
                if py < 9 and m[px][py + 1] != 1:
                    response = "OK"
                    moves += 1
                    py += 1
                else:
                    response = "Imposibil, ai lovit un perete. Încearcă altă directie."

            print()

            ms.setPlayerPos(px, py)
            ex, ey = ms.getEnemyPos()

            if px == 0 or px == 9 or py == 0 or py == 9:
                response = f"Ai reușit! Ai ieșit din labirint în ... {moves} mișcări"
                newGame = False
            elif Util.Manhattan(px, py, ex, ey) < 3:
                response = "Ai picat pradă monstrului din labirint ☹... ai pierdut jocul. Încerca din nou!"
                newGame = False

            en.BestMove()
            GamePaint(ms)

        if request.upper() == "STOP":
            break

        client_socket.send(response.encode("utf-8"))

    client_socket.close()
    print("Connection to client closed")
    server.close()

server()
