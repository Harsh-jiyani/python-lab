from MyQR import myqr

# Phone number data
data3 = "tel:+919876543210"

version, level, qr_name = myqr.generate(
    data3,
    version=1,
    level='M',  # Slightly higher error correction than default
    picture=None,
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='phone_number_qr.png',
    save_dir=None
)

print(f"QR code 3 (phone number) generated as {qr_name}")