import pyqrcode

# Longer text data
data2 = "This is a longer string of text to demonstrate a more complex QR code pattern. It contains more information."

qr_code2 = pyqrcode.create(data2)
qr_code2.png('long_text_qr.png', scale=7)
qr_code2.svg('long_text_qr.svg', scale=7)

print("QR code 2 (long text) generated as long_text_qr.png and long_text_qr.svg")