from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.jpg')

print(img)
print(img.format)
print(img.size)
print(img.mode)

# filtered_img = img.filter(ImageFilter.BLUR) # SHARP
# filtered_img.save("./images/blur.png", "png")

filtered_img = img.convert("L")
# filtered_img.save("./images/gray.png", "png")
# filtered_img.show()

# rotate
# crocked = filtered_img.rotate(90)
# crocked.save("./images/crocked.png", "png")

# resize
resze = filtered_img.resize((300, 300))
resze.save("./images/resize.png", "png")