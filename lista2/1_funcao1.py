import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return 5 * np.power(x, 3) + 2 * np.power(x, 2) - 3 * x - 1

def df(x):
    return 15 * np.power(x, 2) + 4 * x - 3

def d2f(x):
    return 30 * x + 4

def d3f(x):
    return 30

def taylor_truncada_3(x, deltax):
    return f(x) + deltax * df(x) + np.power(deltax, 2) * d2f(x) / 2 + np.power(deltax, 3) * d3f(x) / 6

deltax = 0.001
x_min = -2
x_max = 2
x = np.linspace(x_min, x_max, 40)
y_taylor = np.array([taylor_truncada_3(xi, deltax) for xi in x])
y_f = f(x)
erro = np.abs(100 * (y_taylor - y_f)/y_f)

plt.plot(x, y_taylor, '-or', label='Taylor Truncada')
plt.plot(x, y_f, '-b', label='f(x)')
plt.grid()
plt.title("Série de Taylor para f(x)")
plt.legend()
plt.show()
print(f'Erro médio: {np.mean(erro):.2f}%')

x_dado = np.array([0.01,1.0,2.0,10.0])
plt.plot(x_dado, f(x_dado), "or", label = 'f(x) calculado nos pontos solicitados')
plt.plot(x_dado, taylor_truncada_3(x_dado, deltax), "ob", label = 'Série de taylor truncada calculada nos pontos solicitados')
plt.grid()
plt.title("Série de Taylor para os pontos solicitados de f(x)")
plt.legend()
plt.show()
print(f'Erro entre os valores: {np.abs(100 * (f(x_dado) - taylor_truncada_3(x_dado, deltax))/f(x_dado))}')