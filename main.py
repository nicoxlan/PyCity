import pygame

pygame.init()

displayWidth = 800
displayHeight = 600

# Window
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("PyCity")
icon = pygame.image.load("PyCity.png")
pygame.display.set_icon(icon)
# Game Clock
clock = pygame.time.Clock()

# Game Loop
quitCommand = False
while not quitCommand:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitCommand = True
    pygame.display.update()

    clock.tick(60)

    gameDisplay.fill((40, 116, 166))

pygame.quit()
quit()
