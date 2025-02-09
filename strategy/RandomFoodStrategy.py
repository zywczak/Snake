# Wzorzec Strategia - Konkretna strategia (Losowe generowanie jedzenia)
import random
from strategy.FoodStrategy import FoodStrategy
from food.RedFood import RedFood
from food.YellowFood import YellowFood

class RandomFoodStrategy(FoodStrategy):
    def generate_food(self, width, height, snake):
        random_number = random.randint(0, 9)
        if random_number == 0:
            return YellowFood(width, height, snake)
        else:
            return RedFood(width, height, snake)