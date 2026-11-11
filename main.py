import pygame

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((800, 600))
window.fill((100,100,100))
pygame.display.set_caption("HALLO!")

player = pygame.surface.Surface((40, 40))
player.fill((25, 250, 60))

player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

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


    window.fill((100,25,100))
    player_x += player_vel_x
    player_y += player_vel_y
    window.blit(player, (player_x, player_y))

    pygame.display.flip()
    clock.tick(5)

# run game =  py -3.12 main.py