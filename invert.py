from PIL import Image

import numpy as np


resim = Image.open('C:/Users/gulse/OneDrive/Masaüstü/odev.jpg')
img_dizi = np.array(resim)
maxDeger = 255
img_dizi = maxDeger - img_dizi
ters_img = Image.fromarray(img_dizi)
ters_img.save('C:/Users/gulse/OneDrive/Masaüstü/odev1.jpg')
