import pygame

#Initialising Font type and their size
pygame.font.init()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#Forming a class 'Text' and declaring their properties
class Texts:
    
    def __init__ (self, text, colour, size):

        self.text = text
        self.colour = colour
        self.size = size

    def text_objects (self):

        if self.size == "small":
            textSurface = smallfont.render(self.text, True, self.colour)

        elif self.size == "medium":
            textSurface = medfont.render(self.text, True, self.colour)

        elif self.size == "large":
            textSurface = largefont.render(self.text, True, self.colour)

        return textSurface,textSurface.get_rect()
