import pickle
from ursina import *

app = Ursina()

plums = ["1"]

print ('Buildmine 0.0.1')
player = Sprite('player.png')
cloud = Sprite('cloud.png')
def update():
    player.y += held_keys['w'] * time.dt
    player.x -= held_keys['a'] * time.dt
    player.y -= held_keys['s'] * time.dt
    player.x += held_keys['d'] * time.dt
    cloud.x += time.dt

'''
Hello MadKamel. :)
'''

app.run()
