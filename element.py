from moviepy import *

class Element:
    def __init__(self, media, pos):
        self.media = media
        position = {"up" : (540, 700), "down" : (540, 1400)}
        self.pos = position[pos]