from composition import Composition
video1 = Composition("saxophone.mp4", ["element_sample.png", "element_sample.png"], "Invitation to Dance.mp3")
video1.get_properties()
print(video1.bgm)
# video1.set_bgm("End of the Line.mp3")
# print(video1.bgm)
# video1.gen_video()
video1.gen_sample()