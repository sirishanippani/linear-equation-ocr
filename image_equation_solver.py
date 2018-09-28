''' A python program which can read an image containing linear equation convert it to text and solve that equation.
This project is in its priliminary stage of developement,it has some flaws although it serves the basic purpose.'''

#all imports at a place
import re
from PIL import Image
import pytesseract
import cv2
import os
import numpy as np
import argparse

#reading image and converting it to text
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",type=str,help="path to input image")
args=vars(ap.parse_args())
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image",image)
cv2.imshow("Gray", gray)

gray = cv2.medianBlur(gray, 3)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

#solving the converted equations
a=text
q=""
nos=''
for i in a:
    if i.isalpha():
        q = " ".join([q, i])

    if i.isdigit():
        nos = re.findall('-?\d+\.?\d*', a)

    #if a[c] == '-' and a[c + 1].isalpha():
        #nos + digi
    #c = c + 1
print(q)
l=int(len(q) / 4)
print(nos)

A=[]
b=[]

if(l == 2):
    A = np.array([[int(nos[0]), int(nos[1])], [int(nos[3]), int(nos[4])]])
    b = np.array([int(nos[2]), int(nos[5])])


if(l == 3):
    A = np.array([[int(nos[0]), int(nos[1]), int(nos[2])], [int(nos[4]), int(nos[5]), int(nos[6])], [int(nos[8]), int(nos[9]), int(nos[10])]])
    b = np.array([int(nos[3]), int(nos[7]), int(nos[11])])


if(l == 4):
    A = np.array([[int(nos[0]), int(nos[1]), int(nos[2]), int(nos[3])], [int(nos[5]), int(nos[6]), int(nos[7]), int(nos[8])], [int(nos[10]), int(nos[11]), int(nos[12]), int(nos[13])], [int(nos[15]), int(nos[16]), int(nos[17]), int(nos[18])]])
    b = np.array([int(nos[4]), int(nos[9]), int(nos[14]), int(nos[19])])


if(l == 5):
    A = np.array([[int(nos[0]), int(nos[1]), int(nos[2]), int(nos[3]), int(nos[4])], [int(nos[6]), int(nos[7]), int(nos[8]), int(nos[9]), int(nos[10])], [int(nos[12]), int(nos[13]), int(nos[14]), int(nos[15]), int(nos[16])], [int(nos[18]), int(nos[19]), int(nos[20]), int(nos[21]), int(nos[22])], [int(nos[24]), int(nos[25]), int(nos[26]), int(nos[27]), int(nos[28])] ])
    b = np.array([int(nos[5]), int(nos[11]), int(nos[17]), int(nos[23]), int(nos[29])])

z = np.linalg.solve(A,b)
print(z)

#output image
cv2.imshow("Output", gray)
cv2.waitKey(0)
