# Creating a qr for my github profile
# Install qrgenerator library
# pip install qrcode Image
import qrcode


def qrcode_generator(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="white")
    img.save("qrimg.png")


qrcode_generator("https://github.com/PaulPrabahar")
