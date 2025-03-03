import pygame
import random
# import pygame_textinput
import pygame_gui
# Initialize Pygame
pygame.init()

# Create a clock object
clock = pygame.time.Clock()

# Initialize Pygame mixer
pygame.mixer.init()

# Load the sound effects
bullet_sound = pygame.mixer.Sound('./assets/laser.wav')
explosion_sound = pygame.mixer.Sound('./assets/explosion.wav')

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./assets/ufo.png')
pygame.display.set_icon(icon)

# Button colors
button_color = (250, 128, 114)
button_color_light = (170, 170, 170)
button_color_dark = (100, 100, 100)

# Create a UIManager object
manager = pygame_gui.UIManager((screen_width, screen_height))

# Create a UIConfirmationDialog object
confirmation_dialog = None

# Function to create a button
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(text_surf, text_rect)

# Function to create text objects
def text_objects(text, font):
    text_surface = font.render(text, True, (255, 255, 255))
    return text_surface, text_surface.get_rect()


# Player
player_img = pygame.image.load('./assets/player.png')
player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0

# Enemy
enemies = []
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 18 # Increase the number of enemies

# Initialize enemies in three rows
# for i in range(num_of_enemies):
#     enemy_img.append(pygame.image.load('enemy.png'))
#     enemy_x.append(50 * (i % 6))  # Change the x position
#     enemy_y.append(50 * (i // 6))  # Change the y position
#     enemy_x_change.append(4)
#     enemy_y_change.append(40)




enemies = []
for i in range(num_of_enemies):
    enemy = {
        'img': pygame.image.load('./assets/enemy.png'),
        'x': 50 * (i % 6),
        'y': 50 * (i // 6),
        'x_change': 4,
        'y_change': 40
    }
    enemies.append(enemy)

# Bullet
bullet_img = pygame.image.load('./assets/bullet.png')
bullet_x = 0
bullet_y = 480
bullet_y_change = 20
bullet_state = "ready"  # ready - can't see the bullet on the screen, fire - bullet is moving

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10


# Function to show score
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Function to draw the player
def player(x, y):
    screen.blit(player_img, (x, y))

# Function to draw the enemy
def draw_enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

# Function to fire bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))
    bullet_sound.play()

# Function to check for collision
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    if distance < 27:
        explosion_sound.play()
        return True
    return False

# print explosion graphics
# def explosion(x, y):
#     explosion_img = pygame.image.load('./assets/explosion.png')
#     screen.blit(explosion_img, (x, y))

# Lives
lives = 3
lives_font = pygame.font.Font('freesansbold.ttf', 32)

# Function to show lives
def show_lives(x, y):
    lives_render = lives_font.render("Lives : " + str(lives), True, (255, 255, 255))
    screen.blit(lives_render, (x, y))

# Function to check if player is hit
def is_player_hit(enemy_x, enemy_y, player_x, player_y):
    distance = ((enemy_x - player_x) ** 2 + (enemy_y - player_y) ** 2) ** 0.5
    if distance < 27:
        return True
    return False

# Create a TextInput object
# textinput = pygame_textinput.TextInput()

def game_intro():
    intro = True

    # Load the image
    # ufo_image = pygame.image.load('ufo.png')

    while intro:
        screen.fill((0, 0, 0))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # # Feed the events to the TextInput object
        # if textinput.update(events):
        #     print(textinput.get_text())

        # # Draw the TextInput object
        # screen.blit(textinput.get_surface(), (10, 10))

        # Draw the image on the screen
        # screen.blit(ufo_image, ((screen_width - ufo_image.get_width()) // 2, 50))

        large_text = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("Space Invaders", large_text)
        TextRect.center = ((screen_width / 2), (screen_height / 2))
        screen.blit(TextSurf, TextRect)

        button("Start Game", 150, 450, 150, 50, button_color, button_color_light, game_loop)
        button("Quit Game", 500, 450, 150, 50, button_color, button_color_light, quit_game)

        pygame.display.update()
        clock.tick(15)

# Function to quit the game
def quit_game():
    pygame.quit()
    quit()

# Function to start the game loop
def game_loop():
    print("Starting game loop")
    global player_x
    global player_y
    global player_x_change
    global player_y_change
    global bullet_x
    global bullet_y
    global bullet_state
    global score_value
    global lives
    global num_of_enemies
    global enemy_x
    global enemy_y
    global enemy_x_change
    global enemy_y_change
    global clock
    global running
    global confirmation_dialog
    
    # Game Loop
    running = True
    clock = pygame.time.Clock()  # Create a clock object
    while running:
        clock.tick(60)  # Limit the game to 60 FPS
        time_delta = clock.tick(60)/1000.0

        screen.fill((0, 0, 0))

        # Render Enemies
        for enemy in enemies:
            screen.blit(enemy['img'], (enemy['x'], enemy['y']))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Keyboard inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -5
                if event.key == pygame.K_RIGHT:
                    player_x_change = 5
                if event.key == pygame.K_UP:
                    player_y_change = -5
                if event.key == pygame.K_DOWN:
                    player_y_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_x = player_x
                        fire_bullet(bullet_x, bullet_y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_y_change = 0

            # Keyboard inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if confirmation_dialog is None:
                        print("Creating confirmation dialog")
                        confirmation_dialog = pygame_gui.windows.UIConfirmationDialog(
                            rect=pygame.Rect((250, 200), (300, 200)),
                            manager=manager,
                            window_title='Confirm Exit',
                            action_long_desc='Are you sure you want to quit?',
                            action_short_name='Yes',
                            blocking=True
                        )

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                    if event.ui_element == confirmation_dialog:
                        running = False
                        confirmation_dialog = None

            manager.process_events(event)

        manager.update(time_delta)

        manager.draw_ui(screen)

        pygame.display.update()

        player_x += player_x_change
        player_y += player_y_change

        # Boundary checking for player
        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736

        # Bullet movement
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change

        # Enemy movement
        for enemy in enemies:
            enemy['x'] += enemy['x_change']
            if enemy['x'] <= 0:
                enemy['x_change'] = 4
                enemy['y'] += enemy['y_change']
            elif enemy['x'] >= 736:
                enemy['x_change'] = -4
                enemy['y'] += enemy['y_change']

            # Collision
            for enemy in enemies:
                collision = is_collision(enemy['x'], enemy['y'], bullet_x, bullet_y)
                if collision:
                    bullet_y = 480
                    bullet_state = "ready"
                    score_value += 1
                    enemies.remove(enemy)

            # Collision with player
            for enemy in enemies:
                player_hit = is_player_hit(enemy['x'], enemy['y'], player_x, player_y)
                if player_hit:
                    enemy['x'] = random.randint(0, 735)
                    enemy['y'] = random.randint(50, 150)
                    lives -= 1
                    if lives == 0:
                        running = False

                    for i, enemy in enumerate(enemies):
                        draw_enemy(enemy['x'], enemy['y'], i)

        player(player_x, player_y)
        show_score(text_x, text_y)
        show_lives(650, 10)  # Display lives in the top right corner
        pygame.display.update()

# Call the game intro before starting the game loop
game_intro()
game_loop()