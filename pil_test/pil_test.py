#!/usr/bin/python

import Image
import ImageFilter
import ImageEnhance
image=Image.open('capcha.gif')
#im=image.filter(ImageFilter.MedianFilter())
#enhancer = ImageEnhance.Contrast(im)
#im = enhancer.enhance(2)
#im = im.convert('1')
#image.show()
print image.size
h,w = image.size
print image.format
print image.mode
print image.palette
small_image=image.resize((h/2,w/2))
pil=small_image.load()
print pil[2,3]
print image.info

for i in range(w/2):
    for j in range(h/2):
        v=pil[j,i]
        if v==0:
            print '?',
        else:
            #print pil[j,i],
            print '.',
    print '\n'

