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
