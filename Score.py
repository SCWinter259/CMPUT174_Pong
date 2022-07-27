import pygame

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.score1 = 0
        self.score2 = 0
        self.color = pygame.Color("white")
        self.font = pygame.font.SysFont("", 50)

    def get_score_1(self):
        return self.score1

    def get_score_2(self):
        return self.score2

    def change_score(self, ball, screen_x):
        '''
        checks for ball collision with the end of the screen
        and change the score if any collision happened
        '''
        if ball.get_ball_x() - ball.get_radius() <= 0:
            self.score1 = self.score1 + 1
        elif ball.get_ball_x() + ball.get_radius() >= screen_x:
            self.score2 = self.score2 + 1

    def draw(self):
        left_score = self.font.render(str(self.score1), True, self.color)
        self.screen.blit(left_score, (0, 0))          
        right_score = self.render(str(self.score2), True, self.color)
        self.screen.blit(right_score, (465, 0))