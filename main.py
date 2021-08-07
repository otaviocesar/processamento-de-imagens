from util.Imagem import *

def carregar():
    img1=Imagem()
    img1.carregar('img/lennaRGB.jpg')
    img1.mostrar('Testando lennaRGB.jpg')

def criarVazia():
    img2=Imagem()
    img2.criarVazia('RGB',100,200,)
    img2.mostrar('Vazia RGB 100x200')

def criarDeMatriz():
    img3=Imagem()
    mat=[[[255,255,255],[255,255,255],[255,255,255]],
         [[0,0,0],[0,0,0],[0,0,0]],
         [[0,0,0],[0,0,0],[0,0,0]]    ]
    img3.criarComMatriz(mat)
    img3.mostrar('Criando através de uma matriz pré-existente')

def converteParaRgb():
    img4 = Imagem()
    img4.carregar('img/lennaRGB.jpg')
    img4.mostrar()
    img4.toRGB()
    img4.mostrar()

def converteParaCinza():
    img4 = Imagem()
    img4.carregar('img/lennaRGB.jpg')
    img4.mostrar()
    img4.toGray()
    img4.mostrar()

def getMatriz():
    img =Imagem()
    # img.carregar('img/olho.png')
    img.carregar('img/lennaRGB.jpg')
    # img.criarVazia('L',4,5)
    mat=img.getMatriz()    
    for i in range(30):
        mat[0][i][i]=255
    img.criarComMatriz(mat)  
    img.mostrar()

def salvar():
    img =Imagem()
    img.carregar('img/lennaRGB.jpg')
    mat=img.getMatriz()    
    for i in range(100):
        mat[0][i][i]=200
        mat[0][i][i]=128
    img.criarComMatriz(mat)  
    img.mostrar()
    img.salvar('img/testeSalvar.png',img.TYPE_PNG())
    img.salvar('img/testeSalvar.jpg',img.TYPE_JPG())
    img.salvar('img/testeSalvar.gif',img.TYPE_GIF())
    img.salvar('img/testeSalvar.pdf',img.TYPE_PDF())

if __name__=="__main__":
     carregar() #ok
    # criarVazia() #ok
    #criarDeMatriz()    #ok
    # converteParaRgb() # ok
    # converteParaCinza() #ok
    # getMatriz() #ok
    # salvar() #ok
