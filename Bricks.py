import pygame

#Manufacturing an object "Brick" 
class Brick:

    def __init__(self, x, y, colour):

        self.x = x
        self.y = y
        self.width = 30
        self.height = 20
	self.colour = colour

    #To 'draw' the "Brick" recntangle on the Game Screen 
    def render(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))

    #To 'return' the "Brick" object to a list
    def make_rects(self, window):

        r = pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))
        return r
        
