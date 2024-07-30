import pygame
import sys
import random


pygame.init()
res = (720, 720)

c1 = random.randint(125, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)

screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
color_list = [red, green, blue]

# Colors for the buttons
light_pink = (255, 182, 193)
light_blue = (173, 216, 230)

startl = light_pink
optionsl = light_blue
exitl = (169, 169, 169)  

startd = (255, 105, 180) 
optionsd = (0, 191, 255)  
exitd = (100, 100, 100)  

white = (255, 255, 255)

width = screen.get_width()
height = screen.get_height()

# Initial player positions and other configurations
lead_x = 40
lead_y = height / 2
x = 300
y = 290
width1 = 100
height1 = 40

smallfont = pygame.font.SysFont('Corbel', 35)

text = smallfont.render('Start', True, white)
text1 = smallfont.render('Options', True, white)
exit1 = smallfont.render('Exit', True, white)

blox = smallfont.render('blox', True, (c3, c2, c1))

player_c = random.choice(color_list)
speed = 15
count = 0
enemy_size = 50
e_p = [width, random.randint(50, height - 50)]
e1_p = [random.randint(width, width + 100), random.randint(50, height - 100)]


# game over
def game_over():
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse1 = pygame.mouse.get_pos()
                if 100 < mouse1[0] < 140 and height - 100 < mouse1[1] < height - 80:
                    pygame.quit()
                    sys.exit()
                if width - 180 < mouse1[0] < width - 100 and height - 100 < mouse1[1] < height - 80:
                    game(lead_y, lead_x, speed, count)

        screen.fill((0, 0, 0))
        smallfont = pygame.font.SysFont('Corbel', 60)
        smallfont1 = pygame.font.SysFont('Corbel', 25)
        game_over_text = smallfont.render('GAME OVER', True, white)
        game_exit = smallfont1.render('Exit', True, white)
        restart = smallfont1.render('Restart', True, white)
        mouse1 = pygame.mouse.get_pos()

        if 100 < mouse1[0] < 140 and height - 100 < mouse1[1] < height - 80:
            pygame.draw.rect(screen, exitl, [100, height - 100, 40, 20])
        else:
            pygame.draw.rect(screen, exitd, [100, height - 100, 40, 20])

        if width - 180 < mouse1[0] < width - 100 and height - 100 < mouse1[1] < height - 80:
            pygame.draw.rect(screen, startl, [width - 180, height - 100, 80, 20])
        else:
            pygame.draw.rect(screen, startd, [width - 180, height - 100, 80, 20])

        screen.blit(game_exit, (100, height - 100))
        screen.blit(restart, (width - 180, height - 100))
        screen.blit(game_over_text, (width / 2 - 150, 295))

        pygame.display.update()


# Main game 
def game(lead_y, lead_x, speed, count):
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            lead_y -= 10
        if keys[pygame.K_DOWN]:
            lead_y += 10

        screen.fill((65, 25, 64))
        clock.tick(speed)

        rect = pygame.draw.rect(screen, player_c, [lead_x, lead_y, 40, 40])
        pygame.draw.rect(screen, (c1, c2, c3), [0, 0, width, 40])
        pygame.draw.rect(screen, (c3, c2, c1), [0, 680, width, 40])
        pygame.draw.rect(screen, startd, [width - 100, 0, 100, 40])
        exit2 = smallfont.render('Exit', True, white)

        mouse = pygame.mouse.get_pos()
        if width - 100 < mouse[0] < width and 0 < mouse[1] < 40:
            pygame.draw.rect(screen, startl, [width - 100, 0, 100, 40])
        else:
            pygame.draw.rect(screen, startd, [width - 100, 0, 100, 40])
        if width - 100 < mouse[0] < width and 0 < mouse[1] < 40:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        if e_p[0] > 0 and e_p[0] <= width:
            e_p[0] -= 10
        else:
            if e_p[1] <= 40 or e_p[1] >= height - 40:
                e_p[1] = height / 2
            e_p[1] = random.randint(enemy_size, height - enemy_size)
            e_p[0] = width

        if lead_x <= e_p[0] <= lead_x + 40 and lead_y >= e_p[1] >= lead_y - 40:
            game_over()
        if lead_y <= e_p[1] + enemy_size <= lead_y + 40 and lead_x <= e_p[0] <= lead_x + 40:
            game_over()

        pygame.draw.rect(screen, red, [e_p[0], e_p[1], enemy_size, enemy_size])

        if e1_p[0] > 0 and e1_p[0] <= width + 100:
            e1_p[0] -= 10
        else:
            if e1_p[1] <= 40 or e1_p[1] >= height - 40:
                e1_p[1] = height / 2
            e1_p[1] = random.randint(enemy_size, height - 40)
            e1_p[0] = width + 100

        if lead_x <= e1_p[0] <= lead_x + 40 and lead_y >= e1_p[1] >= lead_y - 40:
            e1_p[0] = width + 100
            e1_p[1] = random.randint(40, height - 40)
            count += 1
            speed += 1
        if lead_y <= e1_p[1] + enemy_size <= lead_y + 40 and lead_x <= e1_p[0] <= lead_x + 40:
            e1_p[0] = width + 100
            e1_p[1] = random.randint(40, height - 40)
            count += 1
            speed += 1
            if count >= 45:
                speed = 60

        if lead_y <= 38 or lead_y >= height - 38:
            game_over()
        if e1_p[0] <= 0:
            game_over()

        pygame.draw.rect(screen, blue, [e1_p[0], e1_p[1], enemy_size, enemy_size])
        score1 = smallfont.render('Score:', True, white)
        screen.blit(score1, (width - 120, height - 40))
        screen.blit(exit2, (width - 80, 0))
        pygame.display.o
# Intro function
def intro(colox_c1, colox_c2, colox, exit1, text1, text):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        mouse = pygame.mouse.get_pos()

        if x < mouse[0] < x + width1 and y < mouse[1] < y + height1:
            pygame.draw.rect(screen, startl, [x, y, width1, height1])
        else:
            pygame.draw.rect(screen, startd, [x, y, width1, height1])

        if x < mouse[0] < x + width1 and y + 70 < mouse[1] < y + 70 + height1:
            pygame.draw.rect(screen, optionsl, [x, y + 70, width1 + 40, height1])
        else:
            pygame.draw.rect(screen, optionsd, [x, y + 70, width1 + 40, height1])

        if x < mouse[0] < width1 + x and y + 140 < mouse[1] < y + 140 + height1:
            pygame.draw.rect(screen, exitl, [x, y + 140, width1, height1])
        else:
            pygame.draw.rect(screen, exitd, [x, y + 140, width1, height1])

        if event.type == pygame.MOUSEBUTTONDOWN:
            if x < mouse[0] < x + width1 and y < mouse[1] < y + height1:
                game(lead_y, lead_x, speed, count)
            elif x < mouse[0] < width1 + x and y + 140 < mouse[1] < y + 140 + height1:
                pygame.quit()
                sys.exit()

        screen.blit(text, (312, 295))
        screen.blit(text1, (312, 365))
        screen.blit(exit1, (312, 435))
        screen.blit(colox, (312, 50))

        clock.tick(60)
        pygame.display.update()

intro(0, 0, colox, exit1, text1, text)

