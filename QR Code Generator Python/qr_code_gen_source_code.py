import qrcode
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr():
    # Get the user input data
    data = entry.get()
    
    if not data:
        messagebox.showwarning("Input Error", "Please enter some data to generate QR code")
        return

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save("qrcode.png")

    # Display the QR code in the GUI
    img = Image.open("qrcode.png")
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img
    messagebox.showinfo("Success", "QR Code generated and saved as qrcode.png")

# Create the main window
root = Tk()
root.title("QR Code Generator")

# Create a label and entry for user input
label = Label(root, text="Enter data:")
label.pack(pady=10)

entry = Entry(root, width=40)
entry.pack(pady=10)

# Create a button to generate the QR code
button = Button(root, text="Generate QR Code", command=generate_qr)
button.pack(pady=10)

# Create a label to display the generated QR code
qr_label = Label(root)
qr_label.pack(pady=10)

# Run the main event loop
root.mainloop()
