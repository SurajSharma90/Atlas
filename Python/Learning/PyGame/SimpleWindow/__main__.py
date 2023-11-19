import pygame

pygame.init()

SCREEN_DIMENSIONS = {"x": 800, "y": 600}

display = pygame.display
screen = display.set_mode((SCREEN_DIMENSIONS["x"], SCREEN_DIMENSIONS["y"]))
display.set_caption("Simple Window")

rect = pygame.Rect((300, 250, 50, 50))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        rect.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        rect.move_ip(1, 0)
    if key[pygame.K_w] == True:
        rect.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        rect.move_ip(0, 1)

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), rect)

    display.update()

pygame.quit()
