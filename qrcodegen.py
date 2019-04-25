import pyqrcode

url = pyqrcode.create('http://www.umuzi.org')

url.svg('uca-url.svg', scale=2)

print(url.terminal(quiet_zone=1))

big_code = pyqrcode.create('0987654321', error='L', version=27, mode='binary')
big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
big_code.show()