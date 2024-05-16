import os
import qrcode

def generate_qrcode(text, filename="qrcode.png", fill_color="black", back_color="white"):
    """
    Generates a QR code from the given text and saves it as an image.
    
    Parameters:
    text (str): The text to encode in the QR code.
    filename (str): The name of the file to save the QR code image.
    fill_color (str): The color of the QR code.
    back_color (str): The background color of the QR code.
    """
    # Check if the filename ends with .png or .jpg, otherwise append .png
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
        filename += '.png'
    
    # Initialize the QRCode object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(text)
    qr.make(fit=True)

    # Create the image of the QR code
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Save the image to a file
    img.save(filename)
    print(f"QR code saved as {filename}")

def get_user_input():
    """
    Collects user input for the text to encode and file name.
    
    Returns:
    tuple: A tuple containing the text to encode and the file name.
    """
    text = input("Enter the text to encode: ")
    filename = input("Enter the filename (default 'qrcode.png'): ") or "qrcode.png"
    return text, filename

if __name__ == "__main__":
    # Get input from the user
    text, filename = get_user_input()
    
    # Generate and save the QR code
    generate_qrcode(text, filename)
