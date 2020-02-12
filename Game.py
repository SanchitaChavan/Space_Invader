import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('si.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('sii.png')
playerX = 370
playerY = 480
playerX_change=0
playerY_change=0

# Enemy
EnemyImg = pygame.image.load('ali.png')
EnemyX = random.randint(0, 800)
EnemyY = random.randint(50, 150)
EnemyX_change = 0.3
EnemyY_change = 100

def player(x, y):
    screen.blit(playerImg, (x, y))
    # blit means draw
def Enemy(x, y):
    screen.blit(EnemyImg, (x, y))

# Game loop ie a window is displayed which closes when close button is pressed
running = True
while running:
    # RGB
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if key is pressed check right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    EnemyX += EnemyX_change

    if EnemyX <= 0:
        EnemyX_change = 0.3
        EnemyY += EnemyY_change
    elif EnemyX >= 736:
        EnemyX_change = -0.3
        EnemyY += EnemyY_change
    player(playerX, playerY)
    Enemy(EnemyX, EnemyY)

    pygame.display.update()
