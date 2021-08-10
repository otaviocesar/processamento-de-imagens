from tkinter import *
from util.Imagem import *
import numpy as numpy
from random import random, randrange

class Application:
    def __init__(self, master=None):
        janela.title("Janela")
        janela.geometry('800x600')
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Imagem")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()

        self.b1 = Button(self.widget1)
        self.b1["text"] = "Carregar"
        self.b1["font"] = ("Calibri", "9")
        self.b1["width"] = 55
        self.b1["command"] = self.carregar
        self.b1.pack ()

        self.b2 = Button(self.widget1)
        self.b2["text"] = "Converte para cinza"
        self.b2["font"] = ("Calibri", "9")
        self.b2["width"] = 55
        self.b2["command"] = self.converteParaCinza
        self.b2.pack ()

        self.b3 = Button(self.widget1)
        self.b3["text"] = "Converte para RGB"
        self.b3["font"] = ("Calibri", "9")
        self.b3["width"] = 55
        self.b3["command"] = self.converteParaRgb
        self.b3.pack ()

        self.b4 = Button(self.widget1)
        self.b4["text"] = "Salvar"
        self.b4["font"] = ("Calibri", "9")
        self.b4["width"] = 55
        self.b4["command"] = self.salvar
        self.b4.pack ()

        self.b5 = Button(self.widget1)
        self.b5["text"] = "Limiar Simples"
        self.b5["font"] = ("Calibri", "9")
        self.b5["width"] = 55
        self.b5["command"] = self.limiarSimples
        self.b5.pack ()

        self.b6 = Button(self.widget1)
        self.b6["text"] = "Limiar Com Modulacao Aleatoria"
        self.b6["font"] = ("Calibri", "9")
        self.b6["width"] = 55
        self.b6["command"] = self.limiarComModulacaoAleatoria
        self.b6.pack ()

        self.b7 = Button(self.widget1)
        self.b7["text"] = "Limiar Com Modulacao Ordenada Periodico Aglomerado"
        self.b7["font"] = ("Calibri", "9")
        self.b7["width"] = 55
        self.b7["command"] = self.limiarComModulacaoOrdenadaPeriodicoAglomerado
        self.b7.pack ()

        self.b8 = Button(self.widget1)
        self.b8["text"] = "Limiar Com Modulacao Ordenada Periodico Disperso"
        self.b8["font"] = ("Calibri", "9")
        self.b8["width"] = 55
        self.b8["command"] = self.limiarComModulacaoOrdenadaPeriodicoDisperso
        self.b8.pack ()

        self.b9 = Button(self.widget1)
        self.b9["text"] = "Limiar Com Modulacao Ordenada Aperiodico"
        self.b9["font"] = ("Calibri", "9")
        self.b9["width"] = 55
        self.b9["command"] = self.limiarComModulacaoOrdenadaAperiodico
        self.b9.pack ()

        self.b10 = Button(self.widget1)
        self.b10["text"] = "Erosão - Morfologia matemática binária"
        self.b10["font"] = ("Calibri", "9")
        self.b10["width"] = 55
        self.b10["command"] = self.erosaoBin
        self.b10.pack ()

        self.b11 = Button(self.widget1)
        self.b11["text"] = "Dilatação - Morfologia matemática binária"
        self.b11["font"] = ("Calibri", "9")
        self.b11["width"] = 55
        self.b11["command"] = self.dilatacaoBin
        self.b11.pack ()

        self.b12 = Button(self.widget1)
        self.b12["text"] = "Abertura - Morfologia matemática binária"
        self.b12["font"] = ("Calibri", "9")
        self.b12["width"] = 55
        self.b12["command"] = self.aberturaBin
        self.b12.pack ()

        self.b13 = Button(self.widget1)
        self.b13["text"] = "Fechamento - Morfologia matemática binária"
        self.b13["font"] = ("Calibri", "9")
        self.b13["width"] = 55
        self.b13["command"] = self.fechamentoBin
        self.b13.pack ()

        self.b14 = Button(self.widget1)
        self.b14["text"] = "Borda interna"
        self.b14["font"] = ("Calibri", "9")
        self.b14["width"] = 55
        self.b14["command"] = self.bordaInterna
        self.b14.pack ()

        self.b15 = Button(self.widget1)
        self.b15["text"] = "Borda externa"
        self.b15["font"] = ("Calibri", "9")
        self.b15["width"] = 55
        self.b15["command"] = self.bordaExterna
        self.b15.pack ()

        self.b16 = Button(self.widget1)
        self.b16["text"] = "Erosão - Morfologia matemática monocromática"
        self.b16["font"] = ("Calibri", "9")
        self.b16["width"] = 55
        self.b16["command"] = self.erosaoMon
        self.b16.pack ()

        self.b17 = Button(self.widget1)
        self.b17["text"] = "Dilatação - Morfologia matemática monocromática"
        self.b17["font"] = ("Calibri", "9")
        self.b17["width"] = 55
        self.b17["command"] = self.dilatacaoMon
        self.b17.pack ()

        self.b18 = Button(self.widget1)
        self.b18["text"] = "Abertura - Morfologia matemática monocromática"
        self.b18["font"] = ("Calibri", "9")
        self.b18["width"] = 55
        self.b18["command"] = self.aberturaMon
        self.b18.pack ()

        self.b19 = Button(self.widget1)
        self.b19["text"] = "Fechamento - Morfologia matemática monocromática"
        self.b19["font"] = ("Calibri", "9")
        self.b19["width"] = 55
        self.b19["command"] = self.fechamentoMon
        self.b19.pack ()

        self.b20 = Button(self.widget1)
        self.b20["text"] = "Gradiente"
        self.b20["font"] = ("Calibri", "9")
        self.b20["width"] = 55
        self.b20["command"] = self.gradiente
        self.b20.pack ()


    def carregar(self):
        if self.msg["text"] == "Imagem":
            #self.msg["text"] = "Teste"
            img1=Imagem()
            img1.carregar('img/lennaRGB.jpg')
            img1.mostrar(janela, 'Testando lennaRGB.jpg')
        else:
            self.msg["text"] = "Imagem"

    def criarVazia(self):
        if self.msg["text"] == "Imagem":
            img2=Imagem()
            img2.criarVazia('RGB',100,200,)
            img2.mostrar(janela,'Vazia RGB 100x200')
        else:
            self.msg["text"] = "Imagem"

    def criarDeMatriz(self):
        if self.msg["text"] == "Imagem":
            img3=Imagem()
            mat=[[[255,255,255],[255,255,255],[255,255,255]],
                [[0,0,0],[0,0,0],[0,0,0]],
                [[0,0,0],[0,0,0],[0,0,0]]    ]
            img3.criarComMatriz(mat)
            img3.mostrar(janela,'Criando através de uma matriz pré-existente')
        else:
            self.msg["text"] = "Imagem"

    def converteParaRgb(self):
        if self.msg["text"] == "Imagem":
            img4 = Imagem()
            img4.carregar('img/lennaRGB.jpg')
            img4.mostrar(janela)
            img4.toRGB()
            img4.mostrar(janela)
        else:
            self.msg["text"] = "Imagem"

    def converteParaCinza(self):
        if self.msg["text"] == "Imagem":
            img4 = Imagem()
            img4.carregar('img/lennaRGB.jpg')
            img4.mostrar(janela)
            img4.toGray()
            img4.mostrar(janela)
        else:
            self.msg["text"] = "Imagem"

    def getMatriz(self):
        if self.msg["text"] == "Imagem":
            img =Imagem()
            # img.carregar('img/olho.png')
            img.carregar('img/lennaRGB.jpg')
            # img.criarVazia('L',4,5)
            mat=img.getMatriz()    
            for i in range(30):
                mat[0][i][i]=255
            img.criarComMatriz(mat)  
            img.mostrar(janela)
        else:
            self.msg["text"] = "Imagem"

    def salvar(self):
        if self.msg["text"] == "Imagem":
            img =Imagem()
            img.carregar('img/lennaRGB.jpg')
            mat=img.getMatriz()    
            for i in range(100):
                mat[0][i][i]=200
                mat[0][i][i]=128
            img.criarComMatriz(mat)  
            img.mostrar(janela)
            img.salvar('img/testeSalvar.png',img.TYPE_PNG())
            img.salvar('img/testeSalvar.jpg',img.TYPE_JPG())
            img.salvar('img/testeSalvar.gif',img.TYPE_GIF())
            img.salvar('img/testeSalvar.pdf',img.TYPE_PDF())
        else:
            self.msg["text"] = "Imagem"

    def subtracao(self, imgA: Imagem, imgB: Imagem):
        nCanais = imgA.getNCanais()
        altura = imgA.getAltura()
        largura = imgA.getLargura()
        matA = imgA.getMatriz()
        matB = imgB.getMatriz()

        cor = None
        matrizSaida = numpy.zeros((nCanais, altura, largura))

        for c in range(nCanais):
            for y in range(altura):
                for x in range(largura):
                    cor = matA[c][y][x] - matB[c-1][y-1][x-1]
                    if (cor < 0):
                        cor = 0
                    matrizSaida[c, y, x] = cor

        return matrizSaida

    def limiarSimples(self):
        if self.msg["text"] == "Imagem":
            img =Imagem()
            img.carregar('img/lennaRGB.jpg')
            img.toGray
            nCanais = img.getNCanais()
            altura = img.getAltura()
            largura = img.getLargura()
            matriz = img.getMatriz()
            matO = numpy.zeros((nCanais, altura, largura))
            branco = 255
            preto = 0
            threshold = int((branco + preto) / 2)

            for c in range(nCanais):
                for y in range(altura):
                    for x in range(largura):
                        if (matriz[c][y][x] < threshold):
                            matO[c, y, x] = preto
                        else:
                            matO[c, y, x] = branco

            imagem = Imagem()
            imagem.criarComMatriz(matO)
            imagem.mostrar(janela, 'Limiar Simples')
            return imagem
        else:
            self.msg["text"] = "Imagem"

    def limiarComModulacaoAleatoria(self):
        if self.msg["text"] == "Imagem":
            img =Imagem()
            img.carregar('img/lennaRGB.jpg')
            img.toGray
            nCanais = img.getNCanais()
            altura = img.getAltura()
            largura = img.getLargura()
            matriz = img.getMatriz()
            matO = numpy.zeros((nCanais, altura, largura))
            branco = 255
            preto = 0
            threshold = int((branco + preto) / 2)

            for c in range(nCanais):
                for y in range(altura):
                    for x in range(largura):
                        aux = matriz[c][y][x] + randrange(-128, 128) - threshold
                        if (aux < threshold):
                            matO[c, y, x] = preto
                        else:
                            matO[c, y, x] = branco

            imagem = Imagem()
            imagem.criarComMatriz(matO)
            imagem.mostrar(janela, 'Limiar com modulação aleatória')
            return imagem
        else:
            self.msg["text"] = "Imagem"

    def quantizacao(self, img: Imagem, input, output):
        img =Imagem()
        img.carregar('img/lennaRGB.jpg')
        img.toGray
        faixa = int(input/output)
        mat = img.getMatriz()
        nCanais = img.getNCanais()
        altura = img.getAltura()
        largura = img.getLargura()

        for c in range(nCanais):
            for y in range(altura):
                for x in range(largura):
                    color = int(mat[c][y][x]/faixa)
                    mat[c][y][x] = color

        imagem = Imagem()
        imagem.criarComMatriz(mat)
        return imagem

    def limiarComModulacaoOrdenadaPeriodicoAglomerado(self):
        if self.msg["text"] == "Imagem":
            img =Imagem()
            img.carregar('img/lennaRGB.jpg')
            img.toGray
            mat = numpy.array([[4, 3, 3], [2, 0, 2], [7, 1, 6]])
            nCanais = self.quantizacao(img, 256, len(
                mat)*(len(mat) + 1)).getNCanais()
            altura = self.quantizacao(img, 256, len(mat)*(len(mat) + 1)).getAltura()
            largura = self.quantizacao(img, 256, len(mat)*(len(mat) + 1)).getLargura()
            matriz = self.quantizacao(img, 256, len(mat)*(len(mat) + 1)).getMatriz()
            coefficient = len(mat)
            matO = numpy.zeros((nCanais, altura*coefficient, largura*coefficient))
            branco = 255
            preto = 0

            for c in range(nCanais):
                for y in range(altura):
                    for x in range(largura):
                        for z in range(len(mat)):
                            for w in range(len(mat[z])):
                                if (matriz[c][y][x] > mat[z][w]):
                                    matO[c, y*coefficient + z,
                                        x*coefficient + w] = branco
                                else:
                                    matO[c, y*coefficient + z,
                                        x*coefficient + w] = preto

            imagem = Imagem()
            imagem.criarComMatriz(matO)
            imagem.mostrar(janela, 'Limiar com modulação ordenada periódico aglomerado')
            return imagem
        else:
            self.msg["text"] = "Imagem"

    def limiarComModulacaoOrdenadaPeriodicoDisperso(self):
        if self.msg["text"] == "Imagem":
            img =Imagem()
            img.carregar('img/lennaRGB.jpg')
            img.toGray
            mat = numpy.array([[4, 3, 3], [2, 0, 2], [7, 1, 6]])
            nCanais = self.quantizacao(img, 256, len(mat)*len(mat)).getNCanais()
            altura = self.quantizacao(img, 256, len(mat)*len(mat)).getAltura()
            largura = self.quantizacao(img, 256, len(mat)*len(mat)).getLargura()
            matriz = self.quantizacao(img, 256, len(mat)*len(mat)).getMatriz()
            matO = numpy.zeros((nCanais, altura, largura))
            branco = 255
            preto = 0
            aux = len(mat)
            z = 0
            w = 0

            for c in range(nCanais):
                for y in range(altura):
                    w = y % aux
                    for x in range(largura):
                        z = x % aux

                        if (matriz[c][y][x] > mat[w][z]):
                            matO[c, y, x] = branco
                        else:
                            matO[c, y, x] = preto

            imagem = Imagem()
            imagem.criarComMatriz(matO)
            imagem.mostrar(janela, 'Limiar com modulação ordenada periódico disperso')
            return imagem
        else:
            self.msg["text"] = "Imagem"

    def limiarComModulacaoOrdenadaAperiodico(self):
        if self.msg["text"] == "Imagem":
            img =Imagem()
            img.carregar('img/lennaRGB.jpg')
            img.toGray
            nCanais = img.getNCanais()
            altura = img.getAltura()
            largura = img.getLargura()
            matriz = img.getMatriz()
            matO = numpy.zeros((nCanais, altura, largura))
            branco = 255
            preto = 0
            threshold = int((branco + preto + 1)/2)
            aux = None

            for c in range(nCanais):
                for x in range(largura-1):
                    for y in range(altura-1):
                        if (matriz[c][y][x] < threshold):
                            aux = matriz[c][y][x] - preto
                            matO[c, y, x] = preto

                        else:
                            aux = matriz[c][y][x] - branco
                            matO[c, y, x] = branco

                        matriz[c][y+1][x] += int((3*aux)/8)
                        matriz[c][y][x+1] += int((3*aux)/8)
                        matriz[c][y+1][x+1] += int((aux/8))

            imagem = Imagem()
            imagem.criarComMatriz(matO)
            imagem.mostrar(janela, 'Limiar com modulação ordenada aperiódico')
            return imagem
        else:
            self.msg["text"] = "Imagem"

    def erosaoBin(self, bool=False):
        if self.msg["text"] == "Imagem":
            mat = numpy.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
            255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
            img = Imagem()
            img.carregar('img/b.png')
            nCanais = img.getNCanais()
            altura = img.getAltura()
            largura = img.getLargura()
            matriz = img.getMatriz()
            matrizSaida = numpy.zeros((nCanais, altura, largura))
            raio = int((len(mat) - 1)/2)
            auxBool = False

            for c in range(nCanais):
                for y in range(raio, altura-raio):
                    for x in range(raio, largura-raio):
                        for z in range(-raio, raio+1):
                            for w in range(-raio, raio+1):
                                if(mat[z+raio][w+raio] == 255):
                                    if (matriz[c][y+z][x+w] != mat[z+raio][w+raio]):
                                        auxBool = False

                        if(auxBool == True):
                            matrizSaida[c, y, x] = matriz[c][y][x]
                        else:
                            matrizSaida[c, y, x] = 0
                        auxBool = True

            imagem = Imagem()
            imagem._criarComMatriz(matrizSaida)
            if (bool == True):
                imagem.mostrar(janela, 'Image Fechamento')
            else:
                imagem.mostrar(janela, 'Imagem Erosao')
            return imagem
        else:
            self.msg["text"] = "Imagem"

    def erosaoBin2(self, img: Imagem, mat, bool=False):
        mat = numpy.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
        255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
        nCanais = img.getNCanais()
        altura = img.getAltura()
        largura = img.getLargura()
        matriz = img.getMatriz()
        matrizSaida = numpy.zeros((nCanais, altura, largura))
        raio = int((len(mat) - 1)/2)
        auxBool = False

        for c in range(nCanais):
            for y in range(raio, altura-raio):
                for x in range(raio, largura-raio):
                    for z in range(-raio, raio+1):
                        for w in range(-raio, raio+1):
                            if(mat[z+raio][w+raio] == 255):
                                if (matriz[c][y+z][x+w] != mat[z+raio][w+raio]):
                                    auxBool = False

                    if(auxBool == True):
                        matrizSaida[c, y, x] = matriz[c][y][x]
                    else:
                        matrizSaida[c, y, x] = 0
                    auxBool = True

        imagem = Imagem()
        imagem._criarComMatriz(matrizSaida)
        if (bool == True):
            imagem.mostrar(janela, 'Image Fechamento')
        else:
            imagem.mostrar(janela, 'Imagem Erosao')
        return imagem

    def dilatacaoBin(self, bool=False):
        if self.msg["text"] == "Imagem":
            mat = numpy.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
            255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
            img = Imagem()
            img.carregar('img/b.png')
            nCanais = img.getNCanais()
            altura = img.getAltura()
            largura = img.getLargura()
            matriz = img.getMatriz()
            matrizSaida = numpy.zeros((nCanais, altura, largura))
            raio = int((len(mat) - 1)/2)
            auxBool = False

            for c in range(nCanais):
                for y in range(raio, altura-raio):
                    for x in range(raio, largura-raio):
                        for z in range(-raio, raio+1):
                            for w in range(-raio, raio+1):
                                if (mat[z+raio][w+raio] == 255):
                                    if (matriz[c][y+z][x+w] == mat[z+raio][w+raio]):
                                        auxBool = True

                        if (auxBool == True):
                            matrizSaida[c, y, x] = 255
                        else:
                            matrizSaida[c, y, x] = 0
                        auxBool = False

            imagem = Imagem()
            imagem._criarComMatriz(matrizSaida)
            if (bool == True):
                imagem.mostrar(janela, 'Imagem Abertura')
            else:
                imagem.mostrar(janela, 'Imagem Dilatação')
            return imagem
        else:
            self.msg["text"] = "Imagem"

    def dilatacaoBin2(self, img: Imagem, mat, bool=False):
        nCanais = img.getNCanais()
        altura = img.getAltura()
        largura = img.getLargura()
        matriz = img.getMatriz()
        matrizSaida = numpy.zeros((nCanais, altura, largura))
        raio = int((len(mat) - 1)/2)
        auxBool = False

        for c in range(nCanais):
            for y in range(raio, altura-raio):
                for x in range(raio, largura-raio):
                    for z in range(-raio, raio+1):
                        for w in range(-raio, raio+1):
                            if (mat[z+raio][w+raio] == 255):
                                if (matriz[c][y+z][x+w] == mat[z+raio][w+raio]):
                                    auxBool = True

                    if (auxBool == True):
                        matrizSaida[c, y, x] = 255
                    else:
                        matrizSaida[c, y, x] = 0
                    auxBool = False

        imagem = Imagem()
        imagem._criarComMatriz(matrizSaida)
        if (bool == True):
            imagem.mostrar(janela, 'Imagem Abertura')
        else:
            imagem.mostrar(janela, 'Imagem Dilatação')
        return imagem

    def aberturaBin(self):
        if self.msg["text"] == "Imagem":
            mat = numpy.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
            255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
            img = Imagem()
            img.carregar('img/b.png')
            return self.dilatacaoBin2(self.erosaoBin2(img, mat), mat, True)
        else:
            self.msg["text"] = "Imagem"

    def fechamentoBin(self):
        if self.msg["text"] == "Imagem":
            mat = numpy.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
            255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
            img = Imagem()
            img.carregar('img/b.png')
            return self.erosaoBin2(self.dilatacaoBin2(img, mat), mat, True)
        else:
            self.msg["text"] = "Imagem"

    def bordaInterna(self):
        if self.msg["text"] == "Imagem":
            mat = numpy.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
            255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
            img = Imagem()
            img.carregar('img/b.png')
            imagemSaida = Imagem()
            imagemSaida._criarComMatriz(self.subtracao(img, self.erosaoBin2(img, mat)))
            imagemSaida.mostrar(janela, 'Borda Interna')
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    def bordaExterna(self):
        if self.msg["text"] == "Imagem":
            mat = numpy.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
            255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
            img = Imagem()
            img.carregar('img/b.png')
            imagemSaida = Imagem()
            imagemSaida._criarComMatriz(self.subtracao(self.dilatacaoBin2(img, mat), img))
            imagemSaida.mostrar(janela, 'Borda Externa')
            return imagemSaida
        else:
            self.msg["text"] = "Imagem"

    def subtracaoMon(self, imgA: Imagem, imgB: Imagem):
        nCanais = imgA.getNCanais()
        altura = imgA.getAltura()
        largura = imgA.getLargura()
        matA = imgA.getMatriz()
        matB = imgB.getMatriz()

        colorSub = None
        matrizSaida = numpy.zeros((nCanais, altura, largura))

        for c in range(nCanais):
            for y in range(altura):
                for x in range(largura):
                    colorSub = matA[c][y][x] - matB[c][y][x]
                    if (colorSub < 0):
                        colorSub = 0
                    matrizSaida[c, y, x] = colorSub

        imagem = Imagem()
        imagem.criarComMatriz(matrizSaida)
        imagem.mostrar(janela, 'Subtração')
        return imagem.criarComMatriz(matrizSaida)

    def subtracaoMon2(self, imgA: Imagem, imgB: Imagem):
        nCanais = imgA.getNCanais()
        altura = imgA.getAltura()
        largura = imgA.getLargura()
        matA = imgA.getMatriz()
        matB = imgB.getMatriz()

        colorSub = None
        matrizSaida = numpy.zeros((nCanais, altura, largura))

        for c in range(nCanais):
            for y in range(altura):
                for x in range(largura):
                    colorSub = matA[c][y][x] - matB[c][y][x]
                    if (colorSub < 0):
                        colorSub = 0
                    matrizSaida[c, y, x] = colorSub

        imagem = Imagem()
        imagem.criarComMatriz(matrizSaida)
        return imagem.getMatriz()

    def erosaoMon(self):
        if self.msg["text"] == "Imagem":
            mat = numpy.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                        1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
            img = Imagem()
            img.carregar('img/lennaRGB.jpg')
            img.toGray()
            nCanais = img.getNCanais()
            altura = img.getAltura()
            largura = img.getLargura()
            matrizEntrada = img.getMatriz()
            matrizSaida = numpy.zeros((nCanais, altura, largura))
            radius = int((len(mat) - 1)/2)
            min = 800000000000000000

            for c in range(nCanais):
                for y in range((radius), (altura-radius)):
                    for x in range((radius), (largura - radius)):
                        for z in range((-radius), (radius + 1)):
                            for w in range((-radius), (radius+1)):
                                if(min > matrizEntrada[c][y + z][x+w] + mat[(z+radius)][(w+radius)]):
                                    min = matrizEntrada[c][y+z][x+w] + \
                                        mat[(z+radius)][(w+radius)]

                        if (min > 0):
                            matrizSaida[c, y, x] = min
                        else:
                            matrizSaida[c, y, x] = 0

                        min = 800000000000000000

            imagem = Imagem()
            imagem.criarComMatriz(matrizSaida)
            imagem.mostrar(janela, 'Erosão Mon')
            return imagem.criarComMatriz(matrizSaida)
        else:
            self.msg["text"] = "Imagem"

    def dilatacaoMon(self):
        if self.msg["text"] == "Imagem":
            mat = numpy.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                        1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
            img = Imagem()
            img.carregar('img/lennaRGB.jpg')
            img.toGray()
            nCanais = img.getNCanais()
            altura = img.getAltura()
            largura = img.getLargura()
            matrizEntrada = img.getMatriz()
            matrizSaida = numpy.zeros((nCanais, altura, largura))
            radius = int((len(mat) - 1)/2)
            max = -800000000000000000

            for c in range(nCanais):
                for y in range(radius, altura - radius):
                    for x in range(radius, largura - radius):
                        for z in range(-radius, radius+1):
                            for w in range(-radius, radius+1):
                                if (max < matrizEntrada[c][y+z][x+w] + mat[z+radius][w+radius]):
                                    max = matrizEntrada[c][y+z][x+w] + \
                                        mat[z+radius][w+radius]

                        if (max > 0):
                            matrizSaida[c, y, x] = max
                        else:
                            matrizSaida[c, y, x] = 0

                        max = -800000000000000000

            imagem = Imagem()
            imagem.criarComMatriz(matrizSaida)
            imagem.mostrar(janela, 'Dilatação Mon')
            return imagem.criarComMatriz(matrizSaida)
        else:
            self.msg["text"] = "Imagem"

    def erosaoMon2(self, img: Imagem, mat):
        nCanais = img.getNCanais()
        altura = img.getAltura()
        largura = img.getLargura()
        matrizEntrada = img.getMatriz()
        matrizSaida = numpy.zeros((nCanais, altura, largura))
        radius = int((len(mat) - 1)/2)
        min = 800000000000000000

        for c in range(nCanais):
            for y in range((radius), (altura-radius)):
                for x in range((radius), (largura - radius)):
                    for z in range((-radius), (radius + 1)):
                        for w in range((-radius), (radius+1)):
                            if(min > matrizEntrada[c][y + z][x+w] + mat[(z+radius)][(w+radius)]):
                                min = matrizEntrada[c][y+z][x+w] + \
                                    mat[(z+radius)][(w+radius)]

                    if (min > 0):
                        matrizSaida[c, y, x] = min
                    else:
                        matrizSaida[c, y, x] = 0

                    min = 800000000000000000

        imagem = Imagem()
        imagem.criarComMatriz(matrizSaida)
        return imagem

    def dilatacaoMon2(self, img: Imagem, mat):
        nCanais = img.getNCanais()
        altura = img.getAltura()
        largura = img.getLargura()
        matrizEntrada = img.getMatriz()
        matrizSaida = numpy.zeros((nCanais, altura, largura))
        radius = int((len(mat) - 1)/2)
        max = -800000000000000000

        for c in range(nCanais):
            for y in range(radius, altura - radius):
                for x in range(radius, largura - radius):
                    for z in range(-radius, radius+1):
                        for w in range(-radius, radius+1):
                            if (max < matrizEntrada[c][y+z][x+w] + mat[z+radius][w+radius]):
                                max = matrizEntrada[c][y+z][x+w] + \
                                    mat[z+radius][w+radius]

                    if (max > 0):
                        matrizSaida[c, y, x] = max
                    else:
                        matrizSaida[c, y, x] = 0

                    max = -800000000000000000

        imagem = Imagem()
        imagem.criarComMatriz(matrizSaida)
        return imagem

    def erosaoMon3(self, img: Imagem, mat, bool=False):
        nCanais = img.getNCanais()
        altura = img.getAltura()
        largura = img.getLargura()
        matrizEntrada = img.getMatriz()
        matrizSaida = numpy.zeros((nCanais, altura, largura))
        radius = int((len(mat) - 1)/2)
        min = 800000000000000000

        for c in range(nCanais):
            for y in range((radius), (altura-radius)):
                for x in range((radius), (largura - radius)):
                    for z in range((-radius), (radius + 1)):
                        for w in range((-radius), (radius+1)):
                            if(min > matrizEntrada[c][y + z][x+w] + mat[(z+radius)][(w+radius)]):
                                min = matrizEntrada[c][y+z][x+w] + \
                                    mat[(z+radius)][(w+radius)]

                    if (min > 0):
                        matrizSaida[c, y, x] = min
                    else:
                        matrizSaida[c, y, x] = 0

                    min = 800000000000000000

        imagem = Imagem()
        imagem.criarComMatriz(matrizSaida)
        if (bool == True):
            imagem.mostrar(janela, 'Fechamento Mon')
        imagem.mostrar(janela, 'Erosão Mon')
        return imagem.criarComMatriz(matrizSaida)

    def dilatacaoMon3(self, img: Imagem, mat, bool=False):
        nCanais = img.getNCanais()
        altura = img.getAltura()
        largura = img.getLargura()
        matrizEntrada = img.getMatriz()
        matrizSaida = numpy.zeros((nCanais, altura, largura))
        radius = int((len(mat) - 1)/2)
        max = -800000000000000000

        for c in range(nCanais):
            for y in range(radius, altura - radius):
                for x in range(radius, largura - radius):
                    for z in range(-radius, radius+1):
                        for w in range(-radius, radius+1):
                            if (max < matrizEntrada[c][y+z][x+w] + mat[z+radius][w+radius]):
                                max = matrizEntrada[c][y+z][x+w] + \
                                    mat[z+radius][w+radius]

                    if (max > 0):
                        matrizSaida[c, y, x] = max
                    else:
                        matrizSaida[c, y, x] = 0

                    max = -800000000000000000

        imagem = Imagem()
        imagem.criarComMatriz(matrizSaida)
        if (bool == True):
            imagem.mostrar(janela, 'Abertura Mon')
        imagem.mostrar(janela, 'Dilatação Mon')
        return imagem.criarComMatriz(matrizSaida)

    def aberturaMon(self):
        if self.msg["text"] == "Imagem":
            mat = numpy.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                        1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
            img = Imagem()
            img.carregar('img/lennaRGB.jpg')
            return self.dilatacaoMon3(self.erosaoMon2(img, mat), mat)
        else:
            self.msg["text"] = "Imagem"

    def fechamentoMon(self):
        if self.msg["text"] == "Imagem":
            mat = numpy.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                        1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
            img = Imagem()
            img.carregar('img/lennaRGB.jpg')
            img.toGray()
            return self.erosaoMon3(self.dilatacaoMon2(img, mat), mat, True)
        else:
            self.msg["text"] = "Imagem"

    def gradiente(self):
        if self.msg["text"] == "Imagem":
            mat = numpy.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                        1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
            img = Imagem()
            img.carregar('img/lennaRGB.jpg')
            img.toGray()
            imagem = Imagem()
            imagem.criarComMatriz(self.subtracaoMon2(
                self.dilatacaoMon2(img, mat), self.erosaoMon2(img, mat)))
            return imagem.mostrar(janela, 'Gradiente')
        else:
            self.msg["text"] = "Imagem"

janela = Tk()
Application(janela)
janela.mainloop()