import matplotlib.pyplot as plt
from math import sin, cos, atan2, pi, sqrt

# constantes
rho = 1.18  # densidade do meio (ar)
g = 9.81   # aceleração gravítica

# propriedades do projétil
m = 0.00137   # massa
Cd_x=0.47   # coefifiente aerodinâmico horizontal
Cd_y=0.82   # coeficiente aerodinâmico vertical
A_x=0.000133    # área na vertical (frente)
A_y=0.001079    # área na horizontal (baixo)
# velocidade inicial e ângulo (em radianos)
v = 14.1      # m/s
theta = 0

# posição inicial
x = 0.
y = 0.64   # altura inicial

def velocidade(v,theta):
    vx= v * cos(theta) 
    vy= v * sin(theta)
    return (vx,vy)

vx = velocidade(v,theta)[0] 
vy = velocidade(v,theta)[1]
vx_init = vx
t = 0.0

# listagem de dados
X = [x]
Y = [y]
VX = [vx]
VY = [vy]
V=[v]
T=[t]
dt=0.01


def drag(v):
    F_y =0.5*rho*vy*vy*A_y*Cd_y
    F_x =0.5*rho*vx*vx*A_x*Cd_x
    return (F_x, F_y)

while ((y>0) | (vy>0)):
    
    Fx, Fy = drag(v)
    
    ax = -Fx/m 
    ay = +Fy/m - g
    

    vx = vx + ax*dt
    vy = vy + ay*dt

    
    x = x + vx*dt + 0.5*ax*dt*dt
    y = y + vy*dt + 0.5*ay*dt*dt
    
    
    v = sqrt(vx*vx+vy*vy)
    theta = atan2(vy,vx)
    t = t + dt
    
    X.append(x)
    Y.append(y)

print('Tempo de voo: %.3f sec\n'%t)
print('Distância total: %.2f m'%X[-1])
print('Velocidade horizontal inicial: %.2f m/s'%vx_init)
print('Velocidade horizontal final: %.2f m/s'%vx)
plt.figure()
plt.plot(X,Y)
plt.title('Trajetoria')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

