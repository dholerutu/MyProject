import qrcode

url = input ("Enter the URL: ").strip() #avoid whitespaces
file_path = r"C:\Users\Rutuja\OneDrive\Git_Project\MyProject\\1_qrcode.png"

qr = qrcode.QRCode() #QR library
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR code was generated!")