import cv2
import numpy as np 
import sys 

def colourred(a):
	if len(a)>20:
		return 
	else:
		for x,y in a:
			im[x,y]=[8,0,236]
		return 

def colourblue(a):
	if len(a)>20:
		return 
	else:
		for x,y in a:
			im[x,y]=[237,0,6]
		return 


im = sys.argv[1]

im = cv2.imread(im)
l = []
p = []
foundred = False 
foundblue = False 
count = 0
count2 = 0

for i in range(im.shape[0]):
	for j in range(im.shape[1]):
		pixel = im[i,j]
		if foundred:
			l.append((i,j))
		if foundblue:
			p.append((i,j))
		if (pixel == [8,0,236]).all():
			foundred = not foundred
			count = count + 1
			if count == 2:
				colourred(l)
				count = 0
				l = []
		if (pixel == [237,0,6]).all():
			foundblue = not foundblue
			count2 = count2 + 1
			if count2 == 2:
				colourblue(p)
				count2 = 0
				p = []
for j in range(im.shape[1]):
	for i in range(im.shape[0]):
		pixel = im[i,j]
		if foundred:
			l.append((i,j))
		if foundblue:
			p.append((i,j))
		if (pixel == [8,0,236]).all():
			foundred = not foundred
			count = count + 1
			if count == 2:
				colourred(l)
				count = 0
				l = []
		if (pixel == [237,0,6]).all():
			foundblue = not foundblue
			count2 = count2 + 1
			if count2 == 2:
				colourblue(p)
				count2 = 0
				p = []

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(im,kernel,iterations = 2)
erosion = cv2.erode(dilation,kernel,iterations = 2)


			

