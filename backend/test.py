from base64 import b64encode

from PIL import Image

from base64 import b64encode

from io import BytesIO, StringIO


import numpy as np
from PIL import Image

im = open(f'./static/img/outline.png', 'rb')
data = np.array(im)

buff = StringIO()
img1 = open(f'./static/img/outline.png', 'rb')
img2 = Image.open(f'./static/img/outline.png')
img2.save('./static/img/elo.png', format='PNG')

# img2.save(buff, format='PNG')
# buff.seek(0)
img2 = open(f'./static/img/elo.png', 'rb')
img1_b = b64encode(img1.read())
img2_b = b64encode(img2.read())

print('1', img1_b, '\n\n\n')

print()
print('2', img2_b, '\n\n\n')




im = cv.imread('outline.png', cv.IMREAD_UNCHANGED)
cv.imwrite('output.png', im, [cv.IMWRITE_PNG_COMPRESSION, 9])


f1 = open('outline.png', 'rb')
f2 = open('output.png', 'rb')

img1_b = b64encode(f1.read())
img2_b = b64encode(f2.read())

print(img1_b)
print(img2_b)

original = cv.imread("outline.png")
duplicate = cv.imread("output.png")
if original.shape == duplicate.shape:
    print("The images have same size and channels")
    difference = cv.subtract(original, duplicate)
    b, g, r = cv.split(difference)

    if cv.countNonZero(b) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(r) == 0:
        print("The images are completely Equal")

# elo2.save(buff, format='PNG')
# print('mode', elo2.mode)
#
# elo3 = b64encode(buff.getvalue())
#
# file1 = open('normal.txt', 'w')
# file2 = open('unnormal.txt', 'w')
# file1.write(str(elo))
# file2.write(str(elo3))
# file1.close()
# file2.close()
# if elo == elo3:
#     print('siema')
# print(len(elo))
# print(len(elo3))
