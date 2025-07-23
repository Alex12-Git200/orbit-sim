import pygame
import subprocess
import sys

pygame.init()

info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Solar System - Main Menu")

bg = pygame.image.load("bg.webp")
bg = pygame.transform.scale(bg, (screen_width, screen_height))

# Colors
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Fonts
title_font = pygame.font.SysFont(None, 110)
button_font = pygame.font.SysFont(None, 50)

# Buttons
play_button = pygame.Rect(screen_width // 2 - 200, screen_height // 2 - 120, 400, 80)
options_button = pygame.Rect(screen_width // 2 - 200, screen_height // 2 - 10, 400, 80)
quit_button = pygame.Rect(screen_width // 2 - 200, screen_height // 2 + 100, 400, 80)


def draw_button(rect, text, hover):
    color = LIGHT_GRAY if hover else DARK_GRAY
    pygame.draw.rect(screen, color, rect, border_radius=10)
    txt_surf = button_font.render(text, True, WHITE)
    txt_rect = txt_surf.get_rect(center=rect.center)
    screen.blit(txt_surf, txt_rect)

def main_menu():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        play_hover = play_button.collidepoint(mouse_pos)
        options_hover = options_button.collidepoint(mouse_pos)
        quit_hover = quit_button.collidepoint(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if play_button.collidepoint(event.pos):
                        subprocess.Popen(['python3', 'game.py'])
                        pygame.quit()
                        sys.exit()
                    if options_button.collidepoint(event.pos):
                        subprocess.Popen(['python3', 'options.py'])
                        pygame.quit()
                        sys.exit()
                    if quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()



        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        # Draw title
        title_surf = title_font.render("Solar System", True, WHITE)
        title_rect = title_surf.get_rect(center=(screen_width // 2, 300))
        screen.blit(title_surf, title_rect)

        # Draw buttons
        draw_button(play_button, "PLAY", play_hover)
        draw_button(options_button, "OPTIONS", options_hover)
        draw_button(quit_button, "QUIT", quit_hover)

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
