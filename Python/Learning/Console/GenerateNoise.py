import random
import pygame

# Generate noise map
NOISE_MAP_SIZE = {"x": 100, "y": 100}
noise = []


for i in range(0, NOISE_MAP_SIZE["x"]):
    noise.append([])
    for k in range(0, NOISE_MAP_SIZE["y"]):
        noise[i].append(random.random())


# Init pygame and window
pygame.init()

SCREEN_DIMENSIONS = {"x": 800, "y": 600}

display = pygame.display
screen = display.set_mode((SCREEN_DIMENSIONS["x"], SCREEN_DIMENSIONS["y"]))
display.set_caption("Simple Window")

# Init rect
rectSize = 5
rect = pygame.Rect((0, 0, rectSize, rectSize))

# Run game
run = True

while run:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE] == True:
        run = False
        break

    # Render loop
    screen.fill((0, 0, 0))

    # Visualize noise map
    for i in range(0, NOISE_MAP_SIZE["x"]):
        for k in range(0, NOISE_MAP_SIZE["y"]):
            rect.update(rect.x, rect.y, rectSize, rectSize)
            random.seed(noise[i][k])
            pygame.draw.rect(screen, (random.random() * 255, random.random() * 255, random.random() * 255), rect)
            rect.update(i * rectSize, k * rectSize, rectSize, rectSize)

    # End render loop
    display.update()

"""
    print("Input: X")
    x = int(input())
    print("Input: Y")
    y = int(input())
    random.seed(noise[x][y])
    print("Seed chosen: " + str(noise[x][y]))
    print("Random Value: " + str(random.random()))

    if x == "exit()" or y == "exit()":
        break
"""

# Exit application
pygame.quit()
