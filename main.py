import random

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"
MOVEMENT_SPEED = 5
class Player(arcade.Sprite):
    """ Player Class """
    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1
class MyGame(arcade.Window):
    score = 0
    check = "Safe"
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.GRAY)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        self.wall_list = arcade.SpriteList()
        for x in range(128, SCREEN_WIDTH, 196):
            for y in range(128, SCREEN_HEIGHT, 196):
                wall = arcade.Sprite("building.png",.3)
                wall.center_x = x
                wall.center_y = y
                # wall.angle = 45
                self.wall_list.append(wall)
        self.player_sprite = arcade.Sprite("taxi.png")
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite.scale = .25
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        #Spawns people and makes list
        self.person = arcade.Sprite("person.png")
        self.person.scale = .2
        self.person.center_x = random.randrange(SCREEN_WIDTH)
        self.person.center_y = random.randrange(SCREEN_HEIGHT)
        #Spawns target
        self.target = arcade.Sprite("target.png")
        self.target.scale = .5
        self.target.center_x = random.randrange(SCREEN_WIDTH)
        self.target.center_y = random.randrange(SCREEN_HEIGHT)
        color_list = ["BLUE","RED"]

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.player_sprite.draw()
        self.person.draw()
        self.target.draw()
        self.wall_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        checktext = f"Check: {self.check}"
        arcade.draw_text(checktext, 10, 30, arcade.color.BLACK, 14)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player_list.update()
        wall_hit = arcade.check_for_collision_with_list(self.player_sprite,self.wall_list)
        for x in wall_hit:
            x.kill()
            self.check = "Hit"
            self.setup()
        if arcade.check_for_collision(self.player_sprite,self.person):
            self.person.kill()
            self.check = "Person"
        if arcade.check_for_collision(self.player_sprite,self.target):
            if self.check == "Person":
                self.check = "Complete"

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
            self.player_sprite.angle = 180
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
            self.player_sprite.angle = 0
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
            self.player_sprite.angle = 270
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
            self.player_sprite.angle = 90

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()