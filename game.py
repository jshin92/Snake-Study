from Snake import *
import random

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

# coordinates used in text blitting
SNAKE_TEXT_LOC = [0, 0]
UNPAUSE_TEXT_LOC = [170, 250]
GAME_OVER_TEXT_LOC = [100, 100]

pygame.init()

FPS = 6
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
RECT_SIZE = 20
BOUNDARY_OFFSET = 10
MAX_COLS = SCREEN_WIDTH//(RECT_SIZE + BOUNDARY_OFFSET)
MAX_ROWS = SCREEN_HEIGHT//(RECT_SIZE + BOUNDARY_OFFSET)
DEFAULT_DIR = "UP"

# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

snake_text = pygame.image.load("assets/snake_text.png").convert()
snake_text.set_colorkey(BLACK)
unpause_text = pygame.image.load("assets/unpause.png").convert()
unpause_text.set_colorkey(BLACK)
game_over_text = pygame.image.load("assets/game_over.png").convert()

pygame.display.set_caption("Snake!")

# Loop until the user clicks the close button.
done = False
# start the game paused.
paused = True
first_time = True
lost = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

snake = Snake(MAX_ROWS, MAX_COLS, GREEN, BOUNDARY_OFFSET, RECT_SIZE, DEFAULT_DIR)
apple = Block(random.randrange(MAX_ROWS), random.randrange(MAX_COLS), RED, BOUNDARY_OFFSET, RECT_SIZE, DEFAULT_DIR)
# -------- Main Program Loop -----------
while not done:
    # need to keep track if we've processed a key or not
    # lest the snake can enter inside itself with quick presses
    pressedArrowKey = False
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN and not pressedArrowKey:
            head = snake.parts[0]
            if event.key == pygame.K_UP and snake.parts[0].direction != "DOWN":
                head.direction = "UP"
                pressedArrowKey = True
            elif event.key == pygame.K_DOWN and snake.parts[0].direction != "UP":
                head.direction = "DOWN"
                pressedArrowKey = True
            elif event.key == pygame.K_LEFT and snake.parts[0].direction != "RIGHT":
                head.direction = "LEFT"
                pressedArrowKey = True
            elif event.key == pygame.K_RIGHT and snake.parts[0].direction != "LEFT":
                head.direction = "RIGHT"
                pressedArrowKey = True
            # can also use 'q' to quit
            elif event.key == pygame.K_q:
                done = True
            elif event.key == pygame.K_SPACE:
                paused = not paused
                first_time = False
            elif event.key == pygame.K_r and lost:
                # reset game if 'r' is pressed
                lost = False
                snake = Snake(MAX_ROWS, MAX_COLS, GREEN, BOUNDARY_OFFSET, RECT_SIZE, DEFAULT_DIR)


    # --- Game logic
    if not paused and not lost:
        collided = False
        if apple.collides_with(snake):
            collided = True
            apple = Block(random.randrange(MAX_ROWS), random.randrange(MAX_COLS), RED, BOUNDARY_OFFSET, RECT_SIZE, DEFAULT_DIR)
            print("Apple gobbled!")

        snake.update(collided)

        # check for snake eating itself
        head = snake.parts[0]
        for body_segment in snake.parts:
            if body_segment.collides_with(snake) and head != body_segment:
                print("Snake ate itself")
                lost = True

        # check for snake going out of bounds
        for body_segment in snake.parts:
            if body_segment.row < 0 or body_segment.row >= MAX_ROWS or body_segment.col < 0 or body_segment.col >= MAX_COLS:
                print("Out of bounds")
                lost = True

    # --- Drawing code
    # -- Clear with black
    screen.fill(BLACK)
    apple.draw(screen)
    snake.draw(screen)

    # only show 'Snake' on startup
    if first_time:
        screen.blit(snake_text, SNAKE_TEXT_LOC)
    # only show instructions on how to unpause when paused
    if paused:
        screen.blit(unpause_text, UNPAUSE_TEXT_LOC)
    # show game over screen if player lost
    if lost:
        screen.blit(game_over_text, GAME_OVER_TEXT_LOC)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- set refresh rate to FPS (defined above)
    clock.tick(FPS)

# Close the window and quit.
pygame.quit()
