from composition import *
import os
import twitter_scraper
video1 = Composition("saxophone.mp4", ["element_sample.png", "element_sample.png"], "Invitation to Dance.mp3")
video1.get_properties()
print(video1.bgm)
# video1.set_bgm("End of the Line.mp3")
# print(video1.bgm)
# video1.gen_video()
# gen_sample()

twitter_scraper.search()
