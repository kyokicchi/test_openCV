
# coding: utf-8

# In[4]:


import cv2

import urllib.request as req

url = 'http://uta.pw/gazoubbs/attach/12-hama.jpg'
local = 'hama.jpg'
req.urlretrieve(url,local)


# In[7]:


img = cv2.imread('hama.jpg')
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('hama.gray.jpg',gray_image)


# In[8]:


sobel_image = cv2.Sobel(img, cv2.CV_32F,1,0,ksize=5)
cv2.imwrite('hama-sobel.jpg',sobel_image)


# In[9]:


canny_image = cv2.Canny(img,30,200)
cv2.imwrite('hama-canny1.jpg',canny_image)
canny_image = 256 - canny_image
cv2.imwrite('hama-canny2.jpg',canny_image)


# In[10]:


reverse_image = 256 - img
cv2.imwrite('reverse.jpg',reverse_image)

