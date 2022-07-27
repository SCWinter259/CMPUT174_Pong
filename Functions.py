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