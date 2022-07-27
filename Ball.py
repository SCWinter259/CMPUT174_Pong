import pygame

class Ball:
    def __init__(self, screen, screen_x, screen_y):
        self.screen = screen
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

    def move(self):
        pass

    def draw(self):
        pass