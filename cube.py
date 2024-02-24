import pygame
import sys
import math

pygame.init()

screen_width = 600
screen_height = 600

black = (0,0,0)
white = (255,255,255)

fps = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

vertices = [[-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1]]

edges = [[0,1],
         [1,2],
         [2,3],
         [3,0],
         [4,5],
         [5,6],
         [6,7],
         [7,4],
         [0,4],
         [1,5],
         [2,6],
         [3,7],
         ]

def scale(list_, k):
    for i in range(len(list_)):
        for j in range(len(list_[0])):
            list_[i][j] *= k

def columnPos(list_):
    return [[list_[0]], [list_[1]], [list_[2]]]

def matrixMult(A, B): #doğru çalışıyor
    C = []
    for i in range(len(A)):
        rowList = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A[0])):
                sum += A[i][k]*B[k][j]
            rowList.append(sum)
        C.append(rowList)
    return C

def rotationX(angle):
    return [[1, 0, 0],
            [0, math.cos(math.radians(angle)), -math.sin(math.radians(angle))],
            [0, math.sin(math.radians(angle)), math.cos(math.radians(angle))]]

def rotationY(angle):
    return [[math.cos(math.radians(angle)), 0, math.sin(math.radians(angle))],
            [0, 1, 0],
            [-math.sin(math.radians(angle)), 0, math.cos(math.radians(angle))]]

scale(vertices, 100)

angleX = 0.0
angleY = 0.0
right, left, down, up = False, False, False, False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
    if(right):
        angleY -= 1
    if(left):
        angleY += 1
    if(up):
        angleX -= 1
    if(down):
        angleX += 1

    screen.fill(black)
    

    for start,end in edges:
        startPos = matrixMult(rotationY(angleY), matrixMult(rotationX(angleX), columnPos(vertices[start])))
        endPos = matrixMult(rotationY(angleY), matrixMult(rotationX(angleX), columnPos(vertices[end])))
        pygame.draw.line(screen, white, [startPos[0][0]+screen_width/2, startPos[1][0]+screen_height/2],
                                        [endPos[0][0]+screen_width/2, endPos[1][0]+screen_height/2])
        


    pygame.display.update()
    clock.tick(fps)
