import pygame

class Paddle:
    def __init__(self, screen, left, top):
        self.screen = screen
        self.left = left
        self.top = top
        self.width = 5
        self.height = 40
        self.speed = 10
        self.color = pygame.Color("white")

    def get_left(self):
        return self.left

    def get_top(self):
        return self.top

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def move(self):
        pass
    
    def draw(self):
        pass