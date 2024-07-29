from settings import *

class PlayerAI:
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food

    def get_next_move(self):
        head = self.snake.get_head_position()
        food_pos = self.food.position

        if head[0] < food_pos[0]:
            return (CELL_SIZE, 0)  # Move right
        elif head[0] > food_pos[0]:
            return (-CELL_SIZE, 0)  # Move left
        elif head[1] < food_pos[1]:
            return (0, CELL_SIZE)  # Move down
        else:
            return (0, -CELL_SIZE)  # Move up
