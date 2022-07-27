import pygame
from Ball import Ball
from Paddle import Paddle
from Score import Score

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
        self.FPS = 60
        self.continue_game = True
        self.close_clicked = False

        self.screen_x = pygame.display.get_window_size()[0]
        self.screen_y = pygame.display.get_window_size()[1]

        # set up paddles
        paddle_height = 40
        paddle_width = 5
        paddle_top = (self.screen_x / 2) - (paddle_height / 2)

        paddle1_left = 30
        paddle2_left = self.screen_x - 30 - paddle_width

        # set up and down button for each paddle
        self.up1 = pygame.K_q
        self.down1 = pygame.K_a
        self.up2 = pygame.K_p
        self.down2 = pygame.K_l

        self.ball = Ball(screen, self.screen_x, self.screen_y)
        self.paddle1 = Paddle(screen, paddle1_left, paddle_top)
        self.paddle2 = Paddle(screen, paddle2_left, paddle_top)
        self.score = Score(screen)

    def update(self):
        '''
        Update the state of every object
        '''
        self.ball.move(self.paddle1, self.paddle2)
        self.paddle1.move(self.up1, self.down1)
        self.paddle2.move(self.up2, self.down2)
        self.score.change_score(self.ball, self.screen_x)

    def draw(self):
        if self.continue_game == True:
            self.screen.fill(self.background_color) 
            self.update()
            self.ball.draw()
            self.paddle1.draw()
            self.paddle2.draw()
            self.score.draw()
        elif self.continue_game == False:
            color = pygame.Color("white")
            font = pygame.font.SysFont("", 50)
            if self.score.get_score_1() == 10:
                message = "player 1 won!"
            else:
                message = "player 2 won!"
            text = font.render(message, True, color)
            text_rect = text.get_rect(center=(self.screen_x / 2, self.screen_y / 2))
            self.screen.blit(text, text_rect)
        pygame.display.flip()

    def handle_event(self):
        '''
        Handles only the quit game event
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_clicked = True

    def play(self):
        '''
        Controls the game play
        '''
        while not self.close_clicked:
            self.handle_event()
            if self.score.get_score_1() < 10 and self.score.get_score_2() < 10:
                self.draw()
                self.game_clock.tick(self.FPS)
            elif self.score.get_score_1() == 10 or self.score.get_score_2() == 10:
                self.continue_game = False
                self.draw()
main()