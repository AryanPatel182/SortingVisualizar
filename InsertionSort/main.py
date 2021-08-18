import pygame, random
from time import sleep
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Insertion Sort")

WHITE = (255,255,255)

kk = 400
def display_plot(value):
    for i in range(0,kk):
        pygame.draw.line(screen, WHITE, (i*(800/kk) , 600), (i*(800/kk), 600 - value[i]), 3)


value = []
for i in range(0,kk):
    value.append(random.randint(0,600))



running = True
i = -1
while running:
    i = i+1
    sleep(0.01)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_plot(value)
    key = value[i]
    j = i - 1
    while j >= 0 and key < value[j]:
        value[j + 1] = value[j]
        j -= 1
    value[j + 1] = key

    pygame.display.update()