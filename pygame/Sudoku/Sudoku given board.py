# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:40:28 2024

@author: mrsag
"""

import pygame
import time

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
board = [
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
    def __init__(self, board):
        self.board = board
        self.selected = None
        self.font = pygame.font.Font(None, 40)
        self.finished_font = pygame.font.Font(None, 60)

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

    def is_valid(self, row, col, num):
        # Check row
        if num in self.board[row]:
            return False
        
        # Check column
        for r in range(9):
            if self.board[r][col] == num:
                return False
        
        # Check 3x3 box
        box_row_start = row - row % 3
        box_col_start = col - col % 3
        for r in range(box_row_start, box_row_start + 3):
            for c in range(box_col_start, box_col_start + 3):
                if self.board[r][c] == num:
                    return False
        
        return True

    def solve_board(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.solve_board():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    game = Sudoku(board)

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
            solved = game.solve_board()
        
        game.draw_grid(screen)

        if solved:
            finished_text = game.finished_font.render("Sudoku Solved!", True, FINISHED_COLOR)
            screen.blit(finished_text, (WIDTH // 2 - finished_text.get_width() // 2, HEIGHT - 80))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
