print("options.py started")

import pygame
import sys
import subprocess

pygame.init()

info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Solar System - Options Menu")

bg = pygame.image.load("bg.webp")
bg = pygame.transform.scale(bg, (screen_width, screen_height))

WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200)

button_font = pygame.font.SysFont(None, 50)


def read_volume_from_file():
    try:
        with open("vol.txt", "r") as f:
            vol_str = f.read().strip()
            vol = float(vol_str)
            return max(0.0, min(1.0, vol))  # clamp between 0 and 1
    except:
        return 0.1

music_volume = read_volume_from_file()
slider_rect = pygame.Rect(screen_width // 2 - 150, 100, 300, 10)
knob_radius = 15
knob_x = slider_rect.x + int(music_volume * slider_rect.width)
dragging = False


# Define exit button rectangle (bottom right)
exit_button_width = 150
exit_button_height = 60
exit_button_margin = 20
exit_button_rect = pygame.Rect(
    screen_width - exit_button_width - exit_button_margin,
    screen_height - exit_button_height - exit_button_margin,
    exit_button_width,
    exit_button_height
)
def draw_slider():
    pygame.draw.rect(screen, WHITE, slider_rect)
    pygame.draw.circle(screen, LIGHT_GRAY, (knob_x, slider_rect.centery), knob_radius)
    label = button_font.render("MUSIC", True, WHITE)
    screen.blit(label, (screen_width // 2 - label.get_width() // 2, slider_rect.y - 50))

def draw_exit_button():
    mouse_pos = pygame.mouse.get_pos()
    if exit_button_rect.collidepoint(mouse_pos):
        color = LIGHT_GRAY  # Hover color
    else:
        color = DARK_GRAY  # Normal color
    pygame.draw.rect(screen, color, exit_button_rect, border_radius=10)
    text = button_font.render("EXIT", True, WHITE)
    text_rect = text.get_rect(center=exit_button_rect.center)
    screen.blit(text, text_rect)

def write_volume_to_file(volume):
    with open("vol.txt", "w") as f:
        f.write(f"{volume:.2f}")

def main():
    global knob_x, dragging, music_volume

    while True:
        screen.fill(BLACK)
        screen.blit(bg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    # Check if dragging knob
                    if pygame.Rect(knob_x - knob_radius, slider_rect.centery - knob_radius, knob_radius * 2, knob_radius * 2).collidepoint(mouse_pos):
                        dragging = True
                    # Check if exit button clicked
                    elif exit_button_rect.collidepoint(mouse_pos):
                        subprocess.Popen(['python3', 'menu.py'])
                        pygame.quit()
                        sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    knob_x = max(slider_rect.x, min(mouse_pos[0], slider_rect.x + slider_rect.width))
                    music_volume = (knob_x - slider_rect.x) / slider_rect.width
                    print(f"Volume: {music_volume:.2f}")

        draw_slider()
        draw_exit_button()
        write_volume_to_file(music_volume)

        pygame.display.flip()

if __name__ == "__main__":
    main()
