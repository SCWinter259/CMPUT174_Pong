import pygame

screen_x = 500
screen_y = 400

def main():
    pygame.init()
    size = (screen_x, screen_y)
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

        # set the ball to be in the middle of the screen
        ball_x = screen_x / 2
        ball_y = screen_y / 2
        ball_velocity_x = 5
        ball_velocity_y = 5
        ball_radius = 5

        paddle_width = 5
        paddle_height = 40
        paddle_top = (screen_x / 2) - (paddle_height / 2)
        paddle_speed = 10

        paddle1_left = 30
        paddle2_left = screen_x - 30 - paddle_width

        self.ball = Ball(screen, ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius)
        self.paddle1 = Paddle(screen, paddle1_left, paddle_top, paddle_width, paddle_height, paddle_speed)
        self.paddle2 = Paddle(screen, paddle2_left, paddle_top, paddle_width, paddle_height, paddle_speed)

class Score:
    def __init__(self):
        pass

    def draw(self):
        pass

class Paddle:
    def __init__(self, screen, left, top, width, height, speed):
        self.screen = screen
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.speed = speed
        self.color = pygame.Color("white")

    def move(self):
        pass
    
    def draw(self):
        pass

class Ball:
    def __init__(self, screen, ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius):
        self.screen = screen
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.ball_velocity_x = ball_velocity_x
        self.ball_velocity_y = ball_velocity_y
        self.radius = ball_radius
        self.color = pygame.Color("white")

    def move(self):
        pass

    def draw(self):
        pass