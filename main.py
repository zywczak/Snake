from RandomFoodStrategy import RandomFoodStrategy
from SnakeController import SnakeController
from SnakeModel import SnakeModel
from SnakeView import SnakeView


if __name__ == "__main__":
    food_strategy = RandomFoodStrategy()

    model = SnakeModel(400, 400, food_strategy)

    view = SnakeView()
    controller = SnakeController(model, view)

    controller.run_game()