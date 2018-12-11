from base64 import b64encode

from PIL import Image

with open(f'./static/img/outline.png', 'rb') as image:
    elo = b64encode(image.read())

from base64 import b64encode
from io import BytesIO

buff = BytesIO()
img1 = open(f'./static/img/outline.png', 'rb')
img2 = Image.open(f'./static/img/outline.png', 'r')
img2.save(buff, format='PNG')
# buff.seek(0)

img1_b = b64encode(img1.read())
img2_b = b64encode(buff.getvalue())

print('1', img1_b, '\n\n\n')

print()
print('2', img2_b, '\n\n\n')

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
