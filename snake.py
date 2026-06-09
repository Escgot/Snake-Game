import pygame
import sys
import random

# --- 1. Setup and Initialization ---
pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20 # The size of our grid squares
FPS = 12

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Classic Snake")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def main():
    # --- 2. Initial Game State ---
    # Snake starts in the middle
    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2
    
    # The snake is a list of [x, y] coordinates
    snake_body = [[snake_x, snake_y]]
    
    # Movement direction (Starts moving right)
    dx = BLOCK_SIZE
    dy = 0

    # Generate first food randomly on the grid
    food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)

    running = True
    while running:
        # --- 3. Event Handling (Controls) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Key presses
            if event.type == pygame.KEYDOWN:
                # Prevent reversing into yourself
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0

        # --- 4. Game Logic ---
        # Calculate new head position
        new_head_x = snake_body[0][0] + dx
        new_head_y = snake_body[0][1] + dy
        new_head = [new_head_x, new_head_y]

        # Check for Game Over (Wall collision)
        if (new_head_x < 0 or new_head_x >= WIDTH or 
            new_head_y < 0 or new_head_y >= HEIGHT):
            running = False # End loop if we hit a wall
            
        # Check for Game Over (Self collision)
        if new_head in snake_body:
            running = False

        # Move the snake (Add new head)
        snake_body.insert(0, new_head)

        # Check for Food
        if new_head_x == food_x and new_head_y == food_y:
            # We ate food! Don't remove the tail, just spawn new food
            food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)
        else:
            # Didn't eat food, remove the tail so we stay the same length
            snake_body.pop()

        # --- 5. Drawing ---
        window.fill(BLACK) # Clear screen
        
        # Draw Food
        pygame.draw.rect(window, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))
        
        # Draw Snake
        for block in snake_body:
            pygame.draw.rect(window, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.flip()
        clock.tick(FPS)

    # If we break out of the loop, the game is over. 
    # Restart the game by calling main() again.
    main()

# Start the game
if __name__ == "__main__":
    main()