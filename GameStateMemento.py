# Wzorzec Memento - Memento
class GameStateMemento:
    def __init__(self, snake, food, direction):
        self.snake = snake
        self.food = food
        self.direction = direction