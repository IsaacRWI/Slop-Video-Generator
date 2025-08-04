from moviepy import *

class Composition:
    def __init__(self, bg, elm_list, bgm = None):
        self.bg = bg
        self.elm_list = elm_list
        self.bgm = bgm
        self.elm1 = elm_list[0]
        self.elm2 = elm_list[1]

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

    def gen_sample(self):
        bg = ImageClip("frame_sample.png").with_start(0).with_duration(2)
        elm1 = ImageClip("element_sample.png").with_start(0).with_duration(2).with_position("center", 1)
        elm2 = ImageClip("element_sample.png").with_start(0).with_duration(2).with_position("center", 1900)
        final_clip = CompositeVideoClip([bg, elm1, elm2])
        final_clip.write_videofile("sample.mp4", 24)

    def gen_video(self):
        bg_clip = VideoFileClip(self.bg).with_start(0).with_duration(5).resized(height=1080)
        bgm_audio = AudioFileClip(self.bgm).with_duration(5)
        # test1 = ImageClip(self.elm1).with_position("center", "top").with_start(0).with_duration(2).resized(height=700)
        elm1 = ImageClip(self.elm1).resized(height = 700).with_position(("center", 20)).with_start(0).with_duration(5)
        elm2 = ImageClip(self.elm2).resized(height = 300).with_position(("center", 400)).with_start(0).with_duration(5)
        final_clip = CompositeVideoClip([bg_clip,elm1, elm2])
        final_clip.audio = CompositeAudioClip([bgm_audio])
        final_clip.write_videofile("test2.mp4")
