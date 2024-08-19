from PIL import Image 
# Image.open('./ATM/IMG.JPG')
orignal_path = './ATM/IMG.JPG'
resized_path = './ATM/resized_IMG.JPG'

def resize_image(img_path, out_path, width, height):
    image = Image.open(img_path)
    resized_image = image.resize(width, height)
    resized_image.save(out_path)

resize_image(orignal_path, resized_path, 200, 200 )