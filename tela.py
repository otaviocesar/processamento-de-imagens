from tkinter import *
from util.Imagem import *
import numpy as numpy
from random import random, randrange


class Application:
    def __init__(self, master=None):
        janela.title("Janela")
        janela.geometry("1000x600")
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Imagem")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack()

        self.b1 = Button(self.widget1)
        self.b1["text"] = "Carregar"
        self.b1["font"] = ("Calibri", "9")
        self.b1["width"] = 55
        self.b1["command"] = self.carregar
        self.b1.pack()

        self.b4 = Button(self.widget1)
        self.b4["text"] = "Salvar"
        self.b4["font"] = ("Calibri", "9")
        self.b4["width"] = 55
        self.b4["command"] = self.salvar
        self.b4.pack()

        self.b5 = Button(self.widget1)
        self.b5["text"] = "Limiar Simples"
        self.b5["font"] = ("Calibri", "9")
        self.b5["width"] = 55
        self.b5["command"] = self.limiarSimples
        self.b5.pack()

        self.b6 = Button(self.widget1)
        self.b6["text"] = "Limiar Com Modulacao Aleatoria"
        self.b6["font"] = ("Calibri", "9")
        self.b6["width"] = 55
        self.b6["command"] = self.limiarComModulacaoAleatoria
        self.b6.pack()

        self.b7 = Button(self.widget1)
        self.b7["text"] = "Limiar Com Modulacao Ordenada Periodico Aglomerado"
        self.b7["font"] = ("Calibri", "9")
        self.b7["width"] = 55
        self.b7["command"] = self.limiarComModulacaoOrdenadaPeriodicoAglomerado
        self.b7.pack()

        self.b8 = Button(self.widget1)
        self.b8["text"] = "Limiar Com Modulacao Ordenada Periodico Disperso"
        self.b8["font"] = ("Calibri", "9")
        self.b8["width"] = 55
        self.b8["command"] = self.limiarComModulacaoOrdenadaPeriodicoDisperso
        self.b8.pack()

        self.b9 = Button(self.widget1)
        self.b9["text"] = "Limiar Com Modulacao Ordenada Aperiodico"
        self.b9["font"] = ("Calibri", "9")
        self.b9["width"] = 55
        self.b9["command"] = self.limiarComModulacaoOrdenadaAperiodico
        self.b9.pack()

        self.b10 = Button(self.widget1)
        self.b10["text"] = "Erosão - Morfologia matemática binária"
        self.b10["font"] = ("Calibri", "9")
        self.b10["width"] = 55
        self.b10["command"] = self.erosaoBin
        self.b10.pack()

        self.b11 = Button(self.widget1)
        self.b11["text"] = "Dilatação - Morfologia matemática binária"
        self.b11["font"] = ("Calibri", "9")
        self.b11["width"] = 55
        self.b11["command"] = self.dilatacaoBin
        self.b11.pack()

        self.b12 = Button(self.widget1)
        self.b12["text"] = "Abertura - Morfologia matemática binária"
        self.b12["font"] = ("Calibri", "9")
        self.b12["width"] = 55
        self.b12["command"] = self.aberturaBin
        self.b12.pack()

        self.b13 = Button(self.widget1)
        self.b13["text"] = "Fechamento - Morfologia matemática binária"
        self.b13["font"] = ("Calibri", "9")
        self.b13["width"] = 55
        self.b13["command"] = self.fechamentoBin
        self.b13.pack()

        self.b14 = Button(self.widget1)
        self.b14["text"] = "Borda interna"
        self.b14["font"] = ("Calibri", "9")
        self.b14["width"] = 55
        self.b14["command"] = self.bordaInterna
        self.b14.pack()

        self.b15 = Button(self.widget1)
        self.b15["text"] = "Borda externa"
        self.b15["font"] = ("Calibri", "9")
        self.b15["width"] = 55
        self.b15["command"] = self.bordaExterna
        self.b15.pack()

        self.b16 = Button(self.widget1)
        self.b16["text"] = "Erosão - Morfologia matemática monocromática"
        self.b16["font"] = ("Calibri", "9")
        self.b16["width"] = 55
        self.b16["command"] = self.erosaoMon
        self.b16.pack()

        self.b17 = Button(self.widget1)
        self.b17["text"] = "Dilatação - Morfologia matemática monocromática"
        self.b17["font"] = ("Calibri", "9")
        self.b17["width"] = 55
        self.b17["command"] = self.dilatacaoMon
        self.b17.pack()

        self.b18 = Button(self.widget1)
        self.b18["text"] = "Abertura - Morfologia matemática monocromática"
        self.b18["font"] = ("Calibri", "9")
        self.b18["width"] = 55
        self.b18["command"] = self.aberturaMon
        self.b18.pack()

        self.b19 = Button(self.widget1)
        self.b19["text"] = "Fechamento - Morfologia matemática monocromática"
        self.b19["font"] = ("Calibri", "9")
        self.b19["width"] = 55
        self.b19["command"] = self.fechamentoMon
        self.b19.pack()

        self.b20 = Button(self.widget1)
        self.b20["text"] = "Gradiente"
        self.b20["font"] = ("Calibri", "9")
        self.b20["width"] = 55
        self.b20["command"] = self.gradiente
        self.b20.pack()

        self.b21 = Button(self.widget1)
        self.b21["text"] = "Smoothing"
        self.b21["font"] = ("Calibri", "9")
        self.b21["width"] = 55
        self.b21["command"] = self.smoothing
        self.b21.pack()

    def carregar(self):
        if self.msg["text"] == "Imagem":
            # self.msg["text"] = "Teste"
            img1 = Imagem()  # Cria um objeto do tipo Imagem
            img1.carregar("img/lenna.png")  # Carrega a imagem do diretório
            img1.mostrar(janela, "Testando lenna.png")  # Mostrar na tela a imagem
        else:
            self.msg["text"] = "Imagem"

    def criarVazia(self):
        if self.msg["text"] == "Imagem":
            img2 = Imagem()  # Cria um objeto do tipo Imagem
            img2.criarVazia(
                "RGB",
                100,
                200,
            )
            img2.mostrar(
                janela, "Vazia RGB 100x200"
            )  # Mostrar na tela a imagem tratada.
        else:
            self.msg["text"] = "Imagem"

    def criarDeMatriz(self):
        if self.msg["text"] == "Imagem":
            img3 = Imagem()  # Cria um objeto do tipo Imagem
            matriz = [
                [[255, 255, 255], [255, 255, 255], [255, 255, 255]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ]
            img3.criarComMatriz(matriz)
            img3.mostrar(
                janela, "Criando através de uma matriz pré-existente"
            )  # Mostrar na tela a imagem tratada.
        else:
            self.msg["text"] = "Imagem"

    def converteParaRgb(self):
        if self.msg["text"] == "Imagem":
            img4 = Imagem()  # Cria um objeto do tipo Imagem
            img4.carregar("img/lenna.png")  # Carrega a imagem do diretório
            img4.mostrar(janela)  # Mostrar na tela a imagem tratada.
            img4.toRGB()
            img4.mostrar(janela)  # Mostrar na tela a imagem tratada.
        else:
            self.msg["text"] = "Imagem"

    def converteParaCinza(self):
        if self.msg["text"] == "Imagem":
            img4 = Imagem()  # Cria um objeto do tipo Imagem
            img4.carregar("img/lennaRGB.jpg")  # Carrega a imagem do diretório
            img4.mostrar(janela)  # Mostrar na tela a imagem tratada.
            img4.toGray()
            img4.mostrar(janela)  # Mostrar na tela a imagem tratada.
        else:
            self.msg["text"] = "Imagem"

    def getMatriz(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            # imagemEntrada.carregar('img/olho.png') #Carrega a imagem do diretório
            imagemEntrada.carregar("img/lennaRGB.jpg")  # Carrega a imagem do diretório
            # imagemEntrada.criarVazia('L',4,5)
            matriz = (
                imagemEntrada.getMatriz()
            )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
            for i in range(30):
                matriz[0][i][i] = 255
            imagemEntrada.criarComMatriz(matriz)
            imagemEntrada.mostrar(janela)  # Mostrar na tela a imagem tratada.
        else:
            self.msg["text"] = "Imagem"

    def salvar(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar("img/lennaRGB.jpg")  # Carrega a imagem do diretório
            matriz = (
                imagemEntrada.getMatriz()
            )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
            for i in range(100):
                matriz[0][i][i] = 200
                matriz[0][i][i] = 128
            imagemEntrada.criarComMatriz(matriz)
            imagemEntrada.mostrar(janela)  # Mostrar na tela a imagem tratada.
            imagemEntrada.salvar("img/testeSalvar.png", imagemEntrada.TYPE_PNG())
            imagemEntrada.salvar("img/testeSalvar.jpg", imagemEntrada.TYPE_JPG())
            imagemEntrada.salvar("img/testeSalvar.gif", imagemEntrada.TYPE_GIF())
            imagemEntrada.salvar("img/testeSalvar.pdf", imagemEntrada.TYPE_PDF())
        else:
            self.msg["text"] = "Imagem"

    def subtracao(self, imgA: Imagem, imgB: Imagem):
        nCanais = imgA.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
        altura = imgA.getAltura()  # Numero correspondente a Altura da Imagem
        largura = imgA.getLargura()  # Numero correspondente a Largura da Imagem
        matA = imgA.getMatriz()  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
        matB = imgB.getMatriz()  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))

        cor = None  # Inicializa variável cor.
        matrizSaida = numpy.zeros(
            (nCanais, altura, largura)
        )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
        # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
        # Laços que percorrem cada pixel
        for c in range(
            nCanais
        ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                altura
            ):  # Laço de posição altura y - Laço que percorre todos os pixels no eixo y.
                for x in range(
                    largura
                ):  # Laço de posição largura x -  Laço que percorre todos os pixels no eixo x.
                    cor = matA[c][y][x] - matB[c - 1][y - 1][x - 1]  # Realiza subtração
                    if cor < 0:  # Evita estouro para números negativos
                        cor = 0  # Seta zero caso seja um número negativo
                    matrizSaida[
                        c, y, x
                    ] = cor  # Seta resultado da subtração no pixel atual.

        return matrizSaida

    # A limiarização converte uma imagem em níveis de cinza ou colorida numa imagem binária,
    # baseado somente no valor do pixel.

    # O método de limiar simples substitui cada pixel na imagem seguindo a seguinte regra:
    # Substitui por um pixel preto se f(i,j) for menor que o limiar, ou por um pixel branco caso contrário.
    def limiarSimples(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/limiarotimo.jpg"
            )  # Carrega a imagem do diretório
            nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
            altura = (
                imagemEntrada.getAltura()
            )  # Numero correspondente a Altura da Imagem
            largura = (
                imagemEntrada.getLargura()
            )  # Numero correspondente a Largura da Imagem
            matriz = (
                imagemEntrada.getMatriz()
            )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
            matrizSaida = numpy.zeros(
                (nCanais, altura, largura)
            )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura. #Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
            # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
            branco = 255  # 255 é o valor equivalente ao pixel branco
            preto = 0  # 0 é o valor equivalente ao pixel preto # 0 é o valor equivalente ao pixel preto

            # limiar = 128;
            limiar = 64
            # Limiar para substituição
            # limiar = 32;
            # limiar = 16;

            # Laços que percorrem cada pixel
            for c in range(
                nCanais
            ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    altura
                ):  # Laço de posição altura y - Laço que percorre todos os pixels no eixo y.
                    for x in range(
                        largura
                    ):  # Laço de posição altura x - Laço que percorre todos os pixels no eixo x.
                        if (
                            matriz[c][y][x] < limiar
                        ):  # Verifica se o valor do Pixel no canal c, altura y, largura x é menor que o limiar.
                            matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                        else:
                            matrizSaida[
                                c, y, x
                            ] = branco  # Seta o valor do pixel em 255.

            imagemSaida = Imagem()  # Cria um objeto do tipo Imagem
            imagemSaida.criarComMatriz(
                matrizSaida
            )  # Cria a imagem de saída com os dados da matriz de saída.
            imagemSaida.mostrar(
                janela, "Limiar Simples"
            )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # O método de Limiar com Modulação Aleatória substitui cada pixel na imagem seguindo a seguinte regra:
    # Substitui por um pixel preto caso o valor de temp (temp = pixel - valorAleatório)
    # for menor que o limiar, ou por um pixel branco caso contrário.
    def limiarComModulacaoAleatoria(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/limiarotimo.jpg"
            )  # Carrega a imagem do diretório
            nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
            altura = (
                imagemEntrada.getAltura()
            )  # Numero correspondente a Altura da Imagem
            largura = (
                imagemEntrada.getLargura()
            )  # Numero correspondente a Largura da Imagem
            matriz = (
                imagemEntrada.getMatriz()
            )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
            matrizSaida = numpy.zeros(
                (nCanais, altura, largura)
            )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
            # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
            branco = 255  # 255 é o valor equivalente ao pixel branco
            preto = 0  # 0 é o valor equivalente ao pixel preto

            # limiar = 128;
            limiar = 64
            # Limiar para substituição
            # limiar = 32;
            # limiar = 16;
            # limiar = (branco + preto)/2;

            # Laços que percorrem cada pixel
            for c in range(
                nCanais
            ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    altura
                ):  # Laço de posição altura y -  Laço que percorre todos os pixels no eixo y.
                    for x in range(
                        largura
                    ):  # Laço de posição largura x -  Laço que percorre todos os pixels no eixo x.
                        temp = matriz[c][y][x] + randrange(
                            -255, 255
                        )  # Soma o valor do Pixel no canal c, altura y, largura x
                        # com um número aleatório no intervalo de -255 a 255.
                        if (
                            temp < limiar
                        ):  # Verifica se o valor do Pixel resultante é menor que o limiar.
                            matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                        else:
                            matrizSaida[
                                c, y, x
                            ] = branco  # Seta o valor do pixel em 255.

            imagemSaida = Imagem()  # Cria um objeto do tipo Imagem
            imagemSaida.criarComMatriz(
                matrizSaida
            )  # Cria a imagem de saída com os dados da matriz de saída.
            imagemSaida.mostrar(
                janela, "Limiar com modulação aleatória"
            )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    def quantizacao(self, imagemEntrada: Imagem, entrada, saida):
        imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
        imagemEntrada.carregar("img/limiarotimo.jpg")  # Carrega a imagem do diretório
        faixa = int(
            entrada / saida
        )  # Determina a faixa do intervalo entre entrada e saída
        matriz = (
            imagemEntrada.getMatriz()
        )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
        nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
        altura = imagemEntrada.getAltura()  # Numero correspondente a Altura da Imagem
        largura = (
            imagemEntrada.getLargura()
        )  # Numero correspondente a Largura da Imagem

        # Laços que percorrem cada pixel
        for c in range(
            nCanais
        ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                altura
            ):  # Laço de posição altura y - Laço que percorre todos os pixels no eixo y.
                for x in range(
                    largura
                ):  # Laço de posição largura x -  Laço que percorre todos os pixels no eixo x.
                    color = int(
                        matriz[c][y][x] / faixa
                    )  # Valor do pixel é o valor atual dividido pelo valor da faixa
                    matriz[c][y][x] = color

        imagemSaida = Imagem()  # Cria um objeto do tipo Imagem
        imagemSaida.criarComMatriz(
            matriz
        )  # Cria a imagem de saída com os dados da matriz de saída.
        return imagemSaida

    # O método de Limiar com Modulação Ordenada Periódico Aglomerado substitui cada pixel na imagem seguindo a seguinte regra:
    # Substitui por um pixel branco caso o valor do pixel for maior que o valor do
    # pixel da matriz de Dithering de entrada, ou por um pixel preto caso contrário.
    # Inicialmente deve-se quantizar a imagem para NxN + 1 níveis.
    # A Imagem de saída será maior que a de entrada.
    def limiarComModulacaoOrdenadaPeriodicoAglomerado(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/limiarotimo.jpg"
            )  # Carrega a imagem do diretório
            matrizDithering = numpy.array(
                [[2, 2, 2], [2, 2, 2]]
            )  # Matriz de Dithering NXN

            entradaQuantizacao = 255  # Valor de entrada para quantização
            saidaQuantizacao = (
                len(matrizDithering) * len(matrizDithering) + 1
            )  # Valor de saída quantização
            matrizQuantizada = self.quantizacao(
                imagemEntrada, entradaQuantizacao, saidaQuantizacao
            )  # Realiza a Quantização.

            nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
            altura = (
                imagemEntrada.getAltura()
            )  # Numero correspondente a Altura da Imagem
            largura = (
                imagemEntrada.getLargura()
            )  # Numero correspondente a Largura da Imagem

            matrizEntrada = (
                matrizQuantizada.getMatriz()
            )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
            matrizSaida = numpy.zeros(
                (nCanais, altura, largura)
            )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
            # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
            branco = 255  # 255 é o valor equivalente ao pixel branco
            preto = 0  # 0 é o valor equivalente ao pixel preto

            # Laços que percorrem cada pixel
            for c in range(
                nCanais
            ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    altura
                ):  # Laço de posição altura y - Laço que percorre todos os pixels no eixo y.
                    for x in range(
                        largura
                    ):  # Laço de posição largura x -  Laço que percorre todos os pixels no eixo x.
                        for d in range(
                            len(matrizDithering)
                        ):  # Laço que percorre o tamanho da matrizDithering
                            for i in range(
                                len(matrizDithering[d])
                            ):  # Posição i percorrendo a matrizDithering
                                if (
                                    matrizEntrada[c][y][x] > matrizDithering[d][i]
                                ):  # Se Valor do pixel é maior que valor da Posição [d][i] percorrendo a matrizDithering
                                    matrizSaida[
                                        c, y, x
                                    ] = branco  # Seta o valor do pixel em 255.
                                else:
                                    matrizSaida[
                                        c, y, x
                                    ] = preto  # Seta o valor do pixel em 0.

            imagemSaida = Imagem()  # Cria um objeto do tipo Imagem
            imagemSaida.criarComMatriz(
                matrizSaida
            )  # Cria a imagem de saída com os dados da matriz de saída.
            imagemSaida.mostrar(
                janela, "Limiar com modulação ordenada periódico aglomerado"
            )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # O método de Limiar com Modulação Ordenada Periódico Disperso substitui cada pixel na imagem seguindo a seguinte regra:
    # Substitui por um pixel branco caso o valor do pixel for maior que o valor do
    # pixel da matriz de Dithering de entrada na posição Posição [i][j] sendo que
    # j = y % dimensao
    # i = x % dimensao
    # dimensao = len(matrizDithering)
    # ,ou por um pixel preto caso contrário.
    def limiarComModulacaoOrdenadaPeriodicoDisperso(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/limiarotimo.jpg"
            )  # Carrega a imagem do diretório
            matrizDithering = numpy.array(
                [[1, 2, 3], [3, 2, 1]]
            )  # Matriz de Dithering NXN
            nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
            altura = (
                imagemEntrada.getAltura()
            )  # Numero correspondente a Altura da Imagem
            largura = (
                imagemEntrada.getLargura()
            )  # Numero correspondente a Largura da Imagem

            entradaQuantizacao = 255  # Valor de entrada para quantização
            saidaQuantizacao = len(matrizDithering) * len(
                matrizDithering
            )  # Valor de saída quantização
            matrizQuantizada = self.quantizacao(
                imagemEntrada, entradaQuantizacao, saidaQuantizacao
            )  # Realiza a Quantização.

            matrizEntrada = (
                matrizQuantizada.getMatriz()
            )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
            matrizSaida = numpy.zeros(
                (nCanais, altura, largura)
            )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
            # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
            branco = 255  # 255 é o valor equivalente ao pixel branco
            preto = 0  # 0 é o valor equivalente ao pixel preto
            dimensao = len(matrizDithering)
            i = 0
            j = 0

            # Laços que percorrem cada pixel
            for c in range(
                nCanais
            ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    altura
                ):  # Laço de posição altura y - Laço que percorre todos os pixels no eixo y.
                    j = y % dimensao  # Resto da divisão inteira
                    for x in range(
                        largura
                    ):  # Laço de posição largura x -  Laço que percorre todos os pixels no eixo x.
                        i = x % dimensao  # Resto da divisão inteira
                        if (
                            matrizEntrada[c][y][x] > matrizDithering[i][j]
                        ):  # Se Valor do pixel é maior que valor da Posição [i][j] percorrendo a matrizDithering
                            matrizSaida[
                                c, y, x
                            ] = branco  # Seta o valor do pixel em 255.
                        else:
                            matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.

            imagemSaida = Imagem()  # Cria um objeto do tipo Imagem
            imagemSaida.criarComMatriz(
                matrizSaida
            )  # Cria a imagem de saída com os dados da matriz de saída.
            imagemSaida.mostrar(
                janela, "Limiar com modulação ordenada periódico disperso"
            )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # O método de Limiar com Modulação Aperiódico substitui cada pixel na imagem seguindo a seguinte regra:
    # Difunde o erro de quantização entre pixels vizinhos da imagem de entrada.
    # A Imagem é percorrida de cima para baixo, da esquerda para a direita.
    # Limiar é a média da imagem
    def limiarComModulacaoOrdenadaAperiodico(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/limiarotimo.jpg"
            )  # Carrega a imagem do diretório
            nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
            altura = (
                imagemEntrada.getAltura()
            )  # Numero correspondente a Altura da Imagem
            largura = (
                imagemEntrada.getLargura()
            )  # Numero correspondente a Largura da Imagem
            matriz = (
                imagemEntrada.getMatriz()
            )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
            matrizSaida = numpy.zeros(
                (nCanais, altura, largura)
            )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
            # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
            branco = 255  # 255 é o valor equivalente ao pixel branco
            preto = 0  # 0 é o valor equivalente ao pixel preto

            # limiar = 128;
            # limiar = 64; #Limiar para substituição
            # limiar = 32;
            # limiar = 16;
            limiar = (branco + preto) / 2
            # Limiar é a média da imagem
            erro = None  # Inicializa a variável erro.

            # Laços que percorrem cada pixel
            for c in range(
                nCanais
            ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
                for x in range(
                    largura - 1
                ):  # Laço que percorre todos os pixels no eixo x
                    for y in range(
                        altura - 1
                    ):  # Laço que percorre todos os pixels no eixo y.
                        if (
                            matriz[c][y][x] < limiar
                        ):  # Verifica se o valor do Pixel no canal c, altura y, largura x é menor que o limiar.
                            erro = matriz[c][y][x] - preto
                            matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                        else:
                            erro = matriz[c][y][x] - branco
                            matrizSaida[
                                c, y, x
                            ] = branco  # Seta o valor do pixel em 255.
                        matriz[c][y + 1][x] += int((3 / 8) * erro)
                        matriz[c][y][x + 1] += int((3 / 8) * erro)
                        matriz[c][y + 1][x + 1] += int((2 / 8) * erro)

            imagemSaida = Imagem()  # Cria um objeto do tipo Imagem
            imagemSaida.criarComMatriz(
                matrizSaida
            )  # Cria a imagem de saída com os dados da matriz de saída.
            imagemSaida.mostrar(
                janela, "Limiar com modulação ordenada aperiódico"
            )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # Erosão - Remove pixels que não possuem o padrão do Elemento Estruturante
    # Encolhe uma imagem. É expressa como a interseção da Imagem e Kernel.
    # Se todos os elementos do Kernel estiverem na Imagem, o pixel central do
    # Kernel é mantido na imagem de saída.
    def erosaoBin(self, bool=False):
        if self.msg["text"] == "Imagem":
            # Conjunto de pixels chamado de elemento estruturante (EE) ou kernel
            # Exemplo de Kernel em cruz
            kernel = numpy.array(
                [
                    [0, 0, 255, 0, 0],
                    [0, 0, 255, 0, 0],
                    [255, 255, 255, 255, 255],
                    [0, 0, 255, 0, 0],
                    [0, 0, 255, 0, 0],
                ]
            )
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar("img/b.png")  # Carrega a imagem do diretório
            nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
            altura = (
                imagemEntrada.getAltura()
            )  # Numero correspondente a Altura da Imagem
            largura = (
                imagemEntrada.getLargura()
            )  # Numero correspondente a Largura da Imagem
            matriz = (
                imagemEntrada.getMatriz()
            )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
            matrizSaida = numpy.zeros(
                (nCanais, altura, largura)
            )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
            # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
            raio = int((len(kernel) - 1) / 2)  # raio baseado no kernel
            temPerfil = False
            branco = 255  # 255 é o valor equivalente ao pixel branco
            preto = 0  # 0 é o valor equivalente ao pixel preto

            # Laços que percorrem cada pixel
            for c in range(
                nCanais
            ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    raio, altura - raio
                ):  # Laço que percorre todos os pixels no eixo y até o limiar do raio do kernel
                    for x in range(
                        raio, largura - raio
                    ):  # Laço que percorre todos os pixels no eixo x até o limiar do raio do kernel
                        for dy in range(-raio, raio + 1):
                            for dx in range(-raio, raio + 1):
                                if (
                                    kernel[dy + raio][dx + raio] == branco
                                ):  # Verifica se o valor do pixel é 255.
                                    if (
                                        matriz[c][y + dy][x + dx]
                                        != kernel[dy + raio][dx + raio]
                                    ):
                                        temPerfil = False

                        if temPerfil == False:
                            matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                        else:
                            matrizSaida[c, y, x] = matriz[c][y][
                                x
                            ]  # Pixel da imagem de entrada não se altera
                        temPerfil = True

            imagemSaida = Imagem()  # Cria um objeto do tipo Imagem
            imagemSaida._criarComMatriz(matrizSaida)
            if bool == True:
                imagemSaida.mostrar(
                    janela, "Imagem Fechamento"
                )  # Mostrar na tela a imagem tratada.
            else:
                imagemSaida.mostrar(
                    janela, "Imagem Erosao"
                )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # Dilatação - Insere pixels no conjunto de pixels que possuem o padrão do Elemento Estruturante
    def dilatacaoBin(self, bool=False):
        if self.msg["text"] == "Imagem":
            # Conjunto de pixels chamado de elemento estruturante (EE) ou kernel
            # Exemplo de Kernel em cruz
            kernel = numpy.array(
                [
                    [0, 0, 255, 0, 0],
                    [0, 0, 255, 0, 0],
                    [255, 255, 255, 255, 255],
                    [0, 0, 255, 0, 0],
                    [0, 0, 255, 0, 0],
                ]
            )
            imagemEntrada = Imagem()
            imagemEntrada.carregar("img/b.png")
            nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
            altura = (
                imagemEntrada.getAltura()
            )  # Numero correspondente a Altura da Imagem
            largura = (
                imagemEntrada.getLargura()
            )  # Numero correspondente a Largura da Imagem
            matriz = (
                imagemEntrada.getMatriz()
            )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
            matrizSaida = numpy.zeros(
                (nCanais, altura, largura)
            )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
            # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
            raio = int((len(kernel) - 1) / 2)
            temPerfil = False
            branco = 255  # 255 é o valor equivalente ao pixel branco
            preto = 0  # 0 é o valor equivalente ao pixel preto

            for c in range(
                nCanais
            ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    raio, altura - raio
                ):  # Laço que percorre todos os pixels no eixo y até o limiar do raio do kernel
                    for x in range(
                        raio, largura - raio
                    ):  # Laço que percorre todos os pixels no eixo x até o limiar do raio do kernel.
                        for z in range(-raio, raio + 1):
                            for w in range(-raio, raio + 1):
                                if (
                                    kernel[z + raio][w + raio] == branco
                                ):  # Verifica se o valor do pixel é 255.
                                    if (
                                        matriz[c][y + z][x + w]
                                        == kernel[z + raio][w + raio]
                                    ):
                                        temPerfil = True

                        if temPerfil == False:
                            matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                        else:
                            matrizSaida[
                                c, y, x
                            ] = branco  # Seta o valor do pixel em 255.
                        temPerfil = False

            imagem = Imagem()
            imagem._criarComMatriz(matrizSaida)
            if bool == True:
                imagem.mostrar(
                    janela, "Imagem Abertura"
                )  # Mostrar na tela a imagem tratada.
            else:
                imagem.mostrar(
                    janela, "Imagem Dilatação"
                )  # Mostrar na tela a imagem tratada.
            return imagem
        else:
            self.msg["text"] = "Imagem"

    # Erosão - Remove pixels que não possuem o padrão do Elemento Estruturante
    def erosaoBinParam(self, imagemEntrada: Imagem, mat):
        mat = numpy.array(
            [
                [255, 0, 0, 255, 0],
                [255, 0, 255, 0, 255],
                [0, 0, 255, 255, 0],
                [255, 0, 255, 0, 255],
            ]
        )
        nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
        altura = imagemEntrada.getAltura()  # Numero correspondente a Altura da Imagem
        largura = (
            imagemEntrada.getLargura()
        )  # Numero correspondente a Largura da Imagem
        matriz = (
            imagemEntrada.getMatriz()
        )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
        matrizSaida = numpy.zeros(
            (nCanais, altura, largura)
        )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
        # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
        raio = int((len(mat) - 1) / 2)
        temPerfil = False
        branco = 255  # 255 é o valor equivalente ao pixel branco
        preto = 0  # 0 é o valor equivalente ao pixel preto

        for c in range(nCanais):
            for y in range(
                raio, altura - raio
            ):  # Laço que percorre todos os pixels no eixo y até o limiar do raio do kernel
                for x in range(
                    raio, largura - raio
                ):  # Laço que percorre todos os pixels no eixo x até o limiar do raio do kernel.
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            if (
                                mat[dy + raio][dx + raio] == branco
                            ):  # Verifica se o valor do pixel é 255.
                                if (
                                    matriz[c][y + dy][x + dx]
                                    != mat[dy + raio][dx + raio]
                                ):
                                    temPerfil = False

                    if temPerfil == False:
                        matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                    else:
                        matrizSaida[c, y, x] = matriz[c][y][x]
                    temPerfil = True

        imagem = Imagem()
        imagem._criarComMatriz(matrizSaida)
        imagem.mostrar(janela, "Imagem Erosao")  # Mostrar na tela a imagem tratada.
        return imagem

    # Dilatação - Insere pixels no conjunto de pixels que possuem o padrão do Elemento Estruturante
    # Dilatação que recebe uma imagem como parâmetro
    def dilatacaoBinParam(self, img: Imagem, mat):
        nCanais = img.getNCanais()
        altura = img.getAltura()
        largura = img.getLargura()
        matriz = img.getMatriz()  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
        matrizSaida = numpy.zeros(
            (nCanais, altura, largura)
        )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
        # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
        raio = int((len(mat) - 1) / 2)
        temPerfil = False
        branco = 255  # 255 é o valor equivalente ao pixel branco
        preto = 0  # 0 é o valor equivalente ao pixel preto

        for c in range(
            nCanais
        ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                raio, altura - raio
            ):  # Laço que percorre todos os pixels no eixo y até o limiar do raio do kernel
                for x in range(
                    raio, largura - raio
                ):  # Laço que percorre todos os pixels no eixo x até o limiar do raio do kernel.
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            if (
                                mat[dy + raio][dx + raio] == branco
                            ):  # Verifica se o valor do pixel é 255.
                                if (
                                    matriz[c][y + dy][x + dx]
                                    == mat[dy + raio][dx + raio]
                                ):
                                    temPerfil = True

                    if temPerfil == False:
                        matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                    else:
                        matrizSaida[c, y, x] = branco  # Seta o valor do pixel em 255.
                    temPerfil = False

        imagem = Imagem()
        imagem._criarComMatriz(matrizSaida)
        imagem.mostrar(janela, "Imagem Dilatação")  # Mostrar na tela a imagem tratada.
        return imagem

    # Abertura Binária =  erosão -> dilatação (Realiza um erosão depois uma dilatação)
    # Abertura – suaviza o contorno de uma imagem.
    # Quebra estreitos e elimina proeminências delgadas.
    # É usada também para remover ruídos da imagem e abrir pequenos vazios ou espaços entre objetos próximos numa imagem .
    # Dada por uma erosão seguida de uma dilatação com o mesmo elemento estruturante.
    def aberturaBin(self):
        if self.msg["text"] == "Imagem":
            # Conjunto de pixels chamado de elemento estruturante (EE) ou kernel
            # Kenel com valores mais aleatórios para contrastar a imagem
            kernel = numpy.array(
                [
                    [255, 0, 0, 255, 0],
                    [255, 0, 255, 0, 255],
                    [0, 0, 255, 255, 0],
                    [255, 0, 255, 0, 255],
                ]
            )
            imagemEntrada = Imagem()
            imagemEntrada.carregar("img/b.png")

            erosao = self.erosaoBinParam(imagemEntrada, kernel)  # Realiza a erosão
            abertura = self.dilatacaoBinParam(
                erosao, kernel
            )  # Realiza a dilatação da erosão com o mesmo Kernel

            return abertura  # Retorna a abertura

        else:
            self.msg["text"] = "Imagem"

    # Fechamento Binário =  dilatação -> erosão (Realiza um dilatação depois uma erosão)
    # Closing – Funde pequenos quebras e alargas golfos estreitos.
    # Elimina pequenos orifícios. Irá preencher ou fechar os vazios.
    # Estas operações remover pixels brancos com ruídos.
    def fechamentoBin(self):
        if self.msg["text"] == "Imagem":
            # Conjunto de pixels chamado de elemento estruturante (EE) ou kernel
            # Kenel com valores mais aleatórios para contrastar a imagem
            kernel = numpy.array(
                [
                    [255, 0, 0, 255, 0],
                    [255, 0, 255, 0, 255],
                    [0, 0, 255, 255, 0],
                    [255, 0, 255, 0, 255],
                ]
            )
            imagemEntrada = Imagem()
            imagemEntrada.carregar("img/b.png")

            dilatacao = self.dilatacaoBinParam(
                imagemEntrada, kernel
            )  # Realiza a dilatação
            fechamento = self.erosaoBinParam(
                dilatacao, kernel
            )  # Realiza a erosão da dilatação com o mesmo Kernel

            return fechamento  # Retorna o fechamento

        else:
            self.msg["text"] = "Imagem"

    # Borda Interna - (Imagem - erosão(Imagem))
    # É a fronteira dada pela diferença entre a imagem original e sua erosão.
    def bordaInterna(self):
        if self.msg["text"] == "Imagem":
            # Conjunto de pixels chamado de elemento estruturante (EE) ou kernel
            # Exemplo de Kernel em cruz
            kernel = numpy.array(
                [
                    [0, 0, 255, 0, 0],
                    [0, 0, 255, 0, 0],
                    [255, 255, 255, 255, 255],
                    [0, 0, 255, 0, 0],
                    [0, 0, 255, 0, 0],
                ]
            )
            imagemEntrada = Imagem()
            imagemEntrada.carregar("img/b.png")
            imagemSaida = Imagem()

            erosao = self.erosaoBinParam(imagemEntrada, kernel)  # Realiza a erosao
            subtracao = self.subtracao(
                imagemEntrada, erosao
            )  # Realiza a subtracao da imagem de entrada pela erosao.

            imagemSaida._criarComMatriz(
                subtracao
            )  # Gera Imagem de saída com borda externa.

            imagemSaida.mostrar(
                janela, "Borda Interna"
            )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # Borda Externa - (dilatacao(Imagem) - Imagem)
    # É a fronteira dada pela diferença entre a imagem original e sua dilatação.
    def bordaExterna(self):
        if self.msg["text"] == "Imagem":
            # Conjunto de pixels chamado de elemento estruturante (EE) ou kernel
            # Exemplo de Kernel em cruz
            kernel = numpy.array(
                [
                    [0, 0, 255, 0, 0],
                    [0, 0, 255, 0, 0],
                    [255, 255, 255, 255, 255],
                    [0, 0, 255, 0, 0],
                    [0, 0, 255, 0, 0],
                ]
            )
            imagemEntrada = Imagem()
            imagemEntrada.carregar("img/b.png")
            imagemSaida = Imagem()

            dilatacao = self.dilatacaoBinParam(
                imagemEntrada, kernel
            )  # Realiza a dilatação
            subtracao = self.subtracao(
                dilatacao, imagemEntrada
            )  # Realiza a subtracao da dilatação pela imagem de entrada.

            imagemSaida._criarComMatriz(
                subtracao
            )  # Gera Imagem de saída com borda externa.
            imagemSaida.mostrar(janela, "Borda Externa")  # Mostra a imagem na tela.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # 1. Posiciona-se a origem do elemento estruturante sobre o primeiro pixel da imagem que sofre erosão.
    # 2. Calcula-se a diferença de cada par correspondente de valores de pixels do elemento estrutural e da imagem.
    # 3. Acha-se o valor mínimo de todas essas diferenças, e armazena-se o pixel correspondente na imagem de saída para este valor.
    # 4. Repete-se este processo para cada pixel da imagem que sofre erosão.
    def erosaoMon(self):
        if self.msg["text"] == "Imagem":
            matriz = numpy.array(
                [
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 16, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                ]
            )
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/lennaCinza.jpg"
            )  # Carrega a imagem do diretório
            imagemEntrada.toGray()
            nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
            altura = (
                imagemEntrada.getAltura()
            )  # Numero correspondente a Altura da Imagem
            largura = (
                imagemEntrada.getLargura()
            )  # Numero correspondente a Largura da Imagem
            matrizEntrada = (
                imagemEntrada.getMatriz()
            )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
            matrizSaida = numpy.zeros(
                (nCanais, altura, largura)
            )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
            # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
            raio = int((len(matriz) - 1) / 2)
            valorMinimo = 800000000000000000
            preto = 0  # 0 é o valor equivalente ao pixel preto

            # Laços que percorrem cada pixel
            for c in range(
                nCanais
            ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    (raio), (altura - raio)
                ):  # Laço que percorre todos os pixels no eixo y até o limiar do raio do kernel
                    for x in range(
                        (raio), (largura - raio)
                    ):  # Laço que percorre todos os pixels no eixo x até o limiar do raio do kernel.
                        for dy in range((-raio), (raio + 1)):
                            for dx in range((-raio), (raio + 1)):
                                if (
                                    valorMinimo
                                    > matrizEntrada[c][y + dy][x + dx]
                                    + matriz[(dy + raio)][(dx + raio)]
                                ):
                                    valorMinimo = (
                                        matrizEntrada[c][y + dy][x + dx]
                                        + matriz[(dy + raio)][(dx + raio)]
                                    )
                        if valorMinimo > preto:
                            matrizSaida[c, y, x] = valorMinimo
                        else:
                            matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                        valorMinimo = 800000000000000000
            imagem = Imagem()  # Cria um objeto do tipo Imagem
            imagem.criarComMatriz(matrizSaida)  # Gera imagem de saída.
            imagem.mostrar(janela, "Erosão Mon")  # Mostrar na tela a imagem tratada.
            return imagem.criarComMatriz(matrizSaida)
        else:
            self.msg["text"] = "Imagem"

    # 1. Posiciona-se a origem do elemento estrutural sobre o primeiro pixel da imagem a ser dilatada.
    # 2. Calcula-se a soma de cada par correspondente de valores de pixels do elemento estrutural e da imagem.
    # 3. Acha-se o valor máximo de todas essas somas, e armazena-se o pixel correspondente na imagem de saída para este valor.
    # 4. Repete-se este processo para cada pixel da imagem a ser dilatada.
    def dilatacaoMon(self):
        if self.msg["text"] == "Imagem":
            matriz = numpy.array(
                [
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 16, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                ]
            )
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/lennaCinza.jpg"
            )  # Carrega a imagem do diretório
            imagemEntrada.toGray()
            nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
            altura = (
                imagemEntrada.getAltura()
            )  # Numero correspondente a Altura da Imagem
            largura = (
                imagemEntrada.getLargura()
            )  # Numero correspondente a Largura da Imagem
            matrizEntrada = (
                imagemEntrada.getMatriz()
            )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
            matrizSaida = numpy.zeros(
                (nCanais, altura, largura)
            )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
            # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
            raio = int((len(matriz) - 1) / 2)
            valorMaximo = -800000000000000000
            preto = 0  # 0 é o valor equivalente ao pixel preto

            # Laços que percorrem cada pixel
            for c in range(
                nCanais
            ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    raio, altura - raio
                ):  # Laço que percorre todos os pixels no eixo y até o limiar do raio do kernel
                    for x in range(
                        raio, largura - raio
                    ):  # Laço que percorre todos os pixels no eixo x até o limiar do raio do kernel.
                        for dy in range(-raio, raio + 1):
                            for dx in range(-raio, raio + 1):
                                if (
                                    valorMaximo
                                    < matrizEntrada[c][y + dy][x + dx]
                                    + matriz[dy + raio][dx + raio]
                                ):
                                    valorMaximo = (
                                        matrizEntrada[c][y + dy][x + dx]
                                        + matriz[dy + raio][dx + raio]
                                    )
                        if valorMaximo > preto:
                            matrizSaida[c, y, x] = valorMaximo
                        else:
                            matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                        valorMaximo = -800000000000000000
            imagem = Imagem()  # Cria um objeto do tipo Imagem
            imagem.criarComMatriz(matrizSaida)  # Gera imagem de saída.
            imagem.mostrar(janela, "Dilatação Mon")  # Mostrar na tela a imagem tratada.
            return imagem.criarComMatriz(matrizSaida)
        else:
            self.msg["text"] = "Imagem"

    # Método erosao que aceita uma imagem de entrada como parâmetro
    def erosaoMonParam(self, imagemEntrada: Imagem, kernel):
        nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
        altura = imagemEntrada.getAltura()  # Numero correspondente a Altura da Imagem
        largura = (
            imagemEntrada.getLargura()
        )  # Numero correspondente a Largura da Imagem
        matrizEntrada = (
            imagemEntrada.getMatriz()
        )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
        matrizSaida = numpy.zeros(
            (nCanais, altura, largura)
        )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
        # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
        raio = int((len(kernel) - 1) / 2)
        valorMinimo = 800000000000000000
        preto = 0  # 0 é o valor equivalente ao pixel preto

        # Laços que percorrem cada pixel
        for c in range(
            nCanais
        ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                (raio), (altura - raio)
            ):  # Laço que percorre todos os pixels no eixo y até o limiar do raio do kernel
                for x in range(
                    (raio), (largura - raio)
                ):  # Laço que percorre todos os pixels no eixo x até o limiar do raio do kernel.
                    for dy in range((-raio), (raio + 1)):
                        for dx in range((-raio), (raio + 1)):
                            if (
                                valorMinimo
                                > matrizEntrada[c][y + dy][x + dx]
                                + kernel[(dy + raio)][(dx + raio)]
                            ):
                                valorMinimo = (
                                    matrizEntrada[c][y + dy][x + dx]
                                    + kernel[(dy + raio)][(dx + raio)]
                                )

                    if valorMinimo > preto:
                        matrizSaida[c, y, x] = valorMinimo
                    else:
                        matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.

                    valorMinimo = 800000000000000000

        imagem = Imagem()  # Cria um objeto do tipo Imagem
        imagem.criarComMatriz(matrizSaida)  # Gera imagem de saída.
        return imagem

    # Método dilatacao que aceita uma imagem de entrada como parâmetro
    def dilatacaoMonParam(self, imagemEntrada: Imagem, kernel):
        nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
        altura = imagemEntrada.getAltura()  # Numero correspondente a Altura da Imagem
        largura = (
            imagemEntrada.getLargura()
        )  # Numero correspondente a Largura da Imagem
        matrizEntrada = (
            imagemEntrada.getMatriz()
        )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
        matrizSaida = numpy.zeros(
            (nCanais, altura, largura)
        )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
        # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
        raio = int((len(kernel) - 1) / 2)
        valorMaximo = -800000000000000000
        preto = 0  # 0 é o valor equivalente ao pixel preto

        # Laços que percorrem cada pixel
        for c in range(
            nCanais
        ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                raio, altura - raio
            ):  # Laço que percorre todos os pixels no eixo y até o limiar do raio do kernel
                for x in range(
                    raio, largura - raio
                ):  # Laço que percorre todos os pixels no eixo x até o limiar do raio do kernel.
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            if (
                                valorMaximo
                                < matrizEntrada[c][y + dy][x + dx]
                                + kernel[dy + raio][dx + raio]
                            ):
                                valorMaximo = (
                                    matrizEntrada[c][y + dy][x + dx]
                                    + kernel[dy + raio][dx + raio]
                                )
                    if valorMaximo > preto:
                        matrizSaida[c, y, x] = valorMaximo
                    else:
                        matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                    valorMaximo = -800000000000000000

        imagem = Imagem()  # Cria um objeto do tipo Imagem
        imagem.criarComMatriz(matrizSaida)  # Gera imagem de saída.
        return imagem

    # Método erosão que aceita uma imagem de entrada como parâmetro
    # E é utilizado no método de fechamento
    def erosaoMonFechamento(self, imagemEntrada: Imagem, kernel):
        nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
        altura = imagemEntrada.getAltura()  # Numero correspondente a Altura da Imagem
        largura = (
            imagemEntrada.getLargura()
        )  # Numero correspondente a Largura da Imagem
        matrizEntrada = (
            imagemEntrada.getMatriz()
        )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
        matrizSaida = numpy.zeros(
            (nCanais, altura, largura)
        )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
        # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
        raio = int((len(kernel) - 1) / 2)
        valorMinimo = 800000000000000000
        preto = 0  # 0 é o valor equivalente ao pixel preto

        # Laços que percorrem cada pixel
        for c in range(
            nCanais
        ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                (raio), (altura - raio)
            ):  # Laço que percorre todos os pixels no eixo y até o limiar do raio do kernel
                for x in range(
                    (raio), (largura - raio)
                ):  # Laço que percorre todos os pixels no eixo x até o limiar do raio do kernel.
                    for dy in range((-raio), (raio + 1)):
                        for dx in range((-raio), (raio + 1)):
                            if (
                                valorMinimo
                                > matrizEntrada[c][y + dy][x + dx]
                                + kernel[(dy + raio)][(dx + raio)]
                            ):
                                valorMinimo = (
                                    matrizEntrada[c][y + dy][x + dx]
                                    + kernel[(dy + raio)][(dx + raio)]
                                )
                    if valorMinimo > preto:
                        matrizSaida[c, y, x] = valorMinimo
                    else:
                        matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                    valorMinimo = 800000000000000000
        imagem = Imagem()  # Cria um objeto do tipo Imagem
        imagem.criarComMatriz(matrizSaida)  # Gera imagem de saída.
        imagem.mostrar(janela, "Fechamento Mon")  # Mostrar na tela a imagem tratada.
        return imagem.criarComMatriz(matrizSaida)

    # Método dilatacao que aceita uma imagem de entrada como parâmetro
    # E é utilizado no método de abertura
    def dilatacaoMonAbertura(self, imagemEntrada: Imagem, kernel):
        nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
        altura = imagemEntrada.getAltura()  # Numero correspondente a Altura da Imagem
        largura = (
            imagemEntrada.getLargura()
        )  # Numero correspondente a Largura da Imagem
        matrizEntrada = (
            imagemEntrada.getMatriz()
        )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
        matrizSaida = numpy.zeros(
            (nCanais, altura, largura)
        )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
        # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
        raio = int((len(kernel) - 1) / 2)
        valorMaximo = -800000000000000000
        preto = 0  # 0 é o valor equivalente ao pixel preto

        # Laços que percorrem cada pixel
        for c in range(
            nCanais
        ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                raio, altura - raio
            ):  # Laço que percorre todos os pixels no eixo y até o limiar do raio do kernel
                for x in range(
                    raio, largura - raio
                ):  # Laço que percorre todos os pixels no eixo x até o limiar do raio do kernel.
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            if (
                                valorMaximo
                                < matrizEntrada[c][y + dy][x + dx]
                                + kernel[dy + raio][dx + raio]
                            ):
                                valorMaximo = (
                                    matrizEntrada[c][y + dy][x + dx]
                                    + kernel[dy + raio][dx + raio]
                                )
                    if valorMaximo > preto:
                        matrizSaida[c, y, x] = valorMaximo
                    else:
                        matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                    valorMaximo = -800000000000000000
        imagem = Imagem()  # Cria um objeto do tipo Imagem
        imagem.criarComMatriz(matrizSaida)  # Gera imagem de saída.
        imagem.mostrar(janela, "Abertura Mon")  # Mostrar na tela a imagem tratada.

    # Abertura Monocromática =  erosão -> dilatação (Realiza um erosão depois uma dilatação)
    # A abertura em tons de cinza funciona como a abertura binária combinando as duas operações de erosão e dilatação em seqüência.
    # A diferença é que a propriedade da idempotência não se aplica:
    # várias aberturas seguidas produzem um resultado mais acentuado do que uma única abertura.
    def aberturaMon(self):
        if self.msg["text"] == "Imagem":
            # Conjunto de pixels chamado de elemento estruturante (EE) ou kernel
            kernel = numpy.array(
                [
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 16, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                ]
            )
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/lennaCinza.jpg"
            )  # Carrega a imagem do diretório

            erosao = self.erosaoMonParam(imagemEntrada, kernel)  # Realiza a erosão
            abertura = self.dilatacaoMonAbertura(
                erosao, kernel
            )  # Realiza a dilatação da erosão com o mesmo Kernel

            return abertura  # Retorna a abertura
        else:
            self.msg["text"] = "Imagem"

    # Método abertura que aceita uma imagem de entrada como parâmetro
    def aberturaMonParam(self, imagemEntrada: Imagem, kernel):
        return self.dilatacaoMonAbertura(
            self.erosaoMonParam(imagemEntrada, kernel),
            kernel,
        )

    # Fechamento Monocromático =  dilatação -> erosão (Realiza um dilatação depois uma erosão)
    # O fechamento em tons de cinza funciona como o fechamento binário combinando as duas operações de dilatação e erosão em seqüência.
    # A diferença é que a propriedade da idempotência não se aplica:
    # Vários fechamentos seguidos produzem uum resultado mais acentuado do que um único fechamento.
    def fechamentoMon(self):
        if self.msg["text"] == "Imagem":
            # Conjunto de pixels chamado de elemento estruturante (EE) ou kernel
            kernel = numpy.array(
                [
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 16, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                ]
            )
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/lennaCinza.jpg"
            )  # Carrega a imagem do diretório

            dilatacao = self.dilatacaoMonParam(
                imagemEntrada, kernel
            )  # Realiza a dilatação
            fechamento = self.erosaoMonFechamento(
                dilatacao, kernel
            )  # Realiza a erosão da dilatação com o mesmo Kernel

            return fechamento  # Retorna o fechamento
        else:
            self.msg["text"] = "Imagem"

    # Método fechamento que aceita uma imagem de entrada como parâmetro
    def fechamentoMonParam(self, imagemEntrada: Imagem, kernel):
        return self.erosaoMonFechamento(
            self.dilatacaoMonParam(imagemEntrada, kernel),
            kernel,
        )

    def subtracaoMon(self, imgA: Imagem, imgB: Imagem):
        nCanais = imgA.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
        altura = imgA.getAltura()  # Numero correspondente a Altura da Imagem
        largura = imgA.getLargura()  # Numero correspondente a Largura da Imagem
        matA = imgA.getMatriz()  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
        matB = imgB.getMatriz()  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))

        cor = None
        matrizSaida = numpy.zeros(
            (nCanais, altura, largura)
        )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
        # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
        # Laços que percorrem cada pixel
        for c in range(
            nCanais
        ):  # Laço que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(altura):  # Laço de posição altura y
                for x in range(largura):  # Laço de posição altura x
                    cor = matA[c][y][x] - matB[c][y][x]
                    if cor < 0:  # Evita estouro para números negativos
                        cor = 0  # Seta zero caso seja um número negativo
                    matrizSaida[
                        c, y, x
                    ] = cor  # Seta resultado da subtração no pixel atual.

        imagem = Imagem()  # Cria um objeto do tipo Imagem
        imagem.criarComMatriz(matrizSaida)  # Gera imagem de saída.
        imagem.mostrar(janela, "Subtração")  # Mostrar na tela a imagem tratada.
        return imagem.criarComMatriz(matrizSaida)

    # Gradiente = Dilatação - erosão (O resultado é a subtração da dilatação pela erosão)
    # Outra forma de encontrar a borda.
    # Composta de três outras operações básicas: Dilatação, erosão e a subtração.
    # A imagem é dilatada e erodida pelo mesmo kernel e o resultado erodido é subtraído do resultado dilatado.
    # Resulta em uma borda maior e mais confiável.
    def gradiente(self):
        if self.msg["text"] == "Imagem":
            # Conjunto de pixels chamado de elemento estruturante (EE) ou kernel
            kernel = numpy.array(
                [
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 62, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                ]
            )
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/lennaCinza.jpg"
            )  # Carrega a imagem do diretório
            imagem = Imagem()  # Cria um objeto do tipo Imagem

            dilatacao = self.dilatacaoMonParam(
                imagemEntrada, kernel
            )  # Realiza a dilatacao
            erosao = self.erosaoMonParam(imagemEntrada, kernel)  # Realiza a erosão
            subtracao = self.subtracaoMon(
                dilatacao, erosao
            )  # Realiza a subtracao da dilatação pela erosão
            imagem.criarComMatriz(subtracao)  # Cria a imagem de saída

            return imagem.mostrar(
                janela, "Gradiente"
            )  # Mostrar na tela a imagem tratada.
        else:
            self.msg["text"] = "Imagem"

    # Smoothing - abertura -> fechamento (Realiza uma abertura depois um fechamento)
    def smoothing(self):
        if self.msg["text"] == "Imagem":
            # Conjunto de pixels chamado de elemento estruturante (EE) ou kernel
            kernel = numpy.array(
                [
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 16, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                ]
            )
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/lennaCinza.jpg"
            )  # Carrega a imagem do diretório

            abertura = self.aberturaMonParam(
                imagemEntrada, kernel
            )  # Realiza a abertura
            smoothing = self.fechamentoMonParam(
                abertura, kernel
            )  # Realiza o fechamento da abertura com o mesmo Kernel

            return smoothing  # Retorna a imagem com o efeito de smoothing
        else:
            self.msg["text"] = "Imagem"


janela = Tk()
Application(janela)
janela.mainloop()
