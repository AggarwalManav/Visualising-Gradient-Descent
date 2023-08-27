import numpy as np
import matplotlib.pyplot as plt

def y_func(x):
    return x**2
def y_derivative(x):
    return 2*x
x=np.arange(-100,100,0.1)
y=y_func(x)
current_pos=(80,y_func(80))
learning_rate=0.01
for i in range(600):
    x_new=current_pos[0]-learning_rate*y_derivative(current_pos[0])
    y_new=y_func(x_new)
    current_pos=(x_new,y_new)
    plt.plot(x,y)
    plt.scatter(current_pos[0],current_pos[1],color="red")
    plt.pause(0.001)
    plt.clf()