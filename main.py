from ursina import *

app = Ursina()

player = Sprite('player.png')
def update():
    player.y += held_keys['w'] * time.dt
    player.x -= held_keys['a'] * time.dt
    player.y -= held_keys['s'] * time.dt
    player.x += held_keys['d'] * time.dt



app.run()
