import qrcode

# Short URL data
data1 = "go.short/abc"

qr1 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=12,
    border=4,
)
qr1.add_data(data1)
qr1.make(fit=True)

img1 = qr1.make_image(fill_color="navy", back_color="lightcyan")
img1.save("short_url_qr.png")

print("QR code 1 (short URL) generated as short_url_qr.png")