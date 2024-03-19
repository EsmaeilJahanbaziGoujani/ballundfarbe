# 1
import pygame
# 8
import sys
# 33
import random

# 2 START PYGAME MODULES
pygame.init()

# ALL VARIABLES

# 3
display_width = 700
display_height = 700
# 5 VARIABLE FOR FIRST PAGE AND GAME LOOP
wating = True
# 23 VARIABLE FOR GAME PHASE
running = True

# 17
game_font = pygame.font.Font('assets/font/Merriweather-Light.ttf', 11)


# GAME DISPLAY
# 4
main_screen = pygame.display.set_mode((display_width, display_height))
# 10
clock = pygame.time.Clock()

# BACKGROUND IMAGES
# 12
start_image = pygame.transform.scale2x(
    pygame.image.load('assets/img/startbg1.jpg'))
# 25
game_image = pygame.transform.scale2x(
    pygame.image.load('assets/img/gamebg2.jpg'))

# INSTRUCTION PHASE
# 14
game_philisophy_text = ["DIE PHILOSOPHIE DES SPIELS:",
                        "OBWOHL ES VIELE MÖGLICHKEITEN GIBT, IM LEBEN ZU LEBEN,",
                        "SIND DIE MEISTENS DAVON SACKGASSEN.",
                        "DENKEN SIE ZUERST ÜBER ALLES NACH,",
                        "BEFOLGEN SIE ES DANN UND TUN SIE ES,",
                        "UND AKZEPTIEREN SIE NICHTS BLIND.",
                        "IHR ERFOLG IST WERTVOLL,",
                        "WENN SIE NIEMANDEM ODER IRGENDETWAS KÖRPERLICH",
                        "ODER GEISTIG GESCHADET HABEN,",
                        "ANSONSTEN IST ES ABSOLUT WERTLOS.",
                        "FOLGEN SIE IMMER DEN RICHTIGEN IDEEN,",
                        "DENN SIE MACHEN SIE GROß UND",
                        "FALSCHE IDEEN SIND WIE EINE SACKGASSEN,",
                        "DIE SIE VON ALLEM ABHÄLT!!!"]
# 15
game_instruction_text = ["SPIELANLEITUNG:",
                         "Das Spiel beginnt durch Drücken der S-Taste",
                         "Sie können nur Hindernisse derselben Farben überwinden",
                         "und sich nach links and rechts bewegen.",
                         "Wenn Sie alle fünf gleichfarbigen Hindernisse überwinden,",
                         "erhöht die Geschwendigkeit des Spiels.",
                         "Am Ende können Sie Ihre Punktzahl und Ihr Level sehen.",
                         "Wenn Sie nocheinmal spielen möchten,",
                         "drücken Sie bitte die R-Taste."]

# 16
start_button_text = "START"
# GENDER TEXTS
# 18 REWNDER PHILOSOPHY TEXT
text_y = 25
for line in game_philisophy_text:
    text_surface = game_font.render(line, True, (255, 255, 255))
    start_image.blit(text_surface, (15, text_y))
    text_y += text_surface.get_height() + 11
# 19 RENDER INSTRUCTION TEXT
text_y += 40
for line in game_instruction_text:
    text_surface = game_font.render(line, True, (255, 255, 255))
    start_image.blit(text_surface, (15, text_y))
    text_y += text_surface.get_height() + 15
# 20 RENDER START BUTTON TEXT
start_button_text_surface = game_font.render(
    start_button_text, True, (0, 255, 0))
start_button_rect = start_button_text_surface.get_rect(
    center=(display_width//2, display_height - 45))

# SONDS

# 21 START SOUND
start_sound = pygame.mixer.Sound('assets/sound/startgame_music.mp3')
# 28 GAME SOUND
game_sound = pygame.mixer.Sound('assets/sound/game_music.mp3')


# 32 COLORS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COLORS = [RED, GREEN, BLUE, YELLOW]

# 34 PLAYER SETTING
player_color = random.choice(COLORS)
player_radius = random.randint(10, 30)
player_x = display_width // 2
player_y = display_height - player_radius * 2
player_speed = 5
score = 0
level = 1

# 35 OBSTACLES SETTINGS
obstacle_color = random.choice(COLORS)
obstacle_width = random.randint(50, 150)
obstacle_height = random.randint(10, 30)
obstacle_x = random.randint(0, display_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 9

# FUNCTIONS
# 36 THE FUNCTIONS OF MAKING OBSTACLES RANDOMLY
# THIS FUNCTION IS CALLED TO DRAW THE OBSTACLE ON THE GAME SCREEN.
def draw_obstacle():
    global main_screen, player_color, player_x, player_y, player_radius, obstacle_color, obstacle_x, obstacle_y, obstacle_height, obstacle_width

    pygame.draw.circle(main_screen, player_color,
                       (player_x, player_y), player_radius)
    pygame.draw.rect(main_screen, obstacle_color, (obstacle_x,
                     obstacle_y, obstacle_width, obstacle_height))

# THIS FUNCTION IS CALLED WHEN THE OBSTACLE REACHES THE BOTTOM OF THE SCREEN, AND IT NEEDS TO BE RESPAWNED AT THE TOP.
def make_new_obstacle():
    global obstacle_color, obstacle_width, obstacle_height, obstacle_x, obstacle_y, display_width, COLORS
    
    obstacle_color = random.choice(COLORS)
    obstacle_width = random.randint(50, 150)
    obstacle_height = random.randint(10, 30)
    obstacle_x = random.randint(0, display_width - obstacle_width)
    obstacle_y = -obstacle_height
    draw_obstacle()


#  GAME LOOP
# 22 PLAY START SOUND WHEN I AM IN THE FIRST PAGE
start_sound.play(-1)
# 6
while wating:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 7 END PYGAME MODULES
            pygame.quit()
            # 9 TERMINATE PROGRAM
            sys.exit()
            # 31 IF PLAYER CLICK ON START BUTTON WITH MOUSE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_position):
                wating = False
                running = True
            # IF PLAYER CLICK ON START BUTTON (CLICK ON 'S') WITH KEYBOARD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                wating = False
                running = True


# 13 SHOW ME START_IMAGE ON DISPLAY
    main_screen.blit(start_image, (0, 0))
# 20 SHOW ME START_BUTTON_TEXT
    if start_button_text_surface:
        pygame.draw.rect(start_image, (0, 0, 255), start_button_rect)
        start_image.blit(start_button_text_surface, start_button_rect)


# 30 UPDATE THE GAME AND THE SPEED WHEN I CHANGE THE IMAGE FROM START IMAGE TO GAME IMAGE
    pygame.display.update()
    clock.tick(70)


# 27 STOP THE START SOUND WHENTHE GAME STARTS
start_sound.stop()


#  GAMEPLAY PHASE

# 29 PLAY THE GAME SOUND WHEN THE GAME STARTS
game_sound.play(-1)
# 24
while running:
    # 26
    main_screen.blit(game_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# 37 THIS LINE UPDATES THE VERTICAL POSITION (OBSTACLE_Y) OF THE OBSTACLE BY ADDING THE OBSTACLE'S SPEED (OBSTACLE_SPEED) TO IT.
    obstacle_y += obstacle_speed
    draw_obstacle()
# 38 THIS CONDITION CHECKS IF THE OBSTACLE HAS REACHED THE BUTTON OF THE SCREEN 
    if obstacle_y > display_height:
        obstacle_y = 0
        make_new_obstacle()


# 11 UPDATE THE GAME AND SET GAME SPEED
    pygame.display.update()
    clock.tick(70)
