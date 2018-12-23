import cv2 as cv
import numpy as np


def image_overlay(back, fore, x, y):
    rows, cols, channels = fore.shape
    trans_indices = fore[..., 3] != 0  # Where not transparent
    overlay_copy = back[y:y + rows, x:x + cols]
    overlay_copy[trans_indices] = fore[trans_indices]
    back[y:y + rows, x:x + cols] = overlay_copy


# test
background = np.zeros((1000, 1000, 4), np.uint8)
background[:] = (127, 127, 127, 1)
overlay = cv.imread('outline.png', cv.IMREAD_UNCHANGED)
print(overlay)
image_overlay(background, overlay, 5, 5)

from PIL import Image

background = Image.open("outline.png")
overlay = Image.open("cloth_indian.png")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")


Image.alpha_composite(background, overlay).save("result.png")