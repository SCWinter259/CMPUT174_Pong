import pygame

class Score:
    def __init__(self, screen, paddle):
        self.screen = screen
        self.score = 0
        self.color = pygame.Color("white")
        self.paddle = paddle
        self.font = pygame.font.SysFont("", 50)

    def get_score(self):
        return self.score

    def change_score(self):
        '''
        checks for ball collision with the end of the screen
        and change the score if any collision happened
        '''
        pass

    def draw(self):
        pass