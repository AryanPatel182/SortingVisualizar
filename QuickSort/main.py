import pygame, random
from time import sleep
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Quick Sort")

WHITE = (255,255,255)

kk = 400
def display_plot(value):
    screen.fill((0, 0, 0))
    for i in range(0,kk):
        pygame.draw.line(screen, WHITE, (int(i*(800/kk)) , 600), (int(i*(800/kk)), 600 - value[i]), 3)
    pygame.display.update()


value = []
for i in range(0,kk):
    value.append(random.randint(0,600))


def partition(arr, low, high):
    sleep(0.01)
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        display_plot(arr)
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    display_plot(arr)
    return i + 1

def quickSort(arr, low, high):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if low < high:
        pi = partition(arr, low, high)
        display_plot(arr)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
        sleep(0.01)
        display_plot(arr)




running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    quickSort(value, 0, kk-1)
    display_plot(value)
    running = False



