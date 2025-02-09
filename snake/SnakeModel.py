# Wzorzec MVC - Model //Singleton
import os
import pickle
import sys
import pygame

from memento.GameStateMemento import *
from food.RedFood import RedFood
from food.YellowFood import YellowFood

class SnakeModel:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init(*args, **kwargs)
        return cls._instance

    def init(self, width, height, food_strategy):
        self.snake = [(100, 100)]
        self.width = width
        self.height = height
        self.food_strategy = food_strategy
        self.food = self.generate_food()
        self.direction = (1, 0)
        self.game_started = False
        self.memento = None
        self.can_restore = True

    def move(self):
        if not self.game_started:
            return

        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        if (
            self.food.position[0] - 20 <= new_head[0] <= self.food.position[0] + 20 and
            self.food.position[1] - 20 <= new_head[1] <= self.food.position[1] + 20
        ):
            if isinstance(self.food, YellowFood) or isinstance(self.food, RedFood):
                self.food.apply_effect(self) 
                for _ in range(20):
                    self.snake.append(self.snake[-1]) 

            self.food = self.generate_food()
        else:
            if new_head in self.snake[1:]:
                print("Game Over!")
                pygame.quit()
                sys.exit()

            self.snake.pop()

        new_head = (new_head[0] % self.width, new_head[1] % self.height)
        self.snake.insert(0, new_head)

    def generate_food(self):
        return self.food_strategy.generate_food(self.width, self.height, self.snake)

    def create_memento(self):
        return GameStateMemento(list(self.snake), self.food, self.direction)

    def restore_from_memento(self, memento):
        self.snake = memento.snake
        self.food = memento.food
        self.direction = memento.direction

    def save_game_state(self):
        self.memento = self.create_memento()
        with open("game_state.pickle", "wb") as file:
            pickle.dump(self.memento, file)

    def load_game_state(self):
        if not self.game_started and self.can_restore:
            try:
                with open("game_state.pickle", "rb") as file:
                    self.memento = pickle.load(file)
                    self.restore_from_memento(self.memento)
                    print("Game state restored.")
            except FileNotFoundError:
                print("No previous game state found.")

            try:
                os.remove("game_state.pickle")
            except FileNotFoundError:
                pass
            self.game_started = True
            self.can_restore = False
            self.memento = None

    def get_score(self):
        return len(self.snake) // 20