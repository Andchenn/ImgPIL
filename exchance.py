from PIL import Image

image_file = Image.open("222.jpg")
image_file = image_file.convert('1')
image_file.save('result.jpg')
