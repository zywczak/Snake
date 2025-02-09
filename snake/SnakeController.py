# Wzorzec MVC - Kontroler
class SnakeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run_game(self):
        while True:
            self.view.clear_screen()
            self.view.draw_food(self.model.food)
            self.view.draw_snake(self.model.snake)
            self.view.draw_score(self.model.get_score())
            self.view.update_display()

            self.model.move()
            self.view.handle_events(self.model)

            self.view.clock.tick(300)