# install all the libraries needed.
# Create a function that collects a text and converts t to a qr code.
# save the qr as an image
# Run the function.
import qrcode

def generate_qrcode(text):
   
   qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        
   )

   qr.add_data(text)
   qr.make(fit=True)
   img = qr.make_image(fill_color="black", back_color="white")
   img.save("fdsadsaf.png")

url = input("Enter your url: ")
generate_qrcode(url)