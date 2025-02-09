# Wzorzec MVC - Widok
import sys
import pygame

class SnakeView:
    def __init__(self):
        pygame.init()
        self.window_size = (400, 400)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

    def draw_snake(self, snake):
        for i, segment in enumerate(snake):
            if i % 40 < 20:
                pygame.draw.circle(self.screen, (0, 255, 0), (segment[0] + 10, segment[1] + 10), 10)
            else: 
                pygame.draw.circle(self.screen, (0, 255, 255), (segment[0] + 10, segment[1] + 10), 10)

    def draw_score(self, score):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def draw_food(self, food):
        pygame.draw.circle(self.screen, food.color, (food.position[0] + 10, food.position[1] + 10), 10)

    def clear_screen(self):
        self.screen.fill((0, 0, 0))

    def update_display(self):
        pygame.display.flip()

    def handle_events(self, model):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and model.direction != (0, 1):
                    model.direction = (0, -1)
                    if not model.game_started:
                        model.game_started = True
                elif event.key == pygame.K_DOWN and model.direction != (0, -1):
                    model.direction = (0, 1)
                    if not model.game_started:
                        model.game_started = True
                elif event.key == pygame.K_LEFT and model.direction != (1, 0):
                    model.direction = (-1, 0)
                    if not model.game_started:
                        model.game_started = True
                elif event.key == pygame.K_RIGHT and model.direction != (-1, 0):
                    model.direction = (1, 0)
                    if not model.game_started:
                        model.game_started = True
                elif event.key == pygame.K_q:
                    model.save_game_state()
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    model.load_game_state()
                    model.game_started = True