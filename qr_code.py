import qrcode as qr

a = input('Get Me Your Name ')
b = input('Get Me Your Age ')
c = input('Get Me Your Number ')

d = a + ',' + b + ',' + c

img = qr.make(d)
img.save("a.png")