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

    def move(self, up, down):
        key = pygame.key.get_pressed()
        if self.top - self.speed >= 0:
            if key[up]:
                self.top = self.top - self.speed
        if self.top + self.height + self.speed <= 400:   
            if key[down]:
                self.top = self.top + self.speed
    
    def draw(self):
        rect_info = pygame.Rect(self.left, self.top, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, rect_info)