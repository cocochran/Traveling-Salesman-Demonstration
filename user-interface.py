import brute_force as bf
import dynamic_programming as dp
import integer_linear_programming as ilp
import pygame
from city import *
from salesman import *
        
class TSPModel:
    def __init__(self):
        self.mode = "Brute Force"

class TSPView:
    def __init__(self, model, width, height):
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        clock = pygame.time.Clock()
        canvas = pygame.surface.Surface((width / 2, height / 2))
        running = True

        salesman_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("white")
            pygame.draw.circle(screen, "red", player_pos, 40)

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

        pygame.quit()

class TSPController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

def main():
    width = 1280
    height = 720
    model = TSPModel()
    view = TSPView(model, width, height)
    controller = TSPController(model, view)



if __name__ == "__main__":
    main()