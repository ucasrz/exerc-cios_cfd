import numpy as np
from math import factorial
from matplotlib import pyplot as plt


def derivadas_seno(x):
    return np.array([np.sin(x),np.cos(x),-np.sin(x),-np.cos(x)])


def taylor_truncada_8(x, deltax):
    funcao = 0
    y = derivadas_seno(x)
    for i in range(8):
        if i < 4:
            funcao += y[i] * np.power(deltax, i) / factorial(i) #vi depois com o chatgpt que poderia ter usado i%4 no índice de y que daria certo, mas resolvi deixar do jeito q pensei
        else:
            j = i - 4
            funcao += y[j] * np.power(deltax, i) / factorial(i)
    return funcao


deltax = 0.001
x_min = -6
x_max = 6
x = np.linspace(x_min, x_max, 100)
y = taylor_truncada_8(x, deltax)
erro = np.abs(100 * (y - np.sin(x + deltax))/np.sin(x + deltax))


plt.plot(x, y, '-or', label='Taylor Truncada 8 termos')
plt.plot(x, np.sin(x + deltax), '-b', label='sin(x + deltax)')
plt.grid()
plt.title("Série de Taylor para sin(x) truncada em 8 termos")
plt.legend()
plt.show()
print(f'Erro médio: {np.mean(erro):.2f}%')

x_dado = np.array([0.01,1.0,2.0,10.0])
plt.plot(x_dado, np.sin(x_dado), "or", label = 'g(x) calculado nos pontos solicitados')
plt.plot(x_dado, taylor_truncada_8(x_dado, deltax), "ob", label = 'Série de taylor truncada calculada nos pontos solicitados')
plt.grid()
plt.title("Série de Taylor para os pontos solicitados de g(x)")
plt.legend()
plt.show()
erro_pontos = np.abs(100 * (np.sin(x_dado) - taylor_truncada_8(x_dado, deltax)) / np.sin(x_dado))
print(f'Erro entre os valores: {erro_pontos}')
print(taylor_truncada_8(0.01, deltax) - np.sin(0.01))