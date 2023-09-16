#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://tranduythanh.com

import  random
import matplotlib.pyplot as plt

incircle=0

simCount=int(input("Maximum number of simulations?"))

circle_center=(0,0)
circle_radius=1

c=plt.Circle(circle_center,circle_radius,ec='b',fill=False)

a=plt.axes(xlim=(-1,1),ylim=(-1,1))
a.add_patch(c)
a.set_aspect('equal')

for i in range(simCount):
    # Create real number x coordinates from -1 to 1
    x=random.uniform(-1.0,1.0)
    # Create real y coordinates from -1 to 1
    y=random.uniform(-1.0,1.0)
    plt.scatter(x,y,s=2)

    dot_value=x*x+y*y
    # Test where the (x,y) coordinates are in the circle
    if dot_value<=1:
        incircle =incircle+1

print("Pi=",4*incircle/simCount)
plt.show()
