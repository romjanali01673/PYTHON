#import qrcode as qr 
#img = qr.make("https://www.facebook.com/profile.php?id=100037207939401")
#img.save("python_ bangla_tutoral.png")

import qrcode 
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 50,
    border = 5,
)

qr.add_data("https://www.facebook.com/profile.php?id=100037207939401")
qr.make (fit = True)
img = qr.make_image(fill_color="red", back_color = "white")
img.save( ' fb.JPEG ') 


