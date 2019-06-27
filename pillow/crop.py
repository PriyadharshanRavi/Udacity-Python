from PIL import Image

img = Image.open("stark.jpg")
#img.rotate(45).show()
area = (100,100,500,500)
cropped = img.crop(area)
print(img.size)
print(img.format)
img.show()
cropped.show()