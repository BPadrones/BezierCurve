import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

#plt.plot(xpoints, ypoints)
#plt.show()

def Lerp(coord0,coord1,seg = 100):
	x_points = [ ]
	y_points = []
	spacing = np.linspace(0,1,seg)
	for space in spacing: 
		x_points.append((1-space)*coord0[0]+space*coord1[0])
		y_points.append((1-space)*coord0[1]+space*coord1[1])
	return x_points,y_points

firstX,firstY = Lerp([1,1],[3,3])
secondX,secondY = Lerp([3,3],[5,1])

ultimate_x = []
ultimate_y = []
for every in range(0,100):
	temp_x,temp_y = Lerp([firstX[every],firstY[every]],[secondX[every],secondY[every]])
	ultimate_x.append(temp_x[every])
	ultimate_y.append(temp_y[every])




plt.plot(ultimate_x,ultimate_y)
plt.show()

'''
def Newlerp(x_points,Y_points, seg = 10):
	xreturn = []
	yreturn = []
	spacing = np.linspace(0,1,seg)
	if len(x_points) != len(Y_points):
		raise ValueError("Arrays Do not match!")
	else:
		for space in spacing:
			xreturn.append((1-space)*x_points[0]+space*x_points[1])
			yreturn.append((1-space)*Y_points[0]+space*Y_points[1])
		return xreturn,yreturn
'''



