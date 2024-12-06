import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PONG GAME"

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.05)
        self.change_x = 2
        self.change_y = 0

    def update(self, delta):
        self.center_x += self.change_x * delta * 60
        self.center_y += self.change_y



class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.2)


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        # Cписок спрайтов
        self.sprite_list = arcade.SpriteList()
        self.bar = Bar()
        self.ball = Ball()
        self.sprite_list.append(self.bar)
        self.sprite_list.append(self.ball)
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.sprite_list.draw()

    def on_update(self, delta):
        print(f"Ball position: {self.ball.center_x}")
        self.sprite_list.update()



if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()