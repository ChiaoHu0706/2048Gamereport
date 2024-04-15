import pygame

# Initialize Pygame
pygame.init()

# Set the size of the window
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Eight Queens")

# Set the background color
background_color = (255, 255, 255)

# Create the chessboard
square_size = 50
chessboard = [[0 for x in range(8)] for y in range(8)]
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            color = (240, 217, 181)
        else:
            color = (181, 136, 99)
        pygame.draw.rect(screen, color, (i*square_size, j *
                         square_size, square_size, square_size))
