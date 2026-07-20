import qrcode
from PIL import Image,ImageDraw,ImageFont

url = input ("Enter the URL: ").strip() #avoid whitespaces
file_path = r"C:\Users\Rutuja\OneDrive\MyProject\\1_qrcode.png"

qr = qrcode.QRCode() #QR library
qr.add_data(url)

img = qr.make_image()

img = img.convert("RGB")
#create white background with extra space below
new_img=Image.new("RGB",(img.width,img.height+120),"white")
new_img.paste(img,(0,0))

#add text in center(2lines)
draw = ImageDraw.Draw(new_img)
font=ImageFont.truetype("arial.ttf",30)

text="Scan QR Code\nTo View Menu"
draw.multiline_text(
    (img.width//2,img.height+60), #center position
    text,
    fill="black",
    font=font,
    align="center",
    anchor="mm" #mm means middle-middle 
    )

#save and show msg
img=new_img
img.save(file_path)

print("QR code was generated!")