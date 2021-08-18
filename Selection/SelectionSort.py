import pygame, random
from time import sleep
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Selection Sort")

WHITE = (255,255,255)

kk = 400
def display_plot(value):
    for i in range(0,kk):
        pygame.draw.line(screen, WHITE, (int(i*(800/kk)) , 600), (int(i*(800/kk)), 600 - value[i]), 3)

value = []
for i in range(0,kk):
    value.append(random.randint(0,600))



running = True
i = -1
while running:
    i = i+1
    if i==400:
        break
    sleep(0.02)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_plot(value)
    min_idx = i
    for j in range(i + 1, kk):
        if value[min_idx] > value[j]:
            min_idx = j
    value[i], value[min_idx] = value[min_idx], value[i]

    pygame.display.update()