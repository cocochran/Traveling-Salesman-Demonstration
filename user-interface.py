import brute_force as bf
import greedy as g
import pygame
from city import *
from salesman import *
from enum import Enum

class Mode(Enum):
    BRUTE_FORCE = 1
    GREEDY = 2

class TSPModel:
    
    def __init__(self, width, height, city_count):
        self.width = width
        self.height = height
        self.mode = Mode.BRUTE_FORCE
        self.city_count = city_count
        self.cities = generate_cities(self.city_count, self.width * 0.9, self.height * 0.9)
        #Salesman is not accessible until after the simulation has begun

    def start_simulation(self):
        match self.mode:
            case Mode.BRUTE_FORCE:
                self.cities = bf.determine_optimal_path(self.cities)
            case Mode.GREEDY:
                self.cities = g.determine_optimal_path(self.cities)
            case _:
                self.cities = bf.determine_optimal_path(self.cities)
               
        self.salesman = Salesman(self.cities)
        
        


class TSPView:
    def __init__(self, model, width, height):
        
        #Make game window
        pygame.init()
        self.model = model
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.canvas = pygame.surface.Surface((width / 2, height / 2))
        running = True
        self.model.start_simulation()
        self.width = width
        self.height = height

        while running:
            # poll for events
            for event in pygame.event.get():
                # 1. Handle window close
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.model.salesman.advance() 
                    

            # fill the screen with a color to wipe away anything from last frame
            
            self.screen.fill("white")
            self.draw_path()
            self.draw_cities()
            pygame.draw.circle(self.screen, "red", (self.model.salesman.x, self.model.salesman.y), 10)
            # RENDER YOUR GAME HERE

            

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(5)  # limits FPS to 60

        pygame.quit()



    def draw_cities(self):
        #Define text colors
        white =  (255, 255, 255)
        blue = (0, 71, 171)
        

        #Cities are the list of cities *in order*.
        cities = list(self.model.cities)
        font_size = 12
        font = pygame.font.SysFont('timesnewroman',  font_size)
        for i in range(0, len(cities)):
            x_offset = -5
            y_offset = 10

            name = cities[i].identifier

            #Render city name.
            city_label = font.render(f"{name}", False, blue, white)   
            pygame.draw.circle(self.screen, "black", (cities[i].x, cities[i].y), 5)
            
            #Actually render the city name.
            if cities[i].x + x_offset + font_size < 0:
                x_offset = 20
            elif cities[i].x + x_offset + font_size > self.width:
                x_offset = -30
            

            if cities[i].y + y_offset + font_size > self.height:
                y_offset = -30
            
            self.screen.blit(city_label, (cities[i].x + x_offset, cities[i].y + y_offset))
    
    def draw_path(self):
        cities = self.model.cities 
        salesman_pos = self.model.salesman.current
        if salesman_pos < len(cities) - 1:
            pygame.draw.line(self.screen, "red", (cities[salesman_pos].x, cities[salesman_pos].y), (cities[salesman_pos+1].x, cities[salesman_pos+1].y), 2)
        
        else:
            for i in range(0, len(cities) - 1):
                pygame.draw.line(self.screen, "black", (cities[i].x, cities[i].y), (cities[i+1].x, cities[i+1].y), 2)



class TSPController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

def main():
    width = 1280
    height = 720
    city_count = 8
    model = TSPModel(width, height, city_count)
    view = TSPView(model, width, height)
    controller = TSPController(model, view)



if __name__ == "__main__":
    main()