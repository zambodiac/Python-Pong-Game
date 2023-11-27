import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
#keys = pygame.key.get_pressed()
font = pygame.font.Font(None,350)

text_surface1 = font.render("0",False,"White")
text_surface2 = font.render('0',False,"White")
back_surface = pygame.image.load('graphics/screen.png').convert()
player_surface = pygame.image.load('graphics/paddle.png').convert_alpha()

player_rect1 = player_surface.get_rect(midleft = (50 ,540))
player_rect2 = player_surface.get_rect(midright = (1870 ,540))

move_w = False
move_s = False
move_up = False
move_down = False
while True:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_w = True
            elif event.key == pygame.K_s:
                move_s = True
            elif event.key == pygame.K_UP:
                move_up = True
            elif event.key == pygame.K_DOWN:
                move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_w = False
            elif event.key == pygame.K_s:
                move_s = False
            elif event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
    if move_w == True:
        player_rect1.y -= 10
        if player_rect1.y <= 0:
            player_rect1.y = 0
    if move_s == True:
        player_rect1.y += 10
        if player_rect1.y >= 835:
            player_rect1.y = 835
    if move_up == True:
        player_rect2.y -= 10
        if player_rect2.y <= 0:
             player_rect2.y = 0
    if move_down == True:
        player_rect2.y += 10
        if player_rect2.y >= 835:
            player_rect2.y = 835
        
        
        

    screen.blit(back_surface, (0,0))
    screen.blit(text_surface1, (400, 50))
    screen.blit(text_surface2, (1320,50))
    screen.blit(player_surface, player_rect1)
    screen.blit(player_surface, player_rect2) 
    
    pygame.display.update()
    clock.tick(60)
