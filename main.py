import pygame
import sys

# Define constants
WIDTH = HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION
FPS = 60

# Initialize pygame
pygame.init()

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Clock for controlling FPS
clock = pygame.time.Clock()

# Load images for chess pieces and resize them
piece_images = {
    'bR': pygame.transform.scale(pygame.image.load('images/bR.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'bN': pygame.transform.scale(pygame.image.load('images/bN.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'bB': pygame.transform.scale(pygame.image.load('images/bB.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'bQ': pygame.transform.scale(pygame.image.load('images/bQ.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'bK': pygame.transform.scale(pygame.image.load('images/bK.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'bP': pygame.transform.scale(pygame.image.load('images/bP.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'wR': pygame.transform.scale(pygame.image.load('images/wR.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'wN': pygame.transform.scale(pygame.image.load('images/wN.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'wB': pygame.transform.scale(pygame.image.load('images/wB.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'wQ': pygame.transform.scale(pygame.image.load('images/wQ.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'wK': pygame.transform.scale(pygame.image.load('images/wK.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'wP': pygame.transform.scale(pygame.image.load('images/wP.png'), (SQUARE_SIZE, SQUARE_SIZE))
}

# Initialize the board
starting_board = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
]

# Function to draw the chess board with pieces
def draw_board(board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = (217, 217, 217) if (row + col) % 2 == 0 else (153, 204, 255)
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[row][col]
            if piece != "":
                screen.blit(piece_images[piece], pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Main game loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        draw_board(starting_board)
        pygame.display.flip()
        clock.tick(FPS)

# Entry point of the program
if __name__ == "__main__":
    main()
