import sys
import os
from PIL import Image, ImageFilter

# first steps

# img = Image.open('./images/pikachu.jpg')

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)

# filtered_img = img.filter(ImageFilter.BLUR) # SHARP
# filtered_img.save("./out/blur.png", "png")

# filtered_img = img.convert("L")
# filtered_img.save("./out/gray.png", "png")
# filtered_img.show()

# rotate
# crocked = filtered_img.rotate(90)
# crocked.save("./out/crocked.png", "png")

# resize
# resze = filtered_img.resize((300, 300))
# resze.save(""./out/resize.png", "png"", "png")


# img = Image.open('./out/astro.jpg')
#
# # new_img = img.resize((400, 200))
# img.thumbnail((400, 600))
# img.save('./out/thumbnail.jpg')

# second steps
path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')