import pygame
from cpu import cpu


processor = cpu(32768, 24577)
processor.reset()

pixelSize = 2
width = 512 * pixelSize
height = 256 * pixelSize
white = (255, 255, 255)
black = (0, 0, 0)


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("HELLO BOOBIE!!!")


def render(cache):
    screen.fill((0, 0, 0))

    for rowIndex, row in enumerate(cache):
        for wordIndex, word in enumerate(row):
            for pixelIndex, pixel in enumerate(word):
                xPosition = (wordIndex * 16 + pixelIndex) * pixelSize
                yPosition = rowIndex * pixelSize
                color = white if pixel == '1' else black 
                pygame.draw.rect(screen, color, (xPosition, yPosition, pixelSize, pixelSize))

    pygame.display.flip()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    processor.cycle()
    
    render(processor.ram.cache)

pygame.quit()































