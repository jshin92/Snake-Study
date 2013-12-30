from Block import *


class Snake:
    """ A class that represents a snake. """
    def __init__(self, max_rows, max_cols, snake_color, boundary_offset, rect_size, dir):
        # initial piece starts in the middle
        self.start_row = max_rows//2
        self.start_col = max_cols//2
        self.snake_color = snake_color
        self.boundary_offset = boundary_offset
        self.rect_size = rect_size
        self.parts = []
        b = Block(self.start_row, self.start_col, self.snake_color, self.boundary_offset, self.rect_size, dir)
        self.parts.append(b)
        self.prev_collision_coords = None

    # draws a snake by drawing all of its pieces.
    def draw(self, screen):
        for piece in self.parts:
            piece.draw(screen)

    def update(self, collided):
        cur_head = self.parts[0]
        cur_tail = self.parts[-1]
        row_delta = 0
        col_delta = 0

        # if we ate a fruit, we need to add a new piece
        if collided:
            if cur_tail.direction == "UP":
                row_delta = 1
            elif cur_tail.direction == "DOWN":
                row_delta = -1
            elif cur_tail.direction == "LEFT":
                col_delta = 1
            elif cur_tail.direction == "RIGHT":
                col_delta = -1
            new_tail = Block(cur_tail.row + row_delta, cur_tail.col + col_delta, cur_tail.color,
                             cur_tail.boundary_offset, cur_tail.rect_size, cur_tail.direction)
            # add updated head of snake
            self.parts.append(new_tail)
        # otherwise, just move the head and remove the tail
        else:
            if cur_head.direction == "UP":
                row_delta = -1
            elif cur_head.direction == "DOWN":
                row_delta = 1
            elif cur_head.direction == "LEFT":
                col_delta = -1
            elif cur_head.direction == "RIGHT":
                col_delta = 1
            new_head = Block(cur_head.row + row_delta, cur_head.col + col_delta, cur_head.color,
                             cur_head.boundary_offset, cur_head.rect_size, cur_head.direction)
            # add updated head of snake
            self.parts.insert(0, new_head)
            # remove last part of snake
            self.parts.pop(-1)
