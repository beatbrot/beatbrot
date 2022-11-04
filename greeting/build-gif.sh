#! /bin/bash
manim scene.py BaseAnim --format=png
manim scene.py DarkModeAnim -t --format=png
gifski -o anim-light.gif --width 600 media/images/scene/BaseAnim*.png
gifski -o anim-dark.gif --width 600 media/images/scene/DarkModeAnim*.png
