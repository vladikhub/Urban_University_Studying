import arcade


class Game(arcade.Window):
    def __init__(self, weight, height, title):
        super().__init__(weight, height, title)
        self.ball = Ball()
        self.bar = Bar()
        self.setup()

    def setup(self):
        self.ball.center_x = SCREEN_WEIGHT / 2
        self.ball.center_y = SCREEN_HIGH / 2
        self.bar.center_x = SCREEN_WEIGHT / 2
        self.bar.center_y = SCREEN_HIGH / 5
        
    def on_draw(self):
        self.clear((255, 255, 255))
        self.ball.draw()
        self.bar.draw()

    def update(self, delta_time: float):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.bar.change_x = self.bar.SPEED
        if symbol == arcade.key.LEFT:
            self.bar.change_x = - self.bar.SPEED

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT:
            self.bar.change_x = 0


SCREEN_WEIGHT = 800
SCREEN_HIGH = 600
SCREEN_TITLE = "PingPong"


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__("ball.png", 0.15)
        self.change_x = 5
        self.change_y = 5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right > SCREEN_WEIGHT or self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HIGH or self.bottom <= 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    SPEED = 5
    def __init__(self):
        super().__init__("platform.png", 0.5)
        self.change_x = 0

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WEIGHT:
            self.right = SCREEN_WEIGHT
        if self.left <= 0:
            self.left = 0


if __name__ == "__main__":
    game = Game(SCREEN_WEIGHT, SCREEN_HIGH, SCREEN_TITLE)
    arcade.run()