import pygame
import random

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((800, 600))
window.fill((100,100,100))
pygame.display.set_caption("HALLO!")

player = pygame.surface.Surface((40, 40))
player.fill((25, 250, 60))
fruit = pygame.surface.Surface((40, 40))
fruit.fill((250,10,10))

fruitCollected = False

player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0
fruit_x = 120
fruit_y = 120

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if player_vel_x != 40:
                    player_vel_x = -40
                    player_vel_y = 0
            if event.key == pygame.K_RIGHT:
                if player_vel_x != -40:
                    player_vel_x = 40
                    player_vel_y = 0
            if event.key == pygame.K_UP:
                if player_vel_y != 40:
                    player_vel_y = -40
                    player_vel_x = 0
            if event.key == pygame.K_DOWN:
                if player_vel_y != -40:
                    player_vel_y = 40
                    player_vel_x = 0

        if player_x == fruit_x and player_y == fruit_y:
            fruitCollected = True

        if fruitCollected: 
            fruit_x = random.randint(0, 19) * 40
            fruit_y = random.randint(0, 14) * 40
            fruitCollected = False

    window.fill((100,25,100))
    player_x += player_vel_x
    player_y += player_vel_y
    window.blit(player, (player_x, player_y))
    window.blit(fruit, (fruit_x, fruit_y))
    print("Player: ", player_x, player_y)
    print("Fruit: ", fruit_x, fruit_y)
    print("Fruit Collected: ", fruitCollected)
    pygame.display.flip()
    clock.tick(5)

# run game =  py -3.12 main.py