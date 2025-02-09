# Wzorzec Fabryka - Konkretny produkt (żółte jedzenie)
import random
from food.Food import Food


class YellowFood(Food):
    def __init__(self, width, height, snake):
        position = self.generate_position(width, height, snake)
        super().__init__((255, 255, 0), position)

    def generate_position(self, width, height, snake):
        while True:
            x = random.randint(0, (width - 20) // 20) * 20
            y = random.randint(0, (height - 20) // 20) * 20
            if (x, y) not in snake:
                return x, y

    def apply_effect(self, model):
        for _ in range(20):
            model.snake.append(model.snake[-1]) 