from wifi_qrcode_generator import wifi_qrcode

qr_code = wifi_qrcode("Gracious", hidden=False, authentication_type="WPA", password='password')

qr_code_img = qr_code.make_image()
qr_code_img.save("wifi_qrcode_img.png")
""" import webbrowser

url_lists = [
    "https://www.google.com",
    "https://www.yahoo.com",
    "https://www.bing.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.github.com",
]

for url in url_lists:
    webbrowser.open(url) """
