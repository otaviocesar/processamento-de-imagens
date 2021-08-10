from tkinter import *
from PIL import Image, ImageTk

class Imagem:

    __img=None
    
    def MODE_RGB(self): return 'RGB'
    def MODE_GRAY(self): return 'L'
    def TYPE_JPG(self): return 'JPEG'
    def TYPE_PNG(self): return 'PNG'
    def TYPE_GIF(self): return 'GIF'
    def TYPE_PDF(self): return 'PDF'

    def carregar(self, path) :
        try:
            self.__img=Image.open(path)
        except:
            print('Erro ao abrir o arquivo '+path)
    
    def criarVazia(self, tipo,altura=0, largura=0) :
        if tipo==self.MODE_RGB():
            self.__img=Image.new(tipo, (largura,altura ), (0, 0, 0))
        else:
            self.__img=Image.new(tipo, (largura, altura ), (0))

    def criarComMatriz(self, mat):
        nCanais = len(mat)
        altura = len(mat[0])
        largura = len(mat[0][0])

        if (nCanais == 3):
            self.criarVazia(self.MODE_RGB(), altura, largura)
            color = []
            for y in range(0, altura):
                for x in range(0, largura):
                    for c in range(0, nCanais):
                        color.append(int(mat[c][y][x]))
                    self.__img.putpixel((x, y), tuple(color))
                    color.clear()

        else:
            self.criarVazia(self.MODE_GRAY(), altura, largura)
            for y in range(altura):
                for x in range(largura):
                    self.__img.putpixel((x, y), int(mat[0][y][x]))

    def _criarComMatriz(self, mat):
        nCanais = len(mat)
        altura = len(mat[0])
        largura = len(mat[0][0])

        if (nCanais == 3):
            self.criarVazia(self.MODE_RGB(), altura, largura)
            color = []
            for y in range(0, altura):
                for x in range(0, largura):
                    for c in range(0, nCanais):
                        color.append(mat[c][y][x])
                    self.__img.putpixel((x, y), tuple(color))
                    color.clear()

        else:
            self.criarVazia(self.MODE_GRAY(), altura, largura)
            for y in range(altura):
                for x in range(largura):
                    self.__img.putpixel((x-1, y-1), int(mat[0][y][x]))

                    
    def toGray(self):
        self.__img=self.__img.convert(self.MODE_GRAY())

    def toRGB(self):
        self.__img=self.__img.convert(self.MODE_RGB())

    def getAltura(self):
        return self.__img.height
    
    def getLargura(self):
        return self.__img.width
    
    def getNCanais(self):
        if self.__img.mode==self.MODE_GRAY():
            return 1
        elif self.__img.mode==self.MODE_RGB():
            return 3
        else:
            print('A imagem não possui um ou três canais. Converta para uma dessas opções.')


    def getMatriz(self):
        nCanais=self.getNCanais()
        altura=self.getAltura()
        largura=self.getLargura()
        mat=[]
        for c in range(nCanais):
            pagina=[]
            for y in range(altura):
                pagina+=[([0]*largura)]
            mat+=[pagina]

        cor=None
        vetImg=self.__img.load()
        if nCanais==3:
            for y in range(0,altura):
                for x in range(0,largura):
                    cor=vetImg[x,y]
                    for c in range(0,nCanais):
                        mat[c][y][x]=cor[c]
        else:
            for y in range(0,altura):
                for x in range(0,largura):
                    mat[0][y][x]=self.__img.getpixel((x,y))

        
        return mat

    def salvar(self,path,tipo):
        self.__img.save(path,tipo)

    def mostrar(self, janela, titulo=''):
        imagem = Label(janela)
        imagem.la = ImageTk.PhotoImage(self.__img)
        imagem['image'] = imagem.la
        imagem.place(x=0,y=0)
