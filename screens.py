import pygame

def show_game_over(screen):
    font = pygame.font.Font(None, 74)  # Use default font
    text = font.render("Game Over", True, (255, 0, 0))  # Red color
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    restart_font = pygame.font.Font(None, 36)
    restart_text = restart_font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

    # Game loop for the game over screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return  True
                if event.key == pygame.K_q:
                    pygame.quit()
                    return

        # Fill the screen with black or another background color
        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        screen.blit(restart_text, restart_rect)
        pygame.display.flip()