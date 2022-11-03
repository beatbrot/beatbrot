#! /bin/bash
manim scene.py -o anim.gif --format=gif -t
mkdir frame
ffmpeg -i media/videos/scene/600p25/anim.gif frame/frame%04d.png
gifski -o anim.gif --width 600 frame/frame*.png