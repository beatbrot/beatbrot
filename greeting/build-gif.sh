#! /bin/bash
manim scene.py -o anim.mp4
mkdir frame
ffmpeg -i media/videos/scene/300p25/anim.mp4 frame/frame%04d.png
gifski -o anim.gif --width 600 frame/frame*.png