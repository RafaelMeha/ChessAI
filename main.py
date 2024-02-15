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


# Function to get legal moves for a pawn
# Function to get legal moves for a pawn
def get_pawn_moves(board, row, col):
    moves = []
    if board[row][col][0] == 'w':  # White pawn
        if row > 0 and board[row - 1][col] == "":
            moves.append((row - 1, col))
            if row == 6 and board[row - 2][col] == "":
                moves.append((row - 2, col))
        if row > 0 and col > 0 and board[row - 1][col - 1] and board[row - 1][col - 1][0] == 'b':
            moves.append((row - 1, col - 1))
        if row > 0 and col < 7 and board[row - 1][col + 1] and board[row - 1][col + 1][0] == 'b':
            moves.append((row - 1, col + 1))
    else:  # Black pawn
        if row < 7 and board[row + 1][col] == "":
            moves.append((row + 1, col))
            if row == 1 and board[row + 2][col] == "":
                moves.append((row + 2, col))
        if row < 7 and col > 0 and board[row + 1][col - 1] and board[row + 1][col - 1][0] == 'w':
            moves.append((row + 1, col - 1))
        if row < 7 and col < 7 and board[row + 1][col + 1] and board[row + 1][col + 1][0] == 'w':
            moves.append((row + 1, col + 1))
    return moves


# Function to get legal moves for a knight
def get_knight_moves(board, row, col):
    moves = []
    directions = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] == "" or board[r][c][0] != board[row][col][0]):
            moves.append((r, c))
    return moves

# Function to get legal moves for a bishop
def get_bishop_moves(board, row, col):
    moves = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < 8 and 0 <= c < 8:
            if board[r][c] == "":
                moves.append((r, c))
            elif board[r][c][0] != board[row][col][0]:
                moves.append((r, c))
                break
            else:
                break
            r, c = r + dr, c + dc
    return moves

# Function to get legal moves for a rook
def get_rook_moves(board, row, col):
    moves = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < 8 and 0 <= c < 8:
            if board[r][c] == "":
                moves.append((r, c))
            elif board[r][c][0] != board[row][col][0]:
                moves.append((r, c))
                break
            else:
                break
            r, c = r + dr, c + dc
    return moves

# Function to get legal moves for a queen
def get_queen_moves(board, row, col):
    return get_rook_moves(board, row, col) + get_bishop_moves(board, row, col)

# Function to get legal moves for a king
def get_king_moves(board, row, col):
    moves = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] == "" or board[r][c][0] != board[row][col][0]):
            moves.append((r, c))
    return moves


# Main game loop
# Function to move a piece on the board
def move_piece(board, start, end):
    start_row, start_col = start
    end_row, end_col = end
    piece = board[start_row][start_col]

    # Check if the move is valid
    if end in get_legal_moves(board, start_row, start_col):
        # Move the piece to the new position
        board[end_row][end_col] = piece
        board[start_row][start_col] = ""
        return True
    else:
        return False


# Function to get all legal moves for a piece
def get_legal_moves(board, row, col):
    piece = board[row][col]
    if piece == "":
        return []
    if piece[1] == 'P':
        return get_pawn_moves(board, row, col)
    elif piece[1] == 'N':
        return get_knight_moves(board, row, col)
    elif piece[1] == 'B':
        return get_bishop_moves(board, row, col)
    elif piece[1] == 'R':
        return get_rook_moves(board, row, col)
    elif piece[1] == 'Q':
        return get_queen_moves(board, row, col)
    elif piece[1] == 'K':
        return get_king_moves(board, row, col)
    return []

# Main game loop
def main():
    board = starting_board
    selected_square = None
    is_white_turn = True  # Initialize with white's turn
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                col = mouse_pos[0] // SQUARE_SIZE
                row = mouse_pos[1] // SQUARE_SIZE
                if selected_square is None:
                    if (is_white_turn and board[row][col] != "" and board[row][col][0] == 'w') or \
                            (not is_white_turn and board[row][col] != "" and board[row][col][0] == 'b'):
                        selected_square = (row, col)
                else:
                    if move_piece(board, selected_square, (row, col)):
                        selected_square = None
                        is_white_turn = not is_white_turn  # Switch turns
                    else:
                        if (is_white_turn and board[row][col] != "" and board[row][col][0] == 'w') or \
                                (not is_white_turn and board[row][col] != "" and board[row][col][0] == 'b'):
                            selected_square = (row, col)

        screen.fill((255, 255, 255))
        draw_board(board)
        if selected_square is not None:
            pygame.draw.rect(screen, (0, 255, 0), (selected_square[1] * SQUARE_SIZE, selected_square[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 4)
        pygame.display.flip()
        clock.tick(FPS)

# Entry point of the program
if __name__ == "__main__":
    main()

