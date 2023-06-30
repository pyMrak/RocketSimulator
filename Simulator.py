from numpy import arange, linspace
from matplotlib import pyplot as plt

rho = 1.293 # [kg/m3]
ag = 9.81
m = 0.154
mf = 0.01
A = 9.535e-4
cd = 0.5
tm_lookup = arange(0, 1.65, 0.05)
Fm_lookup = [0, 0, 2.2, 4.0, 6.5, 10.2, 15.2, 13.0, 10.8, 8.8, 7.5, 7.2, 6.9, 6.7, 6.2, 6.0, 5.9, 5.9, 5.9, 5.8, 5.8, 5.8, 5.8, 5.8, 5.9, 5.9, 5.9, 5.9, 6.0, 6.0, 4.0, 0.3, 0.0]

DC = 0.5*rho*cd*A

def calculateMotorMassConsumption(fuelMass):
    I = 0
    for i in range(len(tm_lookup)-1):
        I += (Fm_lookup[i+1] + Fm_lookup[i])/2*(tm_lookup[i+1] - tm_lookup[i])
    return fuelMass/I

fuelConsumptionConstant = calculateMotorMassConsumption(mf)
lastF = 0
lastT = 0

def motorForce(t):
    global lastT
    global lastF
    if t > tm_lookup[0] and t < tm_lookup[-1]:
        for i, tm in enumerate(tm_lookup):
            if t < tm:
                break
        F = Fm_lookup[i-1] + (t - tm_lookup[i-1])*(Fm_lookup[i] - Fm_lookup[i-1])/(tm_lookup[i] - tm_lookup[i-1])
    else:
        F = 0
    massConsumption = (F + lastF)/2*(t - lastT)*fuelConsumptionConstant
    lastF = F
    lastT = t
    return F, massConsumption

dt = 0.01
t = 0
v = 0
y = 0
a = 0
moving = False

tr = []
yr = []
vr = []
ar = []
mr = []

while True:
    Fm, dm = motorForce(t)
    y += v*dt
    v += a*dt
    Fu = v*abs(v)*DC
    Fg = m*ag
    m -= dm
    tr.append(t)
    yr.append(y)
    vr.append(v)
    ar.append(a/ag)
    mr.append(m)
    if (not moving) and Fm > Fg:
        moving = True
    if moving:
        F = Fm - Fu - Fg
        if y < 0:
            v = 0
            break
    else:
        F = 0
    a = F/m
    t += dt




# t = linspace(-1, 5, 1000)
# F = [motorForce(ti) for ti in t]
plt.plot(tr, yr)
plt.grid()
plt.show()

