import pygame
from Functions import check_collision

class Ball:
    def __init__(self, screen, screen_x, screen_y):
        self.screen = screen
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.ball_x = screen_x / 2
        self.ball_y = screen_y / 2
        self.ball_velocity_x = 5
        self.ball_velocity_y = 5
        self.radius = 5
        self.color = pygame.Color("white")

    def get_radius(self):
        return self.radius

    def get_ball_x(self):
        return self.ball_x

    def get_ball_y(self):
        return self.ball_y

    def get_ball_velocity_x(self):
        return self.ball_velocity_x

    def get_ball_velocity_y(self):
        return self.ball_velocity_y

    def move(self, paddle1, paddle2):
        # original movement
        self.ball_x = self.ball_x + self.ball_velocity_x
        self.ball_y = self.ball_y + self.ball_velocity_y

        # check for paddle or screen collision
        if ((check_collision(paddle1, self) == 1) or 
            (self.ball_x - self.radius <= 0) or 
            (check_collision(paddle2, self) == 2) or 
            (self.ball_x + self.radius >= self.screen_x)):
            self.ball_velocity_x = - self.ball_velocity_x
        if (self.ball_y - self.radius <= 0 or self.ball_y + self.radius >= self.screen_y):
            self.ball_velocity_y = - self.ball_velocity_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)