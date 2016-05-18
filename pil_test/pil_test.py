#!/usr/bin/python

import Image
image=Image.open('capcha.gif')
print image.size
h,w = image.size
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

