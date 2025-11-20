class Salesman:
    def __init__(self, array_of_cities):
        self.array_of_cities = array_of_cities
        self.current = 0
        self.x = array_of_cities[self.current].x
        self.y = array_of_cities[self.current].y

    def advance(self):
        #Increase index on path
        self.current += 1

        #If there is another city at current, update position to next city.
        if self.current < len(self.array_of_cities):
            self.x = self.array_of_cities[self.current].x
            self.y = self.array_of_cities[self.current].y
        
        

        
        

