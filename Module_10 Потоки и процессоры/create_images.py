from PIL import Image

image = Image.open('image.jpg')
for i in range(1, 1001):
    image.save(f"Images\\img_{i}.jpg")