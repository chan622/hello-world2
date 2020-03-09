import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

### Setting the surface
gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption('Game')

### pygame.display.flip() is the same


gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [200,200,20,80])
    pygame.draw.rect(gameDisplay, red, [200,200,20,20])

    gameDisplay.fill(red, rect=[300,300,10,20])

    pygame.display.update()

pygame.quit()
quit()
