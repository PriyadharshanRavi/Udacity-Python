from PIL import Image

color = Image.open("color.jpeg")
square_color = color.resize((500,500))
flip_color = color.transpose(Image.FLIP_LEFT_RIGHT)
spin_color = color.transpose(Image.ROTATE_180)


color.show()
square_color.show()
flip_color.show()
spin_color.show()