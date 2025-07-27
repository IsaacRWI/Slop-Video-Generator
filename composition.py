from moviepy import *

class Composition:
    def __init__(self, bg, elm_list, bgm = None):
        self.bg = bg
        self.elm_list = elm_list
        self.bgm = bgm

    # Alternate method
    """    
    def __init__(self, bg, elm_list, bgm = None):
        self.bg = VideoFileClip(bg)
        self.bgm = AudioFileClip(bgm)
        self.elm1 = ImageClip(elm_list[0])
        self.elm2 = ImageClip(elm_list[1])
    """

    def set_bg(self, bg = None):
        if bg is None:
            pass
        else:
            self.bg = bg

    def set_bgm(self, bgm = None):
        if bgm is None:
            pass
        else:
            self.bgm = bgm

    def get_properties(self):
        print(f"Background Media: {self.bg}")
        print(f"Background Music: {self.bgm}")
        print(f"Featured Elements: {self.elm_list}")

    def gen_layout(self):
        bg_clip = VideoFileClip(self.bg)
        bgm_audio = AudioFileClip(self.bgm)
        elm1 = self.elm_list[0]
        elm2 = self.elm_list[1]
