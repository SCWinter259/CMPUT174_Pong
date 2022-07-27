import pygame
import Functions
import Ball
import Paddle
import Score

def main():
    pygame.init()
    size = (500, 400)
    pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")
    screen = pygame.display.get_surface()
    game = Game(screen)
    game.play()

class Game:
    '''
    This is the game object, which controls the game
    '''
    def __init__(self, screen):
        self.screen = screen
        self.background_color = pygame.Color('black')
        self.game_clock = pygame.time.Clock()   # set up the clock to control FPS later on
        self.FPS = 30
        self.continue_game = True
        self.close_clicked = False

        screen_x = pygame.display.get_window_size()[0]
        screen_y = pygame.display.get_window_size()[1]

        # set up paddles
        paddle_height = 40
        paddle_width = 5
        paddle_top = (screen_x / 2) - (paddle_height / 2)

        paddle1_left = 30
        paddle2_left = screen_x - 30 - paddle_width

        # set up and down button for each paddle
        up1 = pygame.K_q
        down1 = pygame.K_a
        up2 = pygame.K_q
        down2 = pygame.K_l

        self.ball = Ball(screen, screen_x, screen_y)
        self.paddle1 = Paddle(screen, paddle1_left, paddle_top)
        self.paddle2 = Paddle(screen, paddle2_left, paddle_top)
        self.score1 = Score(screen, self.paddle1)
        self.score2 = Score(screen, self.paddle2)

    def update(self):
        pass

    def play(self):
        pass

    def handle_event(self):
        pass

    def draw(self):
        pass