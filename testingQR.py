import pyqrcode
from pyqrcode import QRCode

s = input("Enter the url: ")
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png("myqr.png", scale = 6)