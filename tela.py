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
        self.b10["text"] = "Eros??o - Morfologia matem??tica bin??ria"
        self.b10["font"] = ("Calibri", "9")
        self.b10["width"] = 55
        self.b10["command"] = self.erosaoBin
        self.b10.pack()

        self.b11 = Button(self.widget1)
        self.b11["text"] = "Dilata????o - Morfologia matem??tica bin??ria"
        self.b11["font"] = ("Calibri", "9")
        self.b11["width"] = 55
        self.b11["command"] = self.dilatacaoBin
        self.b11.pack()

        self.b12 = Button(self.widget1)
        self.b12["text"] = "Abertura - Morfologia matem??tica bin??ria"
        self.b12["font"] = ("Calibri", "9")
        self.b12["width"] = 55
        self.b12["command"] = self.aberturaBin
        self.b12.pack()

        self.b13 = Button(self.widget1)
        self.b13["text"] = "Fechamento - Morfologia matem??tica bin??ria"
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
        self.b16["text"] = "Eros??o - Morfologia matem??tica monocrom??tica"
        self.b16["font"] = ("Calibri", "9")
        self.b16["width"] = 55
        self.b16["command"] = self.erosaoMon
        self.b16.pack()

        self.b17 = Button(self.widget1)
        self.b17["text"] = "Dilata????o - Morfologia matem??tica monocrom??tica"
        self.b17["font"] = ("Calibri", "9")
        self.b17["width"] = 55
        self.b17["command"] = self.dilatacaoMon
        self.b17.pack()

        self.b18 = Button(self.widget1)
        self.b18["text"] = "Abertura - Morfologia matem??tica monocrom??tica"
        self.b18["font"] = ("Calibri", "9")
        self.b18["width"] = 55
        self.b18["command"] = self.aberturaMon
        self.b18.pack()

        self.b19 = Button(self.widget1)
        self.b19["text"] = "Fechamento - Morfologia matem??tica monocrom??tica"
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
            img1.carregar("img/lenna.png")  # Carrega a imagem do diret??rio
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
                janela, "Criando atrav??s de uma matriz pr??-existente"
            )  # Mostrar na tela a imagem tratada.
        else:
            self.msg["text"] = "Imagem"

    def converteParaRgb(self):
        if self.msg["text"] == "Imagem":
            img4 = Imagem()  # Cria um objeto do tipo Imagem
            img4.carregar("img/lenna.png")  # Carrega a imagem do diret??rio
            img4.mostrar(janela)  # Mostrar na tela a imagem tratada.
            img4.toRGB()
            img4.mostrar(janela)  # Mostrar na tela a imagem tratada.
        else:
            self.msg["text"] = "Imagem"

    def converteParaCinza(self):
        if self.msg["text"] == "Imagem":
            img4 = Imagem()  # Cria um objeto do tipo Imagem
            img4.carregar("img/lennaRGB.jpg")  # Carrega a imagem do diret??rio
            img4.mostrar(janela)  # Mostrar na tela a imagem tratada.
            img4.toGray()
            img4.mostrar(janela)  # Mostrar na tela a imagem tratada.
        else:
            self.msg["text"] = "Imagem"

    def getMatriz(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            # imagemEntrada.carregar('img/olho.png') #Carrega a imagem do diret??rio
            imagemEntrada.carregar("img/lennaRGB.jpg")  # Carrega a imagem do diret??rio
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
            imagemEntrada.carregar("img/lennaRGB.jpg")  # Carrega a imagem do diret??rio
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

        cor = None  # Inicializa vari??vel cor.
        matrizSaida = numpy.zeros(
            (nCanais, altura, largura)
        )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
        # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
        # La??os que percorrem cada pixel
        for c in range(
            nCanais
        ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                altura
            ):  # La??o de posi????o altura y - La??o que percorre todos os pixels no eixo y.
                for x in range(
                    largura
                ):  # La??o de posi????o largura x -  La??o que percorre todos os pixels no eixo x.
                    cor = matA[c][y][x] - matB[c - 1][y - 1][x - 1]  # Realiza subtra????o
                    if cor < 0:  # Evita estouro para n??meros negativos
                        cor = 0  # Seta zero caso seja um n??mero negativo
                    matrizSaida[
                        c, y, x
                    ] = cor  # Seta resultado da subtra????o no pixel atual.

        return matrizSaida

    # A limiariza????o converte uma imagem em n??veis de cinza ou colorida numa imagem bin??ria,
    # baseado somente no valor do pixel.

    # O m??todo de limiar simples substitui cada pixel na imagem seguindo a seguinte regra:
    # Substitui por um pixel preto se f(i,j) for menor que o limiar, ou por um pixel branco caso contr??rio.
    def limiarSimples(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/limiarotimo.jpg"
            )  # Carrega a imagem do diret??rio
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
            branco = 255  # 255 ?? o valor equivalente ao pixel branco
            preto = 0  # 0 ?? o valor equivalente ao pixel preto # 0 ?? o valor equivalente ao pixel preto

            # limiar = 128;
            limiar = 64
            # Limiar para substitui????o
            # limiar = 32;
            # limiar = 16;

            # La??os que percorrem cada pixel
            for c in range(
                nCanais
            ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    altura
                ):  # La??o de posi????o altura y - La??o que percorre todos os pixels no eixo y.
                    for x in range(
                        largura
                    ):  # La??o de posi????o altura x - La??o que percorre todos os pixels no eixo x.
                        if (
                            matriz[c][y][x] < limiar
                        ):  # Verifica se o valor do Pixel no canal c, altura y, largura x ?? menor que o limiar.
                            matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                        else:
                            matrizSaida[
                                c, y, x
                            ] = branco  # Seta o valor do pixel em 255.

            imagemSaida = Imagem()  # Cria um objeto do tipo Imagem
            imagemSaida.criarComMatriz(
                matrizSaida
            )  # Cria a imagem de sa??da com os dados da matriz de sa??da.
            imagemSaida.mostrar(
                janela, "Limiar Simples"
            )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # O m??todo de Limiar com Modula????o Aleat??ria substitui cada pixel na imagem seguindo a seguinte regra:
    # Substitui por um pixel preto caso o valor de temp (temp = pixel - valorAleat??rio)
    # for menor que o limiar, ou por um pixel branco caso contr??rio.
    def limiarComModulacaoAleatoria(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/limiarotimo.jpg"
            )  # Carrega a imagem do diret??rio
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
            branco = 255  # 255 ?? o valor equivalente ao pixel branco
            preto = 0  # 0 ?? o valor equivalente ao pixel preto

            # limiar = 128;
            limiar = 64
            # Limiar para substitui????o
            # limiar = 32;
            # limiar = 16;
            # limiar = (branco + preto)/2;

            # La??os que percorrem cada pixel
            for c in range(
                nCanais
            ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    altura
                ):  # La??o de posi????o altura y -  La??o que percorre todos os pixels no eixo y.
                    for x in range(
                        largura
                    ):  # La??o de posi????o largura x -  La??o que percorre todos os pixels no eixo x.
                        temp = matriz[c][y][x] + randrange(
                            -255, 255
                        )  # Soma o valor do Pixel no canal c, altura y, largura x
                        # com um n??mero aleat??rio no intervalo de -255 a 255.
                        if (
                            temp < limiar
                        ):  # Verifica se o valor do Pixel resultante ?? menor que o limiar.
                            matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.
                        else:
                            matrizSaida[
                                c, y, x
                            ] = branco  # Seta o valor do pixel em 255.

            imagemSaida = Imagem()  # Cria um objeto do tipo Imagem
            imagemSaida.criarComMatriz(
                matrizSaida
            )  # Cria a imagem de sa??da com os dados da matriz de sa??da.
            imagemSaida.mostrar(
                janela, "Limiar com modula????o aleat??ria"
            )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    def quantizacao(self, imagemEntrada: Imagem, entrada, saida):
        imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
        imagemEntrada.carregar("img/limiarotimo.jpg")  # Carrega a imagem do diret??rio
        faixa = int(
            entrada / saida
        )  # Determina a faixa do intervalo entre entrada e sa??da
        matriz = (
            imagemEntrada.getMatriz()
        )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
        nCanais = imagemEntrada.getNCanais()  # Indice Canais 3 (RGB) ou 1 (CINZA)
        altura = imagemEntrada.getAltura()  # Numero correspondente a Altura da Imagem
        largura = (
            imagemEntrada.getLargura()
        )  # Numero correspondente a Largura da Imagem

        # La??os que percorrem cada pixel
        for c in range(
            nCanais
        ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                altura
            ):  # La??o de posi????o altura y - La??o que percorre todos os pixels no eixo y.
                for x in range(
                    largura
                ):  # La??o de posi????o largura x -  La??o que percorre todos os pixels no eixo x.
                    color = int(
                        matriz[c][y][x] / faixa
                    )  # Valor do pixel ?? o valor atual dividido pelo valor da faixa
                    matriz[c][y][x] = color

        imagemSaida = Imagem()  # Cria um objeto do tipo Imagem
        imagemSaida.criarComMatriz(
            matriz
        )  # Cria a imagem de sa??da com os dados da matriz de sa??da.
        return imagemSaida

    # O m??todo de Limiar com Modula????o Ordenada Peri??dico Aglomerado substitui cada pixel na imagem seguindo a seguinte regra:
    # Substitui por um pixel branco caso o valor do pixel for maior que o valor do
    # pixel da matriz de Dithering de entrada, ou por um pixel preto caso contr??rio.
    # Inicialmente deve-se quantizar a imagem para NxN + 1 n??veis.
    # A Imagem de sa??da ser?? maior que a de entrada.
    def limiarComModulacaoOrdenadaPeriodicoAglomerado(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/limiarotimo.jpg"
            )  # Carrega a imagem do diret??rio
            matrizDithering = numpy.array(
                [[2, 2, 2], [2, 2, 2]]
            )  # Matriz de Dithering NXN

            entradaQuantizacao = 255  # Valor de entrada para quantiza????o
            saidaQuantizacao = (
                len(matrizDithering) * len(matrizDithering) + 1
            )  # Valor de sa??da quantiza????o
            matrizQuantizada = self.quantizacao(
                imagemEntrada, entradaQuantizacao, saidaQuantizacao
            )  # Realiza a Quantiza????o.

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
            branco = 255  # 255 ?? o valor equivalente ao pixel branco
            preto = 0  # 0 ?? o valor equivalente ao pixel preto

            # La??os que percorrem cada pixel
            for c in range(
                nCanais
            ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    altura
                ):  # La??o de posi????o altura y - La??o que percorre todos os pixels no eixo y.
                    for x in range(
                        largura
                    ):  # La??o de posi????o largura x -  La??o que percorre todos os pixels no eixo x.
                        for d in range(
                            len(matrizDithering)
                        ):  # La??o que percorre o tamanho da matrizDithering
                            for i in range(
                                len(matrizDithering[d])
                            ):  # Posi????o i percorrendo a matrizDithering
                                if (
                                    matrizEntrada[c][y][x] > matrizDithering[d][i]
                                ):  # Se Valor do pixel ?? maior que valor da Posi????o [d][i] percorrendo a matrizDithering
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
            )  # Cria a imagem de sa??da com os dados da matriz de sa??da.
            imagemSaida.mostrar(
                janela, "Limiar com modula????o ordenada peri??dico aglomerado"
            )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # O m??todo de Limiar com Modula????o Ordenada Peri??dico Disperso substitui cada pixel na imagem seguindo a seguinte regra:
    # Substitui por um pixel branco caso o valor do pixel for maior que o valor do
    # pixel da matriz de Dithering de entrada na posi????o Posi????o [i][j] sendo que
    # j = y % dimensao
    # i = x % dimensao
    # dimensao = len(matrizDithering)
    # ,ou por um pixel preto caso contr??rio.
    def limiarComModulacaoOrdenadaPeriodicoDisperso(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/limiarotimo.jpg"
            )  # Carrega a imagem do diret??rio
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

            entradaQuantizacao = 255  # Valor de entrada para quantiza????o
            saidaQuantizacao = len(matrizDithering) * len(
                matrizDithering
            )  # Valor de sa??da quantiza????o
            matrizQuantizada = self.quantizacao(
                imagemEntrada, entradaQuantizacao, saidaQuantizacao
            )  # Realiza a Quantiza????o.

            matrizEntrada = (
                matrizQuantizada.getMatriz()
            )  # Matriz dos (3 Canais (1, 2 e 3 - RGB) ou 1 (CINZA))
            matrizSaida = numpy.zeros(
                (nCanais, altura, largura)
            )  # Gera uma matriz de saida zerada com a mesma quantidade de canais, altura e largura.
            # Ex: np.zeros(5) array([ 0.,  0.,  0.,  0.,  0.])
            branco = 255  # 255 ?? o valor equivalente ao pixel branco
            preto = 0  # 0 ?? o valor equivalente ao pixel preto
            dimensao = len(matrizDithering)
            i = 0
            j = 0

            # La??os que percorrem cada pixel
            for c in range(
                nCanais
            ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    altura
                ):  # La??o de posi????o altura y - La??o que percorre todos os pixels no eixo y.
                    j = y % dimensao  # Resto da divis??o inteira
                    for x in range(
                        largura
                    ):  # La??o de posi????o largura x -  La??o que percorre todos os pixels no eixo x.
                        i = x % dimensao  # Resto da divis??o inteira
                        if (
                            matrizEntrada[c][y][x] > matrizDithering[i][j]
                        ):  # Se Valor do pixel ?? maior que valor da Posi????o [i][j] percorrendo a matrizDithering
                            matrizSaida[
                                c, y, x
                            ] = branco  # Seta o valor do pixel em 255.
                        else:
                            matrizSaida[c, y, x] = preto  # Seta o valor do pixel em 0.

            imagemSaida = Imagem()  # Cria um objeto do tipo Imagem
            imagemSaida.criarComMatriz(
                matrizSaida
            )  # Cria a imagem de sa??da com os dados da matriz de sa??da.
            imagemSaida.mostrar(
                janela, "Limiar com modula????o ordenada peri??dico disperso"
            )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # O m??todo de Limiar com Modula????o Aperi??dico substitui cada pixel na imagem seguindo a seguinte regra:
    # Difunde o erro de quantiza????o entre pixels vizinhos da imagem de entrada.
    # A Imagem ?? percorrida de cima para baixo, da esquerda para a direita.
    # Limiar ?? a m??dia da imagem
    def limiarComModulacaoOrdenadaAperiodico(self):
        if self.msg["text"] == "Imagem":
            imagemEntrada = Imagem()  # Cria um objeto do tipo Imagem
            imagemEntrada.carregar(
                "img/limiarotimo.jpg"
            )  # Carrega a imagem do diret??rio
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
            branco = 255  # 255 ?? o valor equivalente ao pixel branco
            preto = 0  # 0 ?? o valor equivalente ao pixel preto

            # limiar = 128;
            # limiar = 64; #Limiar para substitui????o
            # limiar = 32;
            # limiar = 16;
            limiar = (branco + preto) / 2
            # Limiar ?? a m??dia da imagem
            erro = None  # Inicializa a vari??vel erro.

            # La??os que percorrem cada pixel
            for c in range(
                nCanais
            ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
                for x in range(
                    largura - 1
                ):  # La??o que percorre todos os pixels no eixo x
                    for y in range(
                        altura - 1
                    ):  # La??o que percorre todos os pixels no eixo y.
                        if (
                            matriz[c][y][x] < limiar
                        ):  # Verifica se o valor do Pixel no canal c, altura y, largura x ?? menor que o limiar.
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
            )  # Cria a imagem de sa??da com os dados da matriz de sa??da.
            imagemSaida.mostrar(
                janela, "Limiar com modula????o ordenada aperi??dico"
            )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # Eros??o - Remove pixels que n??o possuem o padr??o do Elemento Estruturante
    # Encolhe uma imagem. ?? expressa como a interse????o da Imagem e Kernel.
    # Se todos os elementos do Kernel estiverem na Imagem, o pixel central do
    # Kernel ?? mantido na imagem de sa??da.
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
            imagemEntrada.carregar("img/b.png")  # Carrega a imagem do diret??rio
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
            branco = 255  # 255 ?? o valor equivalente ao pixel branco
            preto = 0  # 0 ?? o valor equivalente ao pixel preto

            # La??os que percorrem cada pixel
            for c in range(
                nCanais
            ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    raio, altura - raio
                ):  # La??o que percorre todos os pixels no eixo y at?? o limiar do raio do kernel
                    for x in range(
                        raio, largura - raio
                    ):  # La??o que percorre todos os pixels no eixo x at?? o limiar do raio do kernel
                        for dy in range(-raio, raio + 1):
                            for dx in range(-raio, raio + 1):
                                if (
                                    kernel[dy + raio][dx + raio] == branco
                                ):  # Verifica se o valor do pixel ?? 255.
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
                            ]  # Pixel da imagem de entrada n??o se altera
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

    # Dilata????o - Insere pixels no conjunto de pixels que possuem o padr??o do Elemento Estruturante
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
            branco = 255  # 255 ?? o valor equivalente ao pixel branco
            preto = 0  # 0 ?? o valor equivalente ao pixel preto

            for c in range(
                nCanais
            ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    raio, altura - raio
                ):  # La??o que percorre todos os pixels no eixo y at?? o limiar do raio do kernel
                    for x in range(
                        raio, largura - raio
                    ):  # La??o que percorre todos os pixels no eixo x at?? o limiar do raio do kernel.
                        for z in range(-raio, raio + 1):
                            for w in range(-raio, raio + 1):
                                if (
                                    kernel[z + raio][w + raio] == branco
                                ):  # Verifica se o valor do pixel ?? 255.
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
                    janela, "Imagem Dilata????o"
                )  # Mostrar na tela a imagem tratada.
            return imagem
        else:
            self.msg["text"] = "Imagem"

    # Eros??o - Remove pixels que n??o possuem o padr??o do Elemento Estruturante
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
        branco = 255  # 255 ?? o valor equivalente ao pixel branco
        preto = 0  # 0 ?? o valor equivalente ao pixel preto

        for c in range(nCanais):
            for y in range(
                raio, altura - raio
            ):  # La??o que percorre todos os pixels no eixo y at?? o limiar do raio do kernel
                for x in range(
                    raio, largura - raio
                ):  # La??o que percorre todos os pixels no eixo x at?? o limiar do raio do kernel.
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            if (
                                mat[dy + raio][dx + raio] == branco
                            ):  # Verifica se o valor do pixel ?? 255.
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

    # Dilata????o - Insere pixels no conjunto de pixels que possuem o padr??o do Elemento Estruturante
    # Dilata????o que recebe uma imagem como par??metro
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
        branco = 255  # 255 ?? o valor equivalente ao pixel branco
        preto = 0  # 0 ?? o valor equivalente ao pixel preto

        for c in range(
            nCanais
        ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                raio, altura - raio
            ):  # La??o que percorre todos os pixels no eixo y at?? o limiar do raio do kernel
                for x in range(
                    raio, largura - raio
                ):  # La??o que percorre todos os pixels no eixo x at?? o limiar do raio do kernel.
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            if (
                                mat[dy + raio][dx + raio] == branco
                            ):  # Verifica se o valor do pixel ?? 255.
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
        imagem.mostrar(janela, "Imagem Dilata????o")  # Mostrar na tela a imagem tratada.
        return imagem

    # Abertura Bin??ria =  eros??o -> dilata????o (Realiza um eros??o depois uma dilata????o)
    # Abertura ??? suaviza o contorno de uma imagem.
    # Quebra estreitos e elimina proemin??ncias delgadas.
    # ?? usada tamb??m para remover ru??dos da imagem e abrir pequenos vazios ou espa??os entre objetos pr??ximos numa imagem .
    # Dada por uma eros??o seguida de uma dilata????o com o mesmo elemento estruturante.
    def aberturaBin(self):
        if self.msg["text"] == "Imagem":
            # Conjunto de pixels chamado de elemento estruturante (EE) ou kernel
            # Kenel com valores mais aleat??rios para contrastar a imagem
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

            erosao = self.erosaoBinParam(imagemEntrada, kernel)  # Realiza a eros??o
            abertura = self.dilatacaoBinParam(
                erosao, kernel
            )  # Realiza a dilata????o da eros??o com o mesmo Kernel

            return abertura  # Retorna a abertura

        else:
            self.msg["text"] = "Imagem"

    # Fechamento Bin??rio =  dilata????o -> eros??o (Realiza um dilata????o depois uma eros??o)
    # Closing ??? Funde pequenos quebras e alargas golfos estreitos.
    # Elimina pequenos orif??cios. Ir?? preencher ou fechar os vazios.
    # Estas opera????es remover pixels brancos com ru??dos.
    def fechamentoBin(self):
        if self.msg["text"] == "Imagem":
            # Conjunto de pixels chamado de elemento estruturante (EE) ou kernel
            # Kenel com valores mais aleat??rios para contrastar a imagem
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
            )  # Realiza a dilata????o
            fechamento = self.erosaoBinParam(
                dilatacao, kernel
            )  # Realiza a eros??o da dilata????o com o mesmo Kernel

            return fechamento  # Retorna o fechamento

        else:
            self.msg["text"] = "Imagem"

    # Borda Interna - (Imagem - eros??o(Imagem))
    # ?? a fronteira dada pela diferen??a entre a imagem original e sua eros??o.
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
            )  # Gera Imagem de sa??da com borda externa.

            imagemSaida.mostrar(
                janela, "Borda Interna"
            )  # Mostrar na tela a imagem tratada.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # Borda Externa - (dilatacao(Imagem) - Imagem)
    # ?? a fronteira dada pela diferen??a entre a imagem original e sua dilata????o.
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
            )  # Realiza a dilata????o
            subtracao = self.subtracao(
                dilatacao, imagemEntrada
            )  # Realiza a subtracao da dilata????o pela imagem de entrada.

            imagemSaida._criarComMatriz(
                subtracao
            )  # Gera Imagem de sa??da com borda externa.
            imagemSaida.mostrar(janela, "Borda Externa")  # Mostra a imagem na tela.
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    # 1. Posiciona-se a origem do elemento estruturante sobre o primeiro pixel da imagem que sofre eros??o.
    # 2. Calcula-se a diferen??a de cada par correspondente de valores de pixels do elemento estrutural e da imagem.
    # 3. Acha-se o valor m??nimo de todas essas diferen??as, e armazena-se o pixel correspondente na imagem de sa??da para este valor.
    # 4. Repete-se este processo para cada pixel da imagem que sofre eros??o.
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
            )  # Carrega a imagem do diret??rio
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
            preto = 0  # 0 ?? o valor equivalente ao pixel preto

            # La??os que percorrem cada pixel
            for c in range(
                nCanais
            ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    (raio), (altura - raio)
                ):  # La??o que percorre todos os pixels no eixo y at?? o limiar do raio do kernel
                    for x in range(
                        (raio), (largura - raio)
                    ):  # La??o que percorre todos os pixels no eixo x at?? o limiar do raio do kernel.
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
            imagem.criarComMatriz(matrizSaida)  # Gera imagem de sa??da.
            imagem.mostrar(janela, "Eros??o Mon")  # Mostrar na tela a imagem tratada.
            return imagem.criarComMatriz(matrizSaida)
        else:
            self.msg["text"] = "Imagem"

    # 1. Posiciona-se a origem do elemento estrutural sobre o primeiro pixel da imagem a ser dilatada.
    # 2. Calcula-se a soma de cada par correspondente de valores de pixels do elemento estrutural e da imagem.
    # 3. Acha-se o valor m??ximo de todas essas somas, e armazena-se o pixel correspondente na imagem de sa??da para este valor.
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
            )  # Carrega a imagem do diret??rio
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
            preto = 0  # 0 ?? o valor equivalente ao pixel preto

            # La??os que percorrem cada pixel
            for c in range(
                nCanais
            ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
                for y in range(
                    raio, altura - raio
                ):  # La??o que percorre todos os pixels no eixo y at?? o limiar do raio do kernel
                    for x in range(
                        raio, largura - raio
                    ):  # La??o que percorre todos os pixels no eixo x at?? o limiar do raio do kernel.
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
            imagem.criarComMatriz(matrizSaida)  # Gera imagem de sa??da.
            imagem.mostrar(janela, "Dilata????o Mon")  # Mostrar na tela a imagem tratada.
            return imagem.criarComMatriz(matrizSaida)
        else:
            self.msg["text"] = "Imagem"

    # M??todo erosao que aceita uma imagem de entrada como par??metro
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
        preto = 0  # 0 ?? o valor equivalente ao pixel preto

        # La??os que percorrem cada pixel
        for c in range(
            nCanais
        ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                (raio), (altura - raio)
            ):  # La??o que percorre todos os pixels no eixo y at?? o limiar do raio do kernel
                for x in range(
                    (raio), (largura - raio)
                ):  # La??o que percorre todos os pixels no eixo x at?? o limiar do raio do kernel.
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
        imagem.criarComMatriz(matrizSaida)  # Gera imagem de sa??da.
        return imagem

    # M??todo dilatacao que aceita uma imagem de entrada como par??metro
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
        preto = 0  # 0 ?? o valor equivalente ao pixel preto

        # La??os que percorrem cada pixel
        for c in range(
            nCanais
        ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                raio, altura - raio
            ):  # La??o que percorre todos os pixels no eixo y at?? o limiar do raio do kernel
                for x in range(
                    raio, largura - raio
                ):  # La??o que percorre todos os pixels no eixo x at?? o limiar do raio do kernel.
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
        imagem.criarComMatriz(matrizSaida)  # Gera imagem de sa??da.
        return imagem

    # M??todo eros??o que aceita uma imagem de entrada como par??metro
    # E ?? utilizado no m??todo de fechamento
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
        preto = 0  # 0 ?? o valor equivalente ao pixel preto

        # La??os que percorrem cada pixel
        for c in range(
            nCanais
        ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                (raio), (altura - raio)
            ):  # La??o que percorre todos os pixels no eixo y at?? o limiar do raio do kernel
                for x in range(
                    (raio), (largura - raio)
                ):  # La??o que percorre todos os pixels no eixo x at?? o limiar do raio do kernel.
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
        imagem.criarComMatriz(matrizSaida)  # Gera imagem de sa??da.
        imagem.mostrar(janela, "Fechamento Mon")  # Mostrar na tela a imagem tratada.
        return imagem.criarComMatriz(matrizSaida)

    # M??todo dilatacao que aceita uma imagem de entrada como par??metro
    # E ?? utilizado no m??todo de abertura
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
        preto = 0  # 0 ?? o valor equivalente ao pixel preto

        # La??os que percorrem cada pixel
        for c in range(
            nCanais
        ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(
                raio, altura - raio
            ):  # La??o que percorre todos os pixels no eixo y at?? o limiar do raio do kernel
                for x in range(
                    raio, largura - raio
                ):  # La??o que percorre todos os pixels no eixo x at?? o limiar do raio do kernel.
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
        imagem.criarComMatriz(matrizSaida)  # Gera imagem de sa??da.
        imagem.mostrar(janela, "Abertura Mon")  # Mostrar na tela a imagem tratada.

    # Abertura Monocrom??tica =  eros??o -> dilata????o (Realiza um eros??o depois uma dilata????o)
    # A abertura em tons de cinza funciona como a abertura bin??ria combinando as duas opera????es de eros??o e dilata????o em seq????ncia.
    # A diferen??a ?? que a propriedade da idempot??ncia n??o se aplica:
    # v??rias aberturas seguidas produzem um resultado mais acentuado do que uma ??nica abertura.
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
            )  # Carrega a imagem do diret??rio

            erosao = self.erosaoMonParam(imagemEntrada, kernel)  # Realiza a eros??o
            abertura = self.dilatacaoMonAbertura(
                erosao, kernel
            )  # Realiza a dilata????o da eros??o com o mesmo Kernel

            return abertura  # Retorna a abertura
        else:
            self.msg["text"] = "Imagem"

    # M??todo abertura que aceita uma imagem de entrada como par??metro
    def aberturaMonParam(self, imagemEntrada: Imagem, kernel):
        return self.dilatacaoMonAbertura(
            self.erosaoMonParam(imagemEntrada, kernel),
            kernel,
        )

    # Fechamento Monocrom??tico =  dilata????o -> eros??o (Realiza um dilata????o depois uma eros??o)
    # O fechamento em tons de cinza funciona como o fechamento bin??rio combinando as duas opera????es de dilata????o e eros??o em seq????ncia.
    # A diferen??a ?? que a propriedade da idempot??ncia n??o se aplica:
    # V??rios fechamentos seguidos produzem uum resultado mais acentuado do que um ??nico fechamento.
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
            )  # Carrega a imagem do diret??rio

            dilatacao = self.dilatacaoMonParam(
                imagemEntrada, kernel
            )  # Realiza a dilata????o
            fechamento = self.erosaoMonFechamento(
                dilatacao, kernel
            )  # Realiza a eros??o da dilata????o com o mesmo Kernel

            return fechamento  # Retorna o fechamento
        else:
            self.msg["text"] = "Imagem"

    # M??todo fechamento que aceita uma imagem de entrada como par??metro
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
        # La??os que percorrem cada pixel
        for c in range(
            nCanais
        ):  # La??o que percorre todos os canais (3 se RGB, 1 se cinza)
            for y in range(altura):  # La??o de posi????o altura y
                for x in range(largura):  # La??o de posi????o altura x
                    cor = matA[c][y][x] - matB[c][y][x]
                    if cor < 0:  # Evita estouro para n??meros negativos
                        cor = 0  # Seta zero caso seja um n??mero negativo
                    matrizSaida[
                        c, y, x
                    ] = cor  # Seta resultado da subtra????o no pixel atual.

        imagem = Imagem()  # Cria um objeto do tipo Imagem
        imagem.criarComMatriz(matrizSaida)  # Gera imagem de sa??da.
        imagem.mostrar(janela, "Subtra????o")  # Mostrar na tela a imagem tratada.
        return imagem.criarComMatriz(matrizSaida)

    # Gradiente = Dilata????o - eros??o (O resultado ?? a subtra????o da dilata????o pela eros??o)
    # Outra forma de encontrar a borda.
    # Composta de tr??s outras opera????es b??sicas: Dilata????o, eros??o e a subtra????o.
    # A imagem ?? dilatada e erodida pelo mesmo kernel e o resultado erodido ?? subtra??do do resultado dilatado.
    # Resulta em uma borda maior e mais confi??vel.
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
            )  # Carrega a imagem do diret??rio
            imagem = Imagem()  # Cria um objeto do tipo Imagem

            dilatacao = self.dilatacaoMonParam(
                imagemEntrada, kernel
            )  # Realiza a dilatacao
            erosao = self.erosaoMonParam(imagemEntrada, kernel)  # Realiza a eros??o
            subtracao = self.subtracaoMon(
                dilatacao, erosao
            )  # Realiza a subtracao da dilata????o pela eros??o
            imagem.criarComMatriz(subtracao)  # Cria a imagem de sa??da

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
            )  # Carrega a imagem do diret??rio

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
