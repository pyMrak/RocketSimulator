from numpy import arange, linspace
from matplotlib import pyplot as plt

rho = 1.293 # [kg/m3]
ag = 9.41
m = 0.15
A = 9.535e-4
cd = 0.3
tm_lookup = arange(0, 1.65, 0.05)
Fm_lookup = [0, 0, 2.2, 4.0, 6.5, 10.2, 15.2, 13.0, 10.8, 8.8, 7.5, 7.2, 6.9, 6.7, 6.2, 6.0, 5.9, 5.9, 5.9, 5.8, 5.8, 5.8, 5.8, 5.8, 5.9, 5.9, 5.9, 5.9, 6.0, 6.0, 4.0, 0.3, 0.0]

DC = 0.5*rho*cd*A

def motorForce(t):
    if t > tm_lookup[0] and t < tm_lookup[-1]:
        for i, tm in enumerate(tm_lookup):
            if t < tm:
                break
        F = Fm_lookup[i-1] + (t - tm_lookup[i-1])*(Fm_lookup[i] - Fm_lookup[i-1])/(tm_lookup[i] - tm_lookup[i-1])
    else:
        F = 0
    return F

dt = 0.01
t = 0
v = 0
x = 0
a = 0
while True:
    Fm = motorForce(t)
    x = v*dt
    v = a*dt
    Fu = v**2*DC
    Fg = m*ag
    F = Fm - Fu - Fg
    a = F/m




# t = linspace(-1, 5, 1000)
# F = [motorForce(ti) for ti in t]
# plt.plot(t, F)
# plt.plot(tm_lookup, Fm_lookup)
# plt.grid()
# plt.show()

