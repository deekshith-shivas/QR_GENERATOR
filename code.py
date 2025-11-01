import qrcode

# Data to encode
data = "https://www.python.org"

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill="black", back_color="white")
img.save("example_qr.png")

print("QR code generate!")
