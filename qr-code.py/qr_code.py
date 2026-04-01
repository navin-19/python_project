try:
    import qrcode
except ModuleNotFoundError:
    raise SystemExit("Install the dependency first: pip install qrcode[pil]")

URL = "https://youtu.be/Kwa59h7HQzM?si=9welUZNdwkiEF0L9"
OUTPUT_FILE = "song.png"

qr_image = qrcode.make(URL)
qr_image.save(OUTPUT_FILE)

print(f"Created {OUTPUT_FILE}")
