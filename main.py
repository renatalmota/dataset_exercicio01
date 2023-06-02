import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()

fluxo_de_caixa = ('jan-mar', 'abr-jun', 'jul-set', 'out-dez')
indice = np.arange(len(fluxo_de_caixa))
acessos = [199300.00, 1370250.00, 40550.00, 15000.00]
plt.bar(indice, acessos)
plt.xticks(indice, fluxo_de_caixa)
plt.ylabel('Acessos')
plt.title('Ranking do 2022')

plt.show()