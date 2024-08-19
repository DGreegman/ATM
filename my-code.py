import qrcode
from PIL import Image

data = input("Enter any thing you want")
qr = qrcode.QRCode(version=2, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill="blue", back_color="yellow")

image.save("qrcode.jpg")
Image.open("qrcode.jpg")
print("QR code generated successfully")