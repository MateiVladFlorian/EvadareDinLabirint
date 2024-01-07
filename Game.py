import pygame
from pygame.locals import *
from Core import *
from MapBuilder import *

# Jucatorul se poate misca prin intermediul comenzilor urmatoare de la tastatura:

"""
       ^
     <- ->
       v
"""

# noinspection SpellCheckingInspection,PyShadowingBuiltins
def setSprite(type: int, x: int, y: int, color: str, hdc):
    blockColor = pygame.Color(color)
    font = pygame.font.Font('freesansbold.ttf', 32)
    c = '#'

    if type == 2:
        c = 'M'
    elif type == 3:
        c = 'J'

    map = font.render(c, True, blockColor, pygame.Color('#000000'))

    textRect = map.get_rect()
    textRect.x, textRect.y = x, y

    textRect.center = (textRect.centerx, textRect.centery)

    if type != 0:
        hdc.blit(map, textRect)


# deseneaza pe ecran labirintul, jucatorul si monstrul
def GamePaint(hdc, px, py, ex, ey, m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == px and j == py:
                setSprite(3, i * 32 + 100, j * 32 + 100, '#28a745', screen)
            elif i == ex and j == ey:
                setSprite(2, i * 32 + 100, j * 32 + 100, '#dc3545', screen)
            elif m[i][j] == 1:
                setSprite(m[i][j], i * 32 + 100, j * 32 + 100, '#4682b4', screen)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Evadare din labirint")

    lastUpdate = 0
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode([500, 500])
    gameOver = False

    while not gameOver:
        # jocul este inchis fortat
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_UP:
                    launch.moveUp()
                elif event.key == K_DOWN:
                    launch.moveDown()
                elif event.key == K_LEFT:
                    launch.moveLeft()
                elif event.key == K_RIGHT:
                    launch.moveRight()

            elif event.type == pygame.QUIT:
                gameOver = True

        # seteaza culoarea pentru ecranul de joc
        screen.fill((0, 0, 0))
        px, py, ex, ey, m = launch.getGameState()
        GamePaint(screen, px, py, ex, ey, m)
        clock.tick(60)
        now = pygame.time.get_ticks()

        if now - lastUpdate > 400:
            launch.BestMove()
            lastUpdate = now

        if not launch.isRunning():
            break

        # actualizeaza ecranul jocului
        pygame.display.update()
        pygame.display.flip()

    # inchide fereastra de joc
    pygame.quit()
