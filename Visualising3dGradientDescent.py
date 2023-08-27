import numpy as np
import matplotlib.pyplot as plt

"""
We'll try to run gradient descent from 3 different points to 
show how they can then achieve different minimas
"""

def z_func(x,y):
    return np.sin(5*x)*np.cos(5*y)/5

def calc_gradient(x,y):
    return np.cos(5*x)*np.cos(5*y),-np.sin(5*x)*np.sin(5*y)

x=np.arange(-1,1,0.05)
y=np.arange(-1,1,0.05)

X,Y=np.meshgrid(x,y)

Z=z_func(X,Y)

current_pos1=(0.7,0.4,z_func(0.7,0.4))
current_pos2=(0.3,0.8,z_func(0.3,0.8))
current_pos3=(-0.5,0.5,z_func(-0.5,0.5))

learning_rate=0.01

ax=plt.axes(projection="3d",computed_zorder=False)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

for i in range(1000):
    X_grad,Y_grad=calc_gradient(current_pos1[0],current_pos1[1])
    X_new,Y_new=current_pos1[0]-learning_rate*X_grad,current_pos1[1]-learning_rate*Y_grad
    current_pos1=(X_new,Y_new,z_func(X_new,Y_new))

    X_grad, Y_grad = calc_gradient(current_pos2[0], current_pos2[1])
    X_new, Y_new = current_pos2[0] - learning_rate * X_grad, current_pos2[1] - learning_rate * Y_grad
    current_pos2 = (X_new, Y_new, z_func(X_new, Y_new))

    X_grad, Y_grad = calc_gradient(current_pos3[0], current_pos3[1])
    X_new, Y_new = current_pos3[0] - learning_rate * X_grad, current_pos3[1] - learning_rate * Y_grad
    current_pos3 = (X_new, Y_new, z_func(X_new, Y_new))

    ax.plot_surface(X,Y,Z,cmap="viridis",zorder=0)
    ax.scatter(current_pos1[0],current_pos1[1],current_pos1[2],color="magenta")
    ax.scatter(current_pos2[0], current_pos2[1], current_pos2[2], color="magenta")
    ax.scatter(current_pos3[0], current_pos3[1], current_pos3[2], color="magenta")
    plt.pause(0.001)
    plt.cla()
