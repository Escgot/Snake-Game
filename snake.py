import pygame
import sys
import random

# --- 1. Setup and Initialization ---
pygame.init()

GAME_WIDTH, GAME_HEIGHT = 600, 400
UI_WIDTH = 200
WINDOW_WIDTH = GAME_WIDTH + UI_WIDTH 
WINDOW_HEIGHT = GAME_HEIGHT          

BLOCK_SIZE = 20 
FPS = 12

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake with UI Panel")
clock = pygame.time.Clock()

pygame.font.init()
title_font = pygame.font.SysFont("monospace", 24, bold=True)
stat_font = pygame.font.SysFont("monospace", 20)

# Colors
BLACK = (0, 0, 0)
DARK_GRAY = (40, 40, 40) 
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)     

# NEW: Accept high_score as an argument so it survives death
def main(high_score): 
    # --- 2. Initial Game State ---
    snake_x = GAME_WIDTH // 2
    snake_y = GAME_HEIGHT // 2
    snake_body = [[snake_x, snake_y]]
    
    dx = BLOCK_SIZE
    dy = 0

    food_x = random.randrange(0, GAME_WIDTH, BLOCK_SIZE)
    food_y = random.randrange(0, GAME_HEIGHT, BLOCK_SIZE)

    score = 0

    running = True
    while running:
        # --- 3. Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0

        # --- 4. Game Logic ---
        new_head_x = (snake_body[0][0] + dx) % GAME_WIDTH
        new_head_y = (snake_body[0][1] + dy) % GAME_HEIGHT
        new_head = [new_head_x, new_head_y]

        # --- GAME OVER CONDITION ---
        if new_head in snake_body:
            # NEW: We only check and refresh the high score right as you die
            if score > high_score:
                high_score = score
            running = False # Break the loop to restart the game
            
        else:
            # Only move and eat if we didn't just die
            snake_body.insert(0, new_head)

            if new_head_x == food_x and new_head_y == food_y:
                score += 1
                # Notice we no longer update the high score here!
                food_x = random.randrange(0, GAME_WIDTH, BLOCK_SIZE)
                food_y = random.randrange(0, GAME_HEIGHT, BLOCK_SIZE)
            else:
                snake_body.pop()

        # --- 5. Drawing ---
        window.fill(BLACK) 
        
        # Game Elements
        pygame.draw.rect(window, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))
        for block in snake_body:
            pygame.draw.rect(window, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

        # UI Panel Background
        pygame.draw.rect(window, DARK_GRAY, (GAME_WIDTH, 0, UI_WIDTH, WINDOW_HEIGHT))
        pygame.draw.line(window, BLUE, (GAME_WIDTH, 0), (GAME_WIDTH, WINDOW_HEIGHT), 5)

        # UI Text
        title_surface = title_font.render("STATS", True, WHITE)
        window.blit(title_surface, (GAME_WIDTH + 60, 20))

        score_surface = stat_font.render(f"Score: {score}", True, WHITE)
        window.blit(score_surface, (GAME_WIDTH + 20, 80))

        best_surface = stat_font.render(f"Best:  {high_score}", True, WHITE)
        window.blit(best_surface, (GAME_WIDTH + 20, 120))

        pygame.display.flip()
        clock.tick(FPS)

    # NEW: Start the next round and pass the newly refreshed high score into it
    main(high_score)

if __name__ == "__main__":
    # The very first time the game opens, the high score is 0
    main(0)