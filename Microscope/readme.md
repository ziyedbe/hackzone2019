# Microscope

Description : we were given a website with a lot of colored pixels

## Walkthrough

Looking through the website, i found nothing but a bunch of colored pixels.
So I downloaded the source code of the page using curl

```bash
curl http://149.56.110.180:1234/ > output.txt
```

I looked through the output, i figured that i could find something extracting the hexadecimal values for colors.

So i wrote this script to extract the values and covert them to a binary file.

```python
import binascii

## This part of the code will extract the hexadecimal
## values from the file 
f=open("output.txt","r")
content =f.readlines()
text = content[8].split('"')
h = ""
for i in range(1,len(text),2):
    h+=text[i][1:]

# Here we'll convert the hexadecimal string we got to 
# a binary file
output = open("output","ab")
hb=binascii.a2b_hex(h)
output.write(hb)
output.close()

```

output

<p align="center">
<img src="output"/>
</p>

It's a gif containing multiple QR codes.

Using an online tool I converted this gif to frames.

I got 50 frame from it.

So i wrote a script to scan the QR codes and extract data from them

```python

from PIL import Image
from pyzbar.pyzbar import decode
ph=""


for i in range(0,50):
    filename= open('frames/frame_'+str(i).zfill(2)+'_delay-0.01s.gif')
    data = decode(Image.open(filename))
    ph+=data[0][0]
    
print(ph)

```
## Flag

HZVII{7h3_0r161n4l_qr_c0d3_w45_d3v3l0p3d_1n_1994.}

