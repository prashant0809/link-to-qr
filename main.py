
#please install this library before code
#pip install qrcode[pil]
import qrcode

# Generate QR code
qr = qrcode.make("https://www.youtube.com/watch?v=10631WQuLYo")

# Save as an image
qr.save("youtube_qqr.png")

print("QR Code generated and saved as youtube_qr.png")
