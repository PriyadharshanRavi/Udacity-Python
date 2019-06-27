from PIL import Image

color = Image.open("color.jpeg")
rat = Image.open("rat.jpeg")
r1,g1,b1 = color.split()
r2,g2,b2 = rat.split()

new_img = Image.merge("RGB", (r1,g2,b1))
new_img.show()