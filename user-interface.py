import brute_force as bf
import dynamic_programming as dp
import integer_linear_programming as ilp
import pygame
from city import *
from salesman import *
        
class TSPModel:
    def __init__(self, width, height, city_count):
        self.width = width
        self.height = height
        self.mode = "Brute Force"
        self.city_count = 10
        self.cities = generate_cities(self.city_count, self.width, self.height)
        self.salesman = Salesman(self.cities)
    
    def start_simulation(self):
        match self.mode:
            case "Brute Force":
                self.cities = bf.determine_optimal_path(self.cities)
            case "Dynamic Programming":
                self.cities = dp.determine_optimal_path(self.cities)
            case "Integer Linear Programming":
                self.cities = ilp.determine_optimal_path(self.cities)
            case _:
                self.cities = bf.determine_optimal_path(self.cities)
        
        self.salesman = Salesman(self.cities)


class TSPView:
    def __init__(self, model, width, height):
        
        pygame.init()
        self.model = model
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.canvas = pygame.surface.Surface((width / 2, height / 2))
        running = True

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()

                if event.type == pygame.QUIT:
                    running = False
                if keys[pygame.K_SPACE]:
                    self.update_view()

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("white")
            pygame.draw.circle(self.screen, "red", (self.model.salesman.x, self.model.salesman.y), 40)

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()

    def update_view(self):
        self.model.salesman.advance()
        self.screen.fill("white")
        pygame.draw.circle(self.screen, "red", (self.model.salesman.x, self.model.salesman.y), 40)

class TSPController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

def main():
    width = 1280
    height = 720
    city_count = 5
    model = TSPModel(width, height, city_count)
    view = TSPView(model, width, height)
    controller = TSPController(model, view)



if __name__ == "__main__":
    main()