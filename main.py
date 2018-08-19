import cv2

import urllib.request as req

url = 'http://uta.pw/gazoubbs/attach/12-hama.jpg'
local = 'hama.jpg'
req.urlretrieve(url,local)

