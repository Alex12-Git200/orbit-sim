import pygame
import math
import subprocess
import sys

pygame.init()


# game variables

info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("Solar System")
debug_shown = False
running = True
font = pygame.font.SysFont("Sans-serif", 80)
button_font = pygame.font.SysFont("Sans-serif", 50)
paused_text = font.render("Paused", True, (255, 255, 255))
speed = 1
bg = pygame.image.load("bg.webp").convert()
bg = pygame.transform.scale(bg, (screen_width, screen_height))
button_rect = pygame.Rect(screen_width - 130 - 20, screen_height - 65 - 0, 120, 50)


# Colors

WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)


# Sun 

sun_color = (255, 204, 51) 
sun_radius = int(min(screen_width, screen_height) * 0.05)
sun_pos = (screen_width // 2, screen_height // 2)  

# Mercury (mer for short)

mer_color = (180, 164, 150)
mer_radius = int(min(screen_width, screen_height) * 0.0043)
mer_orbit_radius = int(min(screen_width, screen_height) * 0.1)
mer_angle = 0


# Venus

venus_color = (230, 220, 170)
venus_radius = int(min(screen_width, screen_height) * 0.0075)
venus_orbit_radius = int(min(screen_width, screen_height) * 0.15)
venus_angle = 0

# earth and moon

earth_color = (0, 0, 255)
earth_radius = int(min(screen_width, screen_height) * 0.009)
earth_orbit_radius = int(min(screen_width, screen_height) * 0.2)
earth_angle = 0

moon_color = (255, 255, 255)
moon_radius = int(min(screen_width, screen_height) * 0.0025)
moon_orbit_radius = int(min(screen_width, screen_height) * 0.025)
moon_angle = 0



# Mars

mars_color = (255, 0, 0)
mars_radius = int(min(screen_width, screen_height) * 0.006)
mars_orbit_radius = int(min(screen_width, screen_height) * 0.25)
mars_angle = 0

# Jupiter

jupiter_color = (216,202,157)
jupiter_radius = int(min(screen_width, screen_height) * 0.02)
jupiter_orbit_radius = int(min(screen_width, screen_height) * 0.3)
jupiter_angle = 0

# Saturn

saturn_color = (255, 165, 0)
saturn_radius = int(min(screen_width, screen_height) * 0.017)
saturn_orbit_radius = int(min(screen_width, screen_height) * 0.35)
saturn_angle = 0

# Uranus

ur_color = (0, 255, 255)
ur_radius = int(min(screen_width, screen_height) * 0.01)
ur_orbit_radius = int(min(screen_width, screen_height) * 0.4)
ur_angle = 0

# Neptune 

ne_color = (0, 0, 255)
ne_radius = int(min(screen_width, screen_height) * 0.01)
ne_orbit_radius = int(min(screen_width, screen_height) * 0.45)
ne_angle = 0


def draw_button(text):
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        color = LIGHT_GRAY
    else:
        color = DARK_GRAY

    pygame.draw.rect(screen, color, button_rect, border_radius = 10)
    
    text = button_font.render(text, True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

def pause():
    while True: 
        global debug_shown
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return
                if event.key == pygame.K_h:
                    if not debug_shown:
                        debug_shown = True
                    else:
                        debug_shown = False

        # Draw time
        screen.fill("black")
        screen.blit(bg, (0, 0))

        if debug_shown:
            pygame.draw.circle(screen, (50, 50, 50), sun_pos, mer_orbit_radius, 1)
            pygame.draw.circle(screen, (50, 50, 50), sun_pos, venus_orbit_radius, 1)
            pygame.draw.circle(screen, (50, 50, 50), sun_pos, earth_orbit_radius, 1)
            pygame.draw.circle(screen, (50, 50, 50), sun_pos, mars_orbit_radius, 1)
            pygame.draw.circle(screen, (80, 80, 80), (int(earth_x), int(earth_y)), moon_orbit_radius, 1)
            pygame.draw.circle(screen, (50, 50, 50), sun_pos, jupiter_orbit_radius, 1)
            pygame.draw.circle(screen, (50, 50, 50), sun_pos, saturn_orbit_radius, 1)
            pygame.draw.circle(screen, (50, 50, 50), sun_pos, ur_orbit_radius, 1)
            pygame.draw.circle(screen, (50, 50, 50), sun_pos, ne_orbit_radius, 1)

        pygame.draw.circle(screen, sun_color, sun_pos, sun_radius)
        pygame.draw.circle(screen, mer_color, (int(mer_x), int(mer_y)), mer_radius)
        pygame.draw.circle(screen, venus_color, (int(venus_x), int(venus_y)), venus_radius)
        pygame.draw.circle(screen, earth_color, (int(earth_x), int(earth_y)), earth_radius)
        pygame.draw.circle(screen, moon_color, (int(moon_x), int(moon_y)), moon_radius)
        pygame.draw.circle(screen, mars_color, (int(mars_x), int(mars_y)), mars_radius)
        pygame.draw.circle(screen, mars_color, (int(mars_x), int(mars_y)), mars_radius)
        pygame.draw.circle(screen, jupiter_color, (int(jupiter_x), int(jupiter_y)), jupiter_radius)
        pygame.draw.circle(screen, saturn_color, (int(saturn_x), int(saturn_y)), saturn_radius)
        pygame.draw.circle(screen, ur_color, (int(ur_x), int(ur_y)), ur_radius)
        pygame.draw.circle(screen, ne_color, (int(ne_x), int(ne_y)), ne_radius)
        speed_text = font.render(f"Speed: {int(display_speed)}", True, (255, 255, 255))
        screen.blit(paused_text, (50, 50))
        screen.blit(speed_text, (50, 1000))
        
        draw_button("Exit")

        pygame.display.flip()
        clock.tick(60)
            
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                if screen.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode((screen_width, screen_height)) 
                else:
                    pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN) 
            if event.key == pygame.K_h:
                if not debug_shown:
                    debug_shown = True
                else:
                    debug_shown = False
            if event.key == pygame.K_p:
                pause()
            if event.key == pygame.K_r:
                speed = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                if event.button == 1:
                    subprocess.Popen(['python3', 'menu.py'])
                    sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        speed += 0.1
    if keys[pygame.K_DOWN]:
        speed -= 0.1


    if speed < 0.02:
        speed = 0.02
    elif speed > 100:
        speed = 100

    display_speed = speed * 5



    if display_speed < 1:
        display_speed = 1

    # mercury orbit
    mer_angle += 0.02 * speed
    mer_x = sun_pos[0] + mer_orbit_radius * math.cos(mer_angle)
    mer_y = sun_pos[1] + mer_orbit_radius * math.sin(mer_angle)

    # venus orbit
    venus_angle += 0.01 * speed
    venus_x = sun_pos[0] + venus_orbit_radius * math.cos(venus_angle)
    venus_y = sun_pos[1] + venus_orbit_radius * math.sin(venus_angle)
    
    # earth and moon orbit

    earth_angle += 0.0068 * speed
    earth_x = sun_pos[0] + earth_orbit_radius * math.cos(earth_angle)
    earth_y = sun_pos[1] + earth_orbit_radius * math.sin(earth_angle)

    moon_angle += 0.03 * speed
    moon_x = earth_x + moon_orbit_radius * math.cos(moon_angle)
    moon_y = earth_y + moon_orbit_radius * math.sin(moon_angle)


    # Mars orbit

    mars_angle += 0.0043 * speed
    mars_x = sun_pos[0] + mars_orbit_radius * math.cos(mars_angle)
    mars_y = sun_pos[1] + mars_orbit_radius * math.sin(mars_angle)

    # Jupiter orbit

    jupiter_angle += 0.003 * speed
    jupiter_x = sun_pos[0] + jupiter_orbit_radius * math.cos(jupiter_angle)
    jupiter_y = sun_pos[1] + jupiter_orbit_radius * math.sin(jupiter_angle)


    # Saturn Orbit

    saturn_angle += 0.002 * speed
    saturn_x = sun_pos[0] + saturn_orbit_radius * math.cos(saturn_angle)
    saturn_y = sun_pos[1] + saturn_orbit_radius * math.sin(saturn_angle)

    # Uranus Orbit

    ur_angle += 0.001 * speed
    ur_x = sun_pos[0] + ur_orbit_radius * math.cos(ur_angle)
    ur_y = sun_pos[1] + ur_orbit_radius * math.sin(ur_angle)

    # Neptune orbit

    ne_angle += 0.0006  * speed
    ne_x = sun_pos[0] + ne_orbit_radius * math.cos(ne_angle)
    ne_y = sun_pos[1] + ne_orbit_radius * math.sin(ne_angle)


    # Draw time
    screen.fill("black")
    screen.blit(bg, (0, 0))

    if debug_shown:
        pygame.draw.circle(screen, (50, 50, 50), sun_pos, mer_orbit_radius, 1)
        pygame.draw.circle(screen, (50, 50, 50), sun_pos, venus_orbit_radius, 1)
        pygame.draw.circle(screen, (50, 50, 50), sun_pos, earth_orbit_radius, 1)
        pygame.draw.circle(screen, (50, 50, 50), sun_pos, mars_orbit_radius, 1)
        pygame.draw.circle(screen, (80, 80, 80), (int(earth_x), int(earth_y)), moon_orbit_radius, 1)
        pygame.draw.circle(screen, (50, 50, 50), sun_pos, jupiter_orbit_radius, 1)
        pygame.draw.circle(screen, (50, 50, 50), sun_pos, saturn_orbit_radius, 1)
        pygame.draw.circle(screen, (50, 50, 50), sun_pos, ur_orbit_radius, 1)
        pygame.draw.circle(screen, (50, 50, 50), sun_pos, ne_orbit_radius, 1)

    pygame.draw.circle(screen, sun_color, sun_pos, sun_radius)
    pygame.draw.circle(screen, mer_color, (int(mer_x), int(mer_y)), mer_radius)
    pygame.draw.circle(screen, venus_color, (int(venus_x), int(venus_y)), venus_radius)
    pygame.draw.circle(screen, earth_color, (int(earth_x), int(earth_y)), earth_radius)
    pygame.draw.circle(screen, moon_color, (int(moon_x), int(moon_y)), moon_radius)
    pygame.draw.circle(screen, mars_color, (int(mars_x), int(mars_y)), mars_radius)
    pygame.draw.circle(screen, jupiter_color, (int(jupiter_x), int(jupiter_y)), jupiter_radius)
    pygame.draw.circle(screen, saturn_color, (int(saturn_x), int(saturn_y)), saturn_radius)
    pygame.draw.circle(screen, ur_color, (int(ur_x), int(ur_y)), ur_radius)
    pygame.draw.circle(screen, ne_color, (int(ne_x), int(ne_y)), ne_radius)
    speed_text = font.render(f"Speed: {int(display_speed)}", True, (255, 255, 255))

    screen.blit(speed_text, (50, 1000))
    
    print(f"S: {speed} | DS: {display_speed}")

    draw_button("Exit")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

