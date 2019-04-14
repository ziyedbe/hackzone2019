import glob
import subprocess
for filename in glob.glob('Crypto_/*.key'):
    f = open(filename,"r")
    content=f.readlines()
    n=int(content[0].split(" ")[2],16)
    for filename1 in glob.glob('Crypto_/*.key'):
        g = open(filename1,"r")
        content1=g.readlines()
        n1=int(content1[0].split(" ")[2],16)
        if(n==n1 and filename!=filename1):
            print(filename+":"+filename1)



