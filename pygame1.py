import pygame

pygame.init()

### Setting the surface
gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption('Game')

### pygame.display.flip() is the same
pygame.display.update()

gameExit = False
### uninitialized pygame
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

pygame.quit()
quit()
