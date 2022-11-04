import os
from manim import *
from PIL import Image
import numpy as np

import requests

dark_mode = "DARK" in os.environ.keys()
greetings = [s.strip() for s in open("greetings.txt", mode="r", encoding="UTF-8").readlines()]


class EmojiImageMobject(ImageMobject):
    def __init__(self, **kwargs):
        url = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/346/waving-hand_1f44b.png"
        im = Image.open(requests.get(url, stream=True).raw)
        emoji_img = np.array(im.convert("RGBA"))
        ImageMobject.__init__(self, emoji_img, **kwargs)


class BaseAnim(Scene):
    BASE_SCALE = 3.8

    def construct(self):
        x = self.build_text(greetings[0])
        self.add(*x)
        self.wiggle(x)

        for g in greetings[1:]:
            x = self.replace(x, g)

        x = self.replace(x, greetings[0])

    def replace(self, old, new_text):
        new = self.build_text(new_text)
        self.transform(old, new)
        return new

    def wiggle(self, state):
        self.play(Wiggle(state[1]))
        self.wait(2.3)

    def transform(self, old, new):
        old_len = len(old[2])
        new_len = len(new[2])
        anims = [
            Transform(old[0], new[0]),
            Transform(old[1], new[1]),
            FadeOut(old[2][slice(old_len - 8)], shift=UP),
            FadeIn(new[2][slice(new_len - 8)], shift=UP),
            Transform(old[2][slice(old_len - 8, old_len)],
                      new[2][slice(new_len - 8, new_len)]),
        ]
        self.play(AnimationGroup(*anims))
        self.clear()
        self.add(*new)
        self.wait(2.3)

    def build_text(self, text):
        intro = Text("<", color=self.text_color(), font="Montserrat",
                     weight="ULTRAHEAVY").scale(self.BASE_SCALE)
        em = EmojiImageMobject().scale(self.BASE_SCALE * 1.2)
        rest = Text(f"{text}, World/>", font="Montserrat",
                    color=self.text_color(), weight="ULTRAHEAVY").scale(self.BASE_SCALE)
        Group(intro, em, rest).arrange(RIGHT)
        return [intro, em, rest]

    def text_color(self):
        return "black"

class DarkModeAnim(BaseAnim):

    def text_color(self):
        return "white"
