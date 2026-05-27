import qrcode
import image
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data = "https://youtu.be/kWkMjYPbLeE?si=MVEBbC5PP8r9kBl4"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("ManojManu.png")

#generting QR code for a website link
#import qrcode
#data = "https://www.instagram.com/gagana_ag/"  
#img = qrcode.make(data)
#img.save("ManojManu.png")
#generting QR code 