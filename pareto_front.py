from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

m = [[5.5, 4 ,4.5],
     [ 1 , 8 , 0 ],
     [3.5, 4 ,5.5],
     [ 3 , 2 , 1 ],
     [ 5 , 1 , 4 ],
     [2.5, 3 , 3 ],
     [ 4 , 6 ,2.5],
     [ 6 , 0 ,0.5]]

front_de_pareto = []
rang = []

def pareto(m,f1,f2,f3) :

	i = 0
	while i < len(m) :
		j = 0
		var = True
		while j < len(m) and var == True :

			if i == j :
				if i < len(m)-1:
					j += 1
				else :
					break

			if (dominate(m[i],m[j],f1,f2,f3) ) :
				j += 1
			else :
				var = False
			

		if var == True :
			front_de_pareto.append(m[i])
			rang.append(i+1)
		i += 1
	print('front de pareto est : {}'.format(rang))
	return(front_de_pareto)



def dominate(row1,row2,minOrMax1,minOrMax2,minOrMax3) :

	if minOrMax1=='min' and minOrMax2=='min' and minOrMax3=='min' :
		if(row1[0] <= row2[0] or row1[1] <= row2[1] or row1[2] <= row2[2]) :
			return True 
		else:
			return False
	elif minOrMax1=='min' and minOrMax2=='min' and minOrMax3=='max' :
		if(row1[0] <= row2[0] or row1[1] <= row2[1] or row1[2] >= row2[2]) :
			return True 
		else:
			return False
	elif minOrMax1=='min' and minOrMax2=='max' and minOrMax3=='min' :
		if(row1[0] <= row2[0] or row1[1] >= row2[1] or row1[2] <= row2[2]) :
			return True 
		else:
			return False
	elif minOrMax1=='min' and minOrMax2=='max' and minOrMax3=='max' :
		if(row1[0] <= row2[0] or row1[1] >= row2[1] or row1[2] >= row2[2]) :
			return True 
		else:
			return False

	elif minOrMax1=='max' and minOrMax2=='min' and minOrMax3=='min' :
		if(row1[0] >= row2[0] or row1[1] <= row2[1] or row1[2] <= row2[2]) :
			return True 
		else:
			return False
	elif minOrMax1=='max' and minOrMax2=='min' and minOrMax3=='max' :
		if(row1[0] >= row2[0] or row1[1] <= row2[1] or row1[2] >= row2[2]) :
			return True 
		else:
			return False
	elif minOrMax1=='max' and minOrMax2=='max' and minOrMax3=='min' :
		if(row1[0] >= row2[0] or row1[1] >= row2[1] or row1[2] <= row2[2]) :
			return True 
		else:
			return False
	elif minOrMax1=='max' and minOrMax2=='max' and minOrMax3=='max' :
		if(row1[0] >= row2[0] or row1[1] >= row2[1] or row1[2] >= row2[2]) :
			return True 
		else:
			return False
	

pareto(m,'min','min','min')


Xs,Ys,Zs = [],[],[]
xs,ys,zs = [],[],[]
print("*"*8 + " front de pareto " + ("*"*8))
for p in m :
    if p in front_de_pareto :
    	print(p)
    	Xs.append(p[0])
    	Ys.append(p[1])
    	Zs.append(p[2])
    else :
    	xs.append(p[0])
    	ys.append(p[1])
    	zs.append(p[2])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



ax.scatter(Xs, Ys, Zs, c='r', marker='o',s=25)
ax.scatter(xs, ys, zs, c='b', marker='o',s=25)
ax.plot_trisurf(Xs, Ys, Zs, linewidth=0.1, antialiased=True,color=(0,0,0,0.5), edgecolor='Gray')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()



