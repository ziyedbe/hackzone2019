
from PIL import Image
from pyzbar.pyzbar import decode
ph=""


for i in range(0,50):
    filename= open('frames/frame_'+str(i).zfill(2)+'_delay-0.01s.gif')
    data = decode(Image.open(filename))
    ph+=data[0][0]
    
print(ph)
