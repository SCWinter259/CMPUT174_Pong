import pygame
from Functions import check_collision
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
        self.up1 = pygame.K_q
        self.down1 = pygame.K_a
        self.up2 = pygame.K_q
        self.down2 = pygame.K_l

        self.ball = Ball(screen, screen_x, screen_y)
        self.paddle1 = Paddle(screen, paddle1_left, paddle_top)
        self.paddle2 = Paddle(screen, paddle2_left, paddle_top)
        self.score = Score(screen)

    def update(self):
        self.ball.move(self.paddle1, self.paddle2)
        self.paddle1.move(self.up1, self.down1)
        self.paddle2.move(self.up2, self.down2)

    def draw(self):
        self.screen.fill(self.background_color) 
        self.update()
        self.ball.draw()
        self.paddle1.draw()
        self.paddle2.draw()
        pygame.display.flip()

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_clicked = True

    def play(self):
        while not self.close_clicked:
            self.handle_event()
            if self.score.get_score1() <= 10 and self.score.get_score_2() <= 10:
                self.draw()
                self.game_clock.tick(self.FPS)

main()