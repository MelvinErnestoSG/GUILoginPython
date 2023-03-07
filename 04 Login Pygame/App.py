import pygame
from pygame.locals import *

pygame.init()

# Colors.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Screen setup.
SCREEN_SIZE = (300, 300)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Login')

# Font.
font = pygame.font.Font(None, 25)

# Input boxes.
username_input = Rect(110, 75, 150, 25)
password_input = Rect(110, 125, 150, 25)

# Input Text.
username_text = ''
password_text = ''

# Variable to keep our game loop running
running = True

# Main loop.
while running:
    # Event handling.
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if username_input.collidepoint(pygame.mouse.get_pos()):
                if event.key == K_BACKSPACE:
                    username_text = username_text[:-1]
                else:
                    username_text += event.unicode
            elif password_input.collidepoint(pygame.mouse.get_pos()):
                if event.key == K_BACKSPACE:
                    password_text = password_text[:-1]
                else:
                    password_text += "*"
        elif event.type == MOUSEBUTTONDOWN:
            if username_input.collidepoint(event.pos):
                # The cursor is inside the username input box.
                pass
            elif password_input.collidepoint(event.pos):
                # The cursor is inside the password input box.
                pass
            else:
                # The cursor is outside the input boxes.
                pass
            if login_button.collidepoint(event.pos):
                # The user clicked on the login button.
                # Check if the username and password are valid.
                print("Username:", username_text)
                print("Password:", password_text)
                if (username_text == 'admin') and (password_text != '1234'):
                    print('Login successful!')
                else:
                    print('Invalid username or password')

    # Fill the background colour to the screen.
    screen.fill(BLACK)

    # Text
    username_label = font.render('Username:', True, WHITE)
    password_label = font.render('Password:', True, WHITE)
    screen.blit(username_label, (20, 80))
    screen.blit(password_label, (25, 130))

    # Input boxes.
    pygame.draw.rect(screen, GRAY, username_input, 2)
    pygame.draw.rect(screen, GRAY, password_input, 2)

    # Input text.
    username_surface = font.render(username_text, True, WHITE)
    password_surface = font.render(password_text, True, WHITE)
    screen.blit(username_surface, (username_input.x + 5, username_input.y + 5))
    screen.blit(password_surface, (password_input.x + 5, password_input.y + 5))

    # Login button.
    login_button = Rect(110, 170, 90, 40)
    pygame.draw.rect(screen, WHITE, login_button)
    login_label = font.render('Login', True, BLACK)
    screen.blit(login_label, (login_button.x + 20, login_button.y + 15))

    # Update screen.
    pygame.display.update()