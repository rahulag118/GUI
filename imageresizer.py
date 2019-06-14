from PIL import Image
img=Image.open('2.jpg')
size=(1366,768)
img.thumbnail(size)
img.save('2_730.jpg')
