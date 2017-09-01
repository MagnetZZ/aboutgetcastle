# -*- coding: utf-8 -*-
import numpy as np
import math

def countcastle(idlist, idnum):
	x0 = idlist[:,0].copy() 
	y0 = idlist[:,1].copy()
	# x0 = [(idlist[i][0]) for i in range(idnum)] # sorted by x 
	# y0 = [(idlist[i][1]) for i in range(idnum)] # Ç³¿½±´
	x1,y1 = x0,y0
	# print(x0.shape)
	# print(idlist[:,0])
	# print(x0[:])
	# print(y0[:])
	x1 = x1[np.argsort(x0)]
	y1 = y1[np.argsort(x0)]
	# print(x1)
	dist =  np.zeros(idnum)
	for i in range(0, idnum):
		dist[i] = math.sqrt((y1[i]-y1[0])**2 + (x1[i]-x1[0])**2)
	dist1 = dist
	dist1 = dist1[np.argsort(dist)] # sorted distance: form 0 to max
	# print(dist1)
	x2 = x1[np.argsort(dist)]  # sort id by distance 
	y2 = y1[np.argsort(dist)]  # sort id by distance
	for i in range(idnum-2, -1, -1):
		print(i)
		# a, b = dist1[i], dist1[i+1]
		# if dist1[i] < dist1[i+1]:
		# 	print('yes')
		print("dist is %f, %f"%(dist1[i],dist1[i+1]))
		vecx0, vecy0 = x2[0] - x2[i], y2[0] - y2[i]
		vecx1, vecy1 = x2[i+1] - x2[i], y2[i+1] - y2[i]
		print('angle:',vecx0*vecx1 + vecy0*vecy1)
		if (vecx0*vecx1 + vecy0*vecy1) <= 0.:
			Ncas = i+1
			return Ncas
		if i == 0:
			return 1 

# def getcastle():
if __name__ == '__main__':
	id_file = open('data.txt','r')
	dd = id_file.readline()
	idnum = int(dd)
	idnum = idnum/2
	print(idnum)
	idlist = np.zeros((idnum,2),dtype=np.int)
	# idlist = [[0,0],[1,0],[2,0],[3,0],[4,0]]
	# idlist = np.array(idlist)
	# print(idlist[1][0])
	for i in range(0, idnum):
		idlist[i][0] = float(id_file.readline())
		idlist[i][1] = float(id_file.readline())
	# print(idlist.shape)
	# print(idlist[1:4,0])
	Ncas = countcastle(idlist, idnum)
	print('The number of castle is %d'%Ncas)

