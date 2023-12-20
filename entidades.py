import numpy as np
import matplotlib.pyplot as plt

class Grafico:
    def __init__(self):
        self.x = None
        self.y = None

    def criar_eixo_x(self, inicio, fim, passo):
        self.x = np.linspace(inicio, fim, passo)

    def calcular_y(self, funcao):
        self.y = funcao(self.x)

    def configura_limites_dos_eixos(self, limite_inferior_x=None, limite_superior_x=None, limite_inferior_y=None, limite_superior_y=None):
        if ((limite_inferior_x is not None) and (limite_superior_x is not None) and (limite_inferior_y is not None) and (limite_superior_y is not None)):
            plt.xlim([limite_inferior_x, limite_superior_x])
            plt.ylim([limite_inferior_y, limite_superior_y])

    def configura_titulo_e_rotulos(self, titulo=None, rotulo_x=None, rotulo_y=None):
        if titulo is not None:
            plt.title(titulo)
        if rotulo_x is not None:
            plt.xlabel(rotulo_x)
        if rotulo_y is not None:
            plt.ylabel(rotulo_y)

    def exibir_grafico(self):
        # Adicionar linha paralela ao eixo y
        plt.axvline(x=0, color='r', linestyle='--')
        # Adicionar linha paralela ao eixo x
        plt.axhline(y=0, color='r', linestyle='--')      
        plt.plot(self.x, self.y)
        plt.show()