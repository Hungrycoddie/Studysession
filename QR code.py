import pyqrcode
big_code = pyqrcode.create('0987654321', error='L', version=27, mode='binary')
big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
big_code.show()
print(big_code.show().terminal(quiet_zone=1))   

#reffence https://pypi.org/project/PyQRCode/
# >>> big_code = pyqrcode.create('0987654321', error='L', version=27, mode='binary')
#>>> big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
#>>> big_code.show()

