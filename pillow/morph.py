from PIL import Image

jon = Image.open("jonsnow.jpg")
boss = Image.open("bossreplace.png")

area = (250,250)

jon.paste(boss, area)

jon.show()