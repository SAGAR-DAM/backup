import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
BACKGROUND_COLOR = (255, 255, 255)
GRID_COLOR = (0, 0, 0)
SELECTED_CELL_COLOR = (173, 216, 230)
FONT_COLOR = (0, 0, 0)
FINISHED_COLOR = (0, 128, 0)
FPS = 30

# Sudoku board (0 represents empty cell)
initial_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

class Sudoku:
    def __init__(self):
        self.board = self.generate_board()
        self.selected = None
        self.font = pygame.font.Font(None, 40)
        self.finished_font = pygame.font.Font(None, 60)

    def generate_board(self):
        # Function to generate a random valid Sudoku board
        board = [[0]*9 for _ in range(9)]
        self.solve_board(board)
        self.remove_numbers(board)
        return board

    def solve_board(self, board):
        # Function to solve a Sudoku board using backtracking
        find = self.find_empty(board)
        if not find:
            return True
        else:
            row, col = find

        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num

                if self.solve_board(board):
                    return True

                board[row][col] = 0

        return False

    def is_valid(self, board, num, pos):
        # Function to check if placing a number in a specific position is valid
        # Check row
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(self, board):
        # Function to find an empty cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)  # row, col
        return None

    def remove_numbers(self, board):
        # Function to remove numbers from the board to create a puzzle
        squares = 81
        empties = 60  # adjust this number to control difficulty

        for _ in range(empties):
            i = random.randint(0, squares - 1)
            board[i // 9][i % 9] = 0

    def draw_grid(self, screen):
        screen.fill(BACKGROUND_COLOR)

        for i in range(10):
            line_width = 4 if i % 3 == 0 else 1
            pygame.draw.line(screen, GRID_COLOR, (i * WIDTH // 9, 0), (i * WIDTH // 9, HEIGHT), line_width)
            pygame.draw.line(screen, GRID_COLOR, (0, i * HEIGHT // 9), (WIDTH, i * HEIGHT // 9), line_width)

        if self.selected:
            pygame.draw.rect(screen, SELECTED_CELL_COLOR,
                             (self.selected[1] * WIDTH // 9, self.selected[0] * HEIGHT // 9, WIDTH // 9, HEIGHT // 9))

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    value = self.font.render(str(self.board[i][j]), True, FONT_COLOR)
                    screen.blit(value, (j * WIDTH // 9 + 30, i * HEIGHT // 9 + 20))

    def select(self, row, col):
        self.selected = (row, col)

    def place_value(self, value):
        row, col = self.selected
        if self.board[row][col] == 0:
            self.board[row][col] = value

    def is_board_complete(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return False
        return True

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    game = Sudoku()

    running = True
    solved = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[1] // (HEIGHT // 9)
                col = pos[0] // (WIDTH // 9)
                game.select(row, col)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game.place_value(1)
                if event.key == pygame.K_2:
                    game.place_value(2)
                if event.key == pygame.K_3:
                    game.place_value(3)
                if event.key == pygame.K_4:
                    game.place_value(4)
                if event.key == pygame.K_5:
                    game.place_value(5)
                if event.key == pygame.K_6:
                    game.place_value(6)
                if event.key == pygame.K_7:
                    game.place_value(7)
                if event.key == pygame.K_8:
                    game.place_value(8)
                if event.key == pygame.K_9:
                    game.place_value(9)

        if not solved and game.is_board_complete():
            solved = True  # Add your own logic here if you want to check for solution

        game.draw_grid(screen)

        if solved:
            finished_text = game.finished_font.render("Sudoku Solved!", True, FINISHED_COLOR)
            screen.blit(finished_text, (WIDTH // 2 - finished_text.get_width() // 2, HEIGHT - 80))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
