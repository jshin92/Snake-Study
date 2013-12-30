import pygame


class Block:
    """ A class that represents a drawable block on the screen. """
    def __init__(self, row, col, color, boundary_offset, rect_size, direction):
        self.row = row
        self.col = col
        self.color = color
        self.boundary_offset = boundary_offset
        self.rect_size = rect_size
        self.direction = direction

    # draws the block based off the offset and rectangle size
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.boundary_offset + (self.boundary_offset + self.rect_size) * self.col,
                                              self.boundary_offset + (self.boundary_offset + self.rect_size) * self.row,
                                              self.rect_size,
                                              self.rect_size])

    # checks if any block collides with a front (head) of a snake
    def collides_with(self, snake):
            if self.row == snake.parts[0].row and self.col == snake.parts[0].col:
                return True
            else:
                return False

