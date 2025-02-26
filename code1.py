import cv2
import os
import string
img =cv2.imread("nature.jpg")
msg =input("Enter secret message.")
password=input("Enter a passwod.")
d={} 
c={}
for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)
m=0
n=0
z=0
for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3
cv2.imwrite("encryptedimage.jpg",img)
os.system("start encryptedimage.jpg")
message=""
n=0
m=0
z=0
pas=input("Enter password for decryption")
if password==pas:
    for i in range(len(msg)):
        message=message+c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1)%3
    print("decrytion message:",message)
else:
    print("YOU ARE NOT Auth")
