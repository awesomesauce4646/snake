import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((0,0,0))
pygame.display.set_caption("HALLO!")

player = pygame.surface.Surface((50, 50))
player.fill((255, 60, 60))

player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)

    window.fill((0,0,0))

    window.blit(player, (player_x, player_y))

    pygame.display.flip()


# run game =  py -3.12 main.py