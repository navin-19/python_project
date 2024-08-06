import qrcode
img=qrcode.make("https://youtu.be/Wq-S2FQAh_w?si=w6cee4E7WG7z0yBz")
img.save("fav_song.jpg")
print("created")