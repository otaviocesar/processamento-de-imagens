from tkinter import *
from util.Imagem import *

class Application:
    def __init__(self, master=None):
        janela.title("Janela")
        janela.geometry('800x400')
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Imagem")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()

        self.b1 = Button(self.widget1)
        self.b1["text"] = "Carregar"
        self.b1["font"] = ("Calibri", "9")
        self.b1["width"] = 20
        self.b1["command"] = self.carregar
        self.b1.pack ()

        self.b2 = Button(self.widget1)
        self.b2["text"] = "Cria Vazia"
        self.b2["font"] = ("Calibri", "9")
        self.b2["width"] = 20
        self.b2["command"] = self.criarVazia
        self.b2.pack ()

        self.b3 = Button(self.widget1)
        self.b3["text"] = "Cria de Matriz"
        self.b3["font"] = ("Calibri", "9")
        self.b3["width"] = 20
        self.b3["command"] = self.criarDeMatriz
        self.b3.pack ()

        self.b4 = Button(self.widget1)
        self.b4["text"] = "Converte para RGB"
        self.b4["font"] = ("Calibri", "9")
        self.b4["width"] = 20
        self.b4["command"] = self.converteParaRgb
        self.b4.pack ()

        self.b5 = Button(self.widget1)
        self.b5["text"] = "Converte para cinza"
        self.b5["font"] = ("Calibri", "9")
        self.b5["width"] = 20
        self.b5["command"] = self.converteParaCinza
        self.b5.pack ()

        self.b6 = Button(self.widget1)
        self.b6["text"] = "Get Matriz"
        self.b6["font"] = ("Calibri", "9")
        self.b6["width"] = 20
        self.b6["command"] = self.getMatriz
        self.b6.pack ()

        self.b7 = Button(self.widget1)
        self.b7["text"] = "Salvar"
        self.b7["font"] = ("Calibri", "9")
        self.b7["width"] = 20
        self.b7["command"] = self.salvar
        self.b7.pack ()

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

janela = Tk()
Application(janela)
janela.mainloop()