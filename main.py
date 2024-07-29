# main.py

import pygame
from snake import Snake
from food import Food
from fireworks import Fireworks
from player_ai import PlayerAI
from settings import *

def main():
    pygame.init()
    pygame.mixer.init()  # Initialize the mixer module
    clock = pygame.time.Clock()

    # Load sounds
    move_sound = pygame.mixer.Sound("snake_game\sound\move.mp3")
    eat_sound = pygame.mixer.Sound("snake_game\sound\eat.mp3")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Python Snake')

    snake = Snake()
    food = Food()
    fireworks = Fireworks()

    ai_player = None
    human_player = True
    paused = False

    # Start screen
    start_screen = True
    while start_screen:
        screen.fill(BLACK)
        font = pygame.font.Font(None, 74)
        text = font.render("Python Snake", True, WHITE)
        screen.blit(text, (WIDTH // 4, HEIGHT // 4))
        font = pygame.font.Font(None, 36)
        text = font.render("Press H for Human Player or A for AI Player", True, WHITE)
        screen.blit(text, (WIDTH // 8, HEIGHT // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    human_player = True
                    start_screen = False
                elif event.key == pygame.K_a:
                    human_player = False
                    ai_player = PlayerAI(snake, food)
                    start_screen = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                elif human_player:  # Only handle key events for human player
                    if event.key == pygame.K_UP:
                        snake.turn((0, -CELL_SIZE))
                        move_sound.play()
                    elif event.key == pygame.K_DOWN:
                        snake.turn((0, CELL_SIZE))
                        move_sound.play()
                    elif event.key == pygame.K_LEFT:
                        snake.turn((-CELL_SIZE, 0))
                        move_sound.play()
                    elif event.key == pygame.K_RIGHT:
                        snake.turn((CELL_SIZE, 0))
                        move_sound.play()

        if not paused:
            if not human_player:
                next_move = ai_player.get_next_move()
                snake.turn(next_move)

            snake.move()
            if snake.get_head_position() == food.position:
                snake.grow = True
                snake.score += 1
                food.randomize_position()
                eat_sound.play()  # Play eating sound
                if snake.score % 5 == 0:  # Increase level every 5 points
                    snake.level += 1
                    snake.speed += 1  # Increase speed with each level, more gradually
                    fireworks.trigger()  # Trigger fireworks on level up

            fireworks.update()

            screen.fill(BLACK)
            snake.draw(screen)
            food.draw(screen)
            fireworks.draw(screen)

            # Display score and level
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'Score: {snake.score}', True, WHITE)
            level_text = font.render(f'Level: {snake.level}', True, WHITE)
            screen.blit(score_text, (10, 10))
            screen.blit(level_text, (10, 50))

        else:
            font = pygame.font.Font(None, 74)
            pause_text = font.render("Paused", True, WHITE)
            screen.blit(pause_text, (WIDTH // 3, HEIGHT // 3))

        pygame.display.update()
        clock.tick(snake.speed)

if __name__ == '__main__':
    main()
