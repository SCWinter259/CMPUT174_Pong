import pygame

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

        self.ball = Ball(screen, screen_x, screen_y)
        self.paddle1 = Paddle(screen, paddle1_left, paddle_top)
        self.paddle2 = Paddle(screen, paddle2_left, paddle_top)

class Score:
    def __init__(self):
        self.score = 0

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

def check_collision(paddle, ball):
    '''
    Checks whether the ball and either paddles have collided
    or not. Returns 1 or 2 as of which paddle collided with the ball.
    Ball will bounce off at the front of each paddle, but can
    go through the sides or the back.
    Returns 0 if no collision happened
    '''
    # ball collided with left (first) paddle
    left = paddle.get_left()
    top = paddle.get_top()
    width = paddle.get_width()
    height = paddle.get_height()
    direction = ball.get_velocity_x()
    ball_x = ball.get_ball_x()
    ball_y = ball.get_ball_y()
    radius = ball.get
    # ball collided with left (first) paddle
    if left == 30:
        if ((direction < 0) and (ball_x - radius <= left + width) and
            (top + height >= ball_y - radius) and (ball_y - radius >= top)):
            return 1
        else:
            return 0
    # ball collided with right (second) paddle
    else:
        if ((direction > 0) and (ball_x + radius >= left) and
            (top + height >= ball_y - radius) and (ball_y - radius >= top)):
            return 2
        else:
            return 0