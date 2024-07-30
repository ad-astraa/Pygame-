import pygame
import sys
import random

# Initialize the constructor
pygame.init()
res = (720, 720)

# Randomly assigns a value to variables ranging from lower limit to upper
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

# Light and dark shades for menu buttons
startl = light_pink
optionsl = light_blue
exitl = (169, 169, 169)  # Light gray for the Exit button

startd = (255, 105, 180)  # Hot pink for dark shade
optionsd = (0, 191, 255)  # Deep sky blue for dark shade
exitd = (100, 100, 100)  # Dark gray for the Exit button

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

# Defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# Texts to be rendered on screen
text = smallfont.render('Start', True, white)
text1 = smallfont.render('Options', True, white)
exit1 = smallfont.render('Exit', True, white)

# Game title
colox = smallfont.render('Colox', True, (c3, c2, c1))

# Game variables
player_c = random.choice(color_list)
speed = 15
count = 0
enemy_size = 50
e_p = [width, random.randint(50, height - 50)]
e1_p = [random.randint(width, width + 100), random.randint(50, height - 100)]


# Function for game over
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


# Main game function
def game(lead_y, lead_x, speed, count):
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
