import numpy as np
from matplotlib import pyplot as plt

#Criando vetores e variáveis
n = 100
Ca = np.zeros(n)
Cb = np.zeros(n)
Cc = np.zeros(n)
tmax = 25
t0 = 0
t = np.linspace(t0 , tmax, n)
k1 = 0.03
k2 = 0.075
delta_t = t[1] - t[0]
print(f'Passo: {delta_t}')

#Condições iniciais
Ca0 = 40
Cb0 = 50
Cc0 = 0

Ca[0] = Ca0
Cb[0] = Cb0
Cc[0] = Cc0

#Modelando as equações:

for i in range(n-1):
  Ca[i+1] = (-k1 * Ca[i] * Cb[i] + k2 * Cc[i]) * delta_t + Ca[i]
  Cb[i+1] = (-k1 * Ca[i] * Cb[i] + k2 * Cc[i]) * delta_t + Cb[i]
  Cc[i+1] = (k1 * Ca[i] * Cb[i] - k2 * Cc[i]) * delta_t + Cc[i]

#plotando

plt.plot(t, Ca, '-r', label='Ca(t)')
plt.plot(t, Cb, '-b', label='Cb(t)')
plt.plot(t, Cc, '-g', label='Cc(t)')
plt.title("Concentrações para a reação de 1ª ordem A + B --> C")
plt.grid()
plt.legend()
plt.show()

print(Ca)
print(Cb)
print(Cc)
print(t)