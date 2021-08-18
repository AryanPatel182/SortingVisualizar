import pygame, random
from time import sleep
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Merge Sort")

WHITE = (255,255,255)

kk = 400


def merge(arr, l, m, r):
    sleep(0.01)
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1



# l is for left index and r is right index of the
# sub-array of arr to be sorted

def mergeSort(arr, l, r):
    display_plot(value)
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        display_plot(arr)
        pygame.display.update()
        mergeSort(arr, m + 1, r)
        display_plot(arr)
        pygame.display.update()
        merge(arr, l, m, r)

    pygame.display.update()



def display_plot(value):
    screen.fill((0, 0, 0))
    for i in range(0,kk):
        pygame.draw.line(screen, WHITE, (int(i*(800/kk)) , 600), (int(i*(800/kk)), 600 - value[i]), 3)


value = []
for i in range(0,kk):
    value.append(random.randint(0,600))



running = True
i = 0
while running:
    i = i+1
    sleep(1)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_plot(value)
    mergeSort(value, 0, kk-1)
    display_plot(value)
    pygame.display.update()
    running = False


