from PIL import Image
from PIL import ImageFilter


blur = Image.open("blur.jpg")
bw = blur.convert("L")
blur = blur.filter(ImageFilter.BLUR)
detail = blur.filter(ImageFilter.DETAIL)
edges = blur.filter(ImageFilter.FIND_EDGES)

bw.show()
blur.show()
detail.show()
edges.show()