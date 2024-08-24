#pip install pyqrcode

import pyqrcode 
from pyqrcode import QRCode 
  
# String which represents the QR code 
# Attaching my linkedin profile link here to generate QR.
s = "https://www.linkedin.com/in/mradul-malviya-3b8a7418b/?trk=opento_sprofile_details"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file name "myqr.png" 
#Scalable Vector Graphics
url.svg("mylinkedin.svg", scale = 8) 
