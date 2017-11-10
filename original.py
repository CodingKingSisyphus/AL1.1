# example of numerical integration of projectile motion in 2D
import matplotlib.pyplot as plt
from math import sin, cos, atan2, pi, sqrt

# constants
rho = 1.22 # density of medium
g = 9.81   # acceleration of gravity

# projectile properties
A = 0.05  # cross sectional area
Cd = 0.5  # drag factor
m = 0.1   # mass

# initial velocity & angle (radians)
v = 10.      # m/s
theta = pi/4

# initial position, velocity, time
x = 0.
y = 5.    # height above target surface
vx = v * cos(theta)
vy = v * sin(theta)
vx_init = vx
t = 0.

# storage for the result
X = [x]
Y = [y]
VX = [vx]
VY = [vy]
V=[v]
T=[t]
# step size
dt = 0.01

def drag(v, theta):
    F =0.5*rho*v*v*A*Cd
    return (F*cos(theta), F*sin(theta))

while ((y>0) | (vy>0)):
    # instantaneous force:
    Fx, Fy = drag(v, theta)
    # acceleration:
    ax = -Fx/m
    ay = -Fy/m - g
    # position update:
    x = x + vx*dt + 0.5*ax*dt*dt
    y = y + vy*dt + 0.5*ay*dt*dt
    # update velocity components:
    vx = vx + ax*dt
    vy = vy + ay*dt
    # new angle and velocity:
    v = sqrt(vx*vx+vy*vy)
    theta = atan2(vy,vx)
    # store result for plotting:
    X.append(x)
    Y.append(y)
    t = t + dt
    VX.append(vx)
    VY.append(vy)
    V.append(v)
    T.append(t)
# adjust last point to Y=0 - we may have "overshot":
ft = Y[-2]/(Y[-2]-Y[-1]) # fractional time to last point
X[-1] = X[-2] + (X[-1]-X[-2])*ft
Y[-1] = 0.
t = t - (1-ft)*dt

print('Total flight time: %.3f sec\n'%t)
print('Total distance: %.2f m'%X[-1])
print('Initial horizontal velocity: %.2f m/s'%vx_init)
print('Final horizontal velocity: %.2f m/s'%vx)
plt.figure()
plt.plot(X,Y)
plt.title('projectile motion')
plt.xlabel('X position')
plt.ylabel('Y position')
plt.show()

plt.figure()
plt.plot(VX,T)
plt.title('Velocidade horizontal - tempo')
plt.xlabel('t(s)')
plt.ylabel('Vx(m/s)')
plt.show()

plt.figure()
plt.plot(VY,T)
plt.title('Velocidade vertical - tempo')
plt.xlabel('t(s)')
plt.ylabel('Vy(m/s)')
plt.show()
