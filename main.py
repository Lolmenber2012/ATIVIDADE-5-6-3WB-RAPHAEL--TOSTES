import sys
from pygame import *

init()
screen = display.set_mode((1280, 720))
running = True

fonte = font.Font("GODOFWAR.ttf", 50)
image = image.load("Kratos.png")
image = transform.scale(image, (200, 200))
mixer.music.load("Homens queimem a vila.mp3")
mixer.music.play(-1)
#BP
while running:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    screen.fill("#97D1FA")
    draw.rect(screen, (0, 255, 0), (0, 680, 1280, 50))
    draw.rect(screen, (150, 75, 0), (630, 500, 600, 200))
    draw.circle(screen, "#FFF251", (80, 80), 50)
    draw.polygon(screen, "#F2883B", [(400, 300), (450, 300), (425, 250)])
    draw.line(screen, "#FFF251", (10, 150), (100, 20), 4)

    screen.blit(image, (500, 300))

    steve_text = fonte.render("HOMENS, QUEIMEM A VILA!", True, "#000000")
    screen.blit(steve_text, (500, 250))

    display.update()