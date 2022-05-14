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
    def __init__(self, screen):
        self.screen = screen
        self.background_color = pygame.Color('black')
        self.game_clock = pygame.time.Clock()
        self.FPS = 30
        self.continue_game = True
        self.close_clicked = False
        
        paddle1_point = 0
        paddle2_point = 0
        
        ball_center = [250, 200]
        ball_velocity = [5, 5]
        ball_radius = 5
        
        paddle1_left = 30
        paddle1_top = 190
        paddle1_width = 5
        paddle1_height = 40
        
        paddle2_left = 465
        paddle2_top = 190
        paddle2_width = 5
        paddle2_height = 40     
        
        self.ball = Ball(screen, ball_center, ball_velocity, ball_radius, paddle1_point, paddle2_point)
        self.paddle1 = Paddle1(screen, paddle1_left, paddle1_top, paddle1_width, paddle1_height)
        self.paddle2 = Paddle2(screen, paddle2_left, paddle2_top, paddle2_width, paddle2_height)
        
    def collide(self):
        rect1 = pygame.Rect(self.paddle1.left, self.paddle1.top, self.paddle1.width, self.paddle1.height)
        rect2 = pygame.Rect(self.paddle2.left, self.paddle2.top, self.paddle2.width, self.paddle2.height)        
        if rect1.collidepoint(self.ball.center) == True and self.ball.velocity[0] < 0:
            self.ball.velocity[0] = -self.ball.velocity[0]
        if rect2.collidepoint(self.ball.center) == True and self.ball.velocity[0] > 0:
            self.ball.velocity[0] = -self.ball.velocity[0]          
    
    def update(self):
        # moving stuff
        self.collide()
        self.ball.move()
        self.paddle1.move()
        self.paddle2.move()
    
    def draw(self):
        self.screen.fill(self.background_color) 
        self.update()
        self.ball.draw()
        self.paddle1.draw()
        self.paddle2.draw()
        pygame.display.flip()
    
    def play(self):
        while not self.close_clicked:
            self.handle_event()
            if self.ball.paddle1_point <= 10 and self.ball.paddle2_point <= 10:
                self.draw()
                self.game_clock.tick(self.FPS)        
    
    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_clicked = True        
        
class Paddle1:
    def __init__(self, screen, paddle1_left, paddle1_top, paddle1_width, paddle1_height):
        self.screen = screen
        self.color = pygame.Color("white")
        self.left = paddle1_left
        self.top = paddle1_top
        self.width = paddle1_width
        self.height = paddle1_height
        self.speed = 10
        
    def move(self):
        key = pygame.key.get_pressed()
        if self.top - self.speed >= 0:
            if key[pygame.K_q]:
                self.top = self.top - self.speed
        if self.top + self.height + self.speed <= 400:   
            if key[pygame.K_a]:
                self.top = self.top + self.speed            
    
    def draw(self):      
        pygame.draw.rect(self.screen, self.color, (self.left, self.top, self.width, self.height))        

class Paddle2:
    def __init__(self, screen, paddle2_left, paddle2_top, paddle2_width, paddle2_height):
        self.screen = screen
        self.color = pygame.Color("white")
        self.left = paddle2_left
        self.top = paddle2_top
        self.width = paddle2_width
        self.height = paddle2_height
        self.speed = 10        
        
    def move(self):
        key = pygame.key.get_pressed()
        if self.top - self.speed >= 0:
            if key[pygame.K_p]:
                self.top = self.top - self.speed
        if self.top + self.height + self.speed <= 400:   
            if key[pygame.K_l]:
                self.top = self.top + self.speed                            
           
    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.left, self.top, self.width, self.height))        

class Ball:
    def __init__(self, screen, ball_center, ball_velocity, ball_radius, paddle1_point, paddle2_point):
        self.screen = screen
        self.color = pygame.Color("white")
        self.center = ball_center
        self.velocity = ball_velocity
        self.radius = ball_radius
        self.paddle1_point = paddle1_point
        self.paddle2_point = paddle2_point        
        
    def move(self):
        self.center[0] = self.center[0] + self.velocity[0]
        self.center[1] = self.center[1] + self.velocity[1]
        if self.center[0] - self.radius <= 0:
            self.velocity[0] = -self.velocity[0]
            self.paddle2_point = self.paddle2_point + 1
        if self.center[0] + self.radius >= 500:
            self.velocity[0] = -self.velocity[0]
            self.paddle1_point = self.paddle1_point + 1   
        if self.center[1] - self.radius <= 0:
            self.velocity[1] = -self.velocity[1]
        if self.center[1] + self.radius >= 400:
            self.velocity[1] = -self.velocity[1]     
    
    def draw(self):
        scores_font = pygame.font.SysFont("", 50)
        scores1 = scores_font.render(str(self.paddle1_point), True, self.color)
        self.screen.blit(scores1, (0, 0))          
        scores2 = scores_font.render(str(self.paddle2_point), True, self.color)
        self.screen.blit(scores2, (465, 0))         
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)

main()