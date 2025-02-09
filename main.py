from strategy.RandomFoodStrategy import RandomFoodStrategy
from snake.SnakeController import SnakeController
from snake.SnakeModel import SnakeModel
from snake.SnakeView import SnakeView


if __name__ == "__main__":
    food_strategy = RandomFoodStrategy()

    model = SnakeModel(400, 400, food_strategy)

    view = SnakeView()
    controller = SnakeController(model, view)

    controller.run_game()