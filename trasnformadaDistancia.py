import numpy as numpy
from itertools import product
from copy import deepcopy
import matplotlib.pyplot as plt
from skimage import draw
from tkinter import *
from util.Imagem import *

class Transformada:
    N_max = numpy.inf

    def __init__(self, master=None):
        janela.title("Janela")
        janela.geometry("1000x600")
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Transformada da Distância")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack()

        self.b1 = Button(self.widget1)
        self.b1["text"] = "D_E"
        self.b1["font"] = ("Calibri", "9")
        self.b1["width"] = 55
        self.b1["command"] = self.D_E
        self.b1.pack()

        self.b2 = Button(self.widget1)
        self.b2["text"] = "D_E_Aleatoria"
        self.b2["font"] = ("Calibri", "9")
        self.b2["width"] = 55
        self.b2["command"] = self.D_E_Aleatoria
        self.b2.pack()

        self.b3 = Button(self.widget1)
        self.b3["text"] = "D_4"
        self.b3["font"] = ("Calibri", "9")
        self.b3["width"] = 55
        self.b3["command"] = self.D_4
        self.b3.pack()

        self.b4 = Button(self.widget1)
        self.b4["text"] = "D_4_Aleatoria"
        self.b4["font"] = ("Calibri", "9")
        self.b4["width"] = 55
        self.b4["command"] = self.D_4_Aleatoria
        self.b4.pack()

        self.b5 = Button(self.widget1)
        self.b5["text"] = "D_8"
        self.b5["font"] = ("Calibri", "9")
        self.b5["width"] = 55
        self.b5["command"] = self.D_8
        self.b5.pack()

        self.b6 = Button(self.widget1)
        self.b6["text"] = "D_8_Aleatoria"
        self.b6["font"] = ("Calibri", "9")
        self.b6["width"] = 55
        self.b6["command"] = self.D_8_Aleatoria
        self.b6.pack()

        self.b7 = Button(self.widget1)
        self.b7["text"] = "D_E_ImagemReal"
        self.b7["font"] = ("Calibri", "9")
        self.b7["width"] = 55
        self.b7["command"] = self.D_E_ImagemReal
        self.b7.pack()

    # Distância Euclidiana
    def distanciaEuclidiana(*p):
        # parametros p: (x1, x2, y1, y2)
        distancia = numpy.sqrt((p[0] - p[1]) ** 2 + (p[2] - p[3]) ** 2)
        return distancia

    # Distancia Quarteirão ou (D_4)
    def distanciaQuarteirao(*p):
        # parametros p: (x1, x2, y1, y2)
        distancia = numpy.abs(p[0] - p[1]) + numpy.abs(p[2] - p[3])
        return distancia

    # Distancia Xadrez ou (D_8)
    def distanciaXadrez(*p):
        # parametros p: (x1, x2, y1, y2)
        distancia = numpy.max([numpy.abs(p[0] - p[1]), numpy.abs(p[2] - p[3])])
        return distancia

    def gerarImagem(aleatorio=True):

        if aleatorio:
            imagem = numpy.zeros([100, 100])

            x = numpy.random.randint(0, 100, 3) # Gera 3 valores de x aleatórios de 0 a 100.
            y = numpy.random.randint(0, 100, 3) # Gera 3 valores de y aleatórios de 0 a 100.

            for i in range(len(x)): # Laço que percorre a lista de valores gerada aleatoriamente. 
                # Cria um círculo externo e um interno. Em seguida, subtrai o interno do externo.
                raio = 1 #Raio do círculo
                centro = (x[i],y[i]) #Coordenada central do círculo. Seta o valor atual de x e y. 
                rr, cc = draw.disk(centro, radius=raio, shape=imagem.shape) #Gera coordenadas de pixels dentro do círculo.

                imagem[rr, cc] = 1
        else:
            imagem = numpy.array([[0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 1, 1, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0]
                ], dtype=numpy.float)

            # imagem = numpy.zeros([80, 80])
            # imagem[40, 40] = 1

        imagemSaida = deepcopy(imagem)

        # Gerando o inverso da imagem.
        imagemSaida[numpy.where(imagem == 0)] = Transformada.N_max
        imagemSaida[numpy.where(imagem == 1)] = 0

        return imagemSaida

    def getMascara(etapa):
        listaCoordenadas = numpy.array(list(range(3))) - 1 #Cálculo de vizinhança euclidiano de 3 por 3. (main.py)
        #listaCoordenadas = numpy.array(list(range(5))) - 2 #Cálculo de vizinhança euclidiano de 5 por 5. (main.py)
        #listaCoordenadas = numpy.array(list(range(7))) - 3 #Cálculo de vizinhança euclidiano de 7 por 7. (main.py)

        mascaras = numpy.array(list(product(listaCoordenadas, listaCoordenadas)))

        if etapa == 1: #Se você tiver uma lista / matriz / array bidimensional, esta notação fornecerá todos os valores na coluna 0 (de todas as linhas).
            mapeamentoMascara = mascaras[numpy.where((mascaras[:, 0] < 0) | ((mascaras[:, 0] == 0) & (mascaras[:, 1] < 0)))]
        elif etapa == 2:
            mapeamentoMascara = mascaras[numpy.where((mascaras[:, 0] > 0) | ((mascaras[:, 0] == 0) & (mascaras[:, 1] > 0)))]

        return mapeamentoMascara

    #Calcula a distância à esquerda, parte superior do filtro.
    def passoUm(distancia, imagem):
        altura = imagem.shape[0]
        largura = imagem.shape[1]

        # Realiza uma cópia desvinculada do objeto imagem
        imagemSaida = deepcopy(imagem)

        for y in range(altura):
            for x in range(largura):
                mascaras = []
                for coordenada in Transformada.getMascara(1): # coordenada  - Coordenada da Vizinhança Paso 1.
                    try:
                        mascara = distancia(y, y + coordenada[1], x, x + coordenada[0]) + \
                                    imagemSaida[y + coordenada[1]:y + coordenada[1] + 1, x + coordenada[0]:x + coordenada[0] + 1]
                        if len(mascara) == 0:
                            mascara = Transformada.N_max
                    except:
                        mascara = Transformada.N_max

                    mascaras.append(mascara)

                # Adicionar Centro.
                mascaras.append(imagemSaida[y, x])

                try:
                    imagemSaida[y, x] = numpy.min(mascaras).item()
                except:
                    imagemSaida[y, x] = numpy.min(mascaras)

        return imagemSaida

    #Calcula a distância à direita, parte inferior do filtro.
    def passoDois(distancia, imagem):
        altura = imagem.shape[0]
        largura = imagem.shape[1]

        # Realiza uma cópia desvinculada do objeto imagem
        imagemSaida = deepcopy(imagem)

        for y in range(altura - 1, -1, -1):
            for x in range(largura - 1, -1, -1):
                mascaras = []
                for coordenada in Transformada.getMascara(2): # coordenada  - Coordenada da Vizinhança - Passo 2.
                    try:
                        mascara = distancia(y, y + coordenada[1], x, x + coordenada[0]) + \
                                    imagemSaida[y + coordenada[1]:y + coordenada[1] + 1, x + coordenada[0]:x + coordenada[0] + 1]
                        if len(mascara) == 0:
                            mascara = Transformada.N_max
                    except:
                        mascara = Transformada.N_max

                    mascaras.append(mascara)

                # Adicionar Centro.
                mascaras.append(imagemSaida[y, x])

                try:
                    imagemSaida[y, x] = numpy.min(mascaras).item()
                except:
                    imagemSaida[y, x] = numpy.min(mascaras)

        return imagemSaida

    def transformadaImagemFixa(distancia, tipo):
        imagem = Transformada.gerarImagem(aleatorio=False)
        passo_um = Transformada.passoUm(distancia, imagem)
        resultado = Transformada.passoDois(distancia, passo_um)

        plt.subplot(1, 2, 1)
        plt.imshow(imagem)
        plt.title("Imagem")
        
        ax = plt.gca()
        for y in range(imagem.shape[0]):
            for x in range(imagem.shape[1]):
                ax.text(x, y, str(imagem[y, x])[:3], color='white', ha='center', va='center')

        plt.subplot(1, 2, 2)
        plt.imshow(resultado)
        plt.title("Imagem com {}".format(tipo))

        ax = plt.gca()
        for y in range(resultado.shape[0]):
            for x in range(resultado.shape[1]):
                ax.text(x, y, str(resultado[y, x])[:3], color='white', ha='center', va='center')


        plt.show()

    def transformadaImagemAleatoria(distancia, tipo):
        imagem = Transformada.gerarImagem()
        passo_um = Transformada.passoUm(distancia, imagem)
        resultado = Transformada.passoDois(distancia, passo_um)
        X, Y = numpy.meshgrid(list(range(imagem.shape[0])), list(range(imagem.shape[1])))

        plt.subplot(1, 2, 1)
        plt.title("Aleatório")
        plt.imshow(imagem)

        plt.subplot(1, 2, 2)
        plt.title("Aleatório com {}".format(tipo))
        plt.imshow(resultado)

        plt.contour(X, Y, resultado[Y, X], 12, colors='white', linewidths=.2)
        plt.show()

    def D_E_imagemReal(self, distancia, imagemEntrada: Imagem):
        nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
        altura = (
            imagemEntrada.getAltura()
        )  # Numero correspondente a Altura da Imagem
        largura = (
            imagemEntrada.getLargura()
        )  # Numero correspondente a Largura da Imagem
        matrizSaida = numpy.zeros(
            (nCanais, altura, largura)
        )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura. #Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
        # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])

        #TODO 

        imagemSaida = Imagem()  # Cria um objeto do tipo Imagem
        imagemSaida.criarComMatriz(
            matrizSaida
        )  # Cria a imagem de saída com os dados da matriz de saída.
        imagemSaida.mostrar(
            janela, "Imagem Saida"
        )  # Mostrar na tela a imagem tratada.
        return imagemSaida

    def imagemReal(self, distancia):
        imagem = Imagem()  # Cria um objeto do tipo Imagem
        imagem.carregar("img/aviao.png")  # Carrega a imagem do diretório
        imagemSaida = self.D_E_imagemReal(distancia, imagem)
        return imagemSaida 

    def D_E(self):
        Transformada.transformadaImagemFixa(Transformada.distanciaEuclidiana, "D_E")

    def D_E_Aleatoria(self):
        Transformada.transformadaImagemAleatoria(Transformada.distanciaEuclidiana, "D_E_Aleatoria")

    def D_4(self):
        Transformada.transformadaImagemFixa(Transformada.distanciaQuarteirao, "D_4")

    def D_4_Aleatoria(self):
        Transformada.transformadaImagemAleatoria(Transformada.distanciaQuarteirao, "D_4_Aleatoria")

    def D_8(self):
        Transformada.transformadaImagemFixa(Transformada.distanciaXadrez, "D_8")

    def D_8_Aleatoria(self):
        Transformada.transformadaImagemAleatoria(Transformada.distanciaXadrez, "D_8_Aleatoria")
    
    def D_E_ImagemReal(self):
        self.imagemReal(self.distanciaEuclidiana)

janela = Tk()
Transformada(janela)
janela.mainloop()
        
