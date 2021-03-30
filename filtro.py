from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np
from matplotlib import pyplot as plt

class Application:
    def __init__(self, master=None):

        self.widget1 = Frame(master)
        self.widget1.pack()

        self.msg = Label(self.widget1, text="Escolha um filtro e depois escolha uma imagem")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack ()

        self.botao = Button(self.widget1)
        self.botao["text"] = "Visualizar imagem normal"
        self.botao["font"] = ("Calibri", "9")
        self.botao["width"] = 50
        self.botao["command"] = self.normal_imagem

        self.botao1 = Button(self.widget1)
        self.botao1["text"] = "filtro escala de cinza"
        self.botao1["font"] = ("Calibri", "9")
        self.botao1["width"] = 50
        self.botao1["command"] = self.cinza_imagem

        self.botao2 = Button(self.widget1)
        self.botao2["text"] = "filtro inverter imagem"
        self.botao2["font"] = ("Calibri", "9")
        self.botao2["width"] = 50
        self.botao2["command"] = self.binaria_imagem

        self.botao3 = Button(self.widget1)
        self.botao3["text"] = "Detecta borda da imagem"
        self.botao3["font"] = ("Calibri", "9")
        self.botao3["width"] = 50
        self.botao3["command"] = self.detecta_bordas

        self.botao4 = Button(self.widget1)
        self.botao4["text"] = "Gaussian Blur - suavizando imagem"
        self.botao4["font"] = ("Calibri", "9")
        self.botao4["width"] = 50
        self.botao4["command"] = self.gaussian_blur

        self.botao.pack()
        self.botao1.pack()
        self.botao2.pack()
        self.botao3.pack()
        self.botao4.pack()
    

    def normal_imagem(self):

        #captura o caminho da imagem
        filename = filedialog.askopenfilename()
        print(filename)

        #ler e carrega a imagem
        img = cv2.imread(filename, 0)

        im = cv2.imread(filename, cv2.IMREAD_COLOR)
        cv2.imshow('Imagem normal', im)
        cv2.waitKey()

        #Display image
        im.show()
    
    def cinza_imagem(self):

        #captura o caminho da imagem
        filename = filedialog.askopenfilename()
        print(filename)

        #ler e carrega a imagem
        img = cv2.imread(filename, 0)

        im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        cv2.imshow('Escala de cinza', im)
        cv2.waitKey()

        #Display image
        plt.show()

    def binaria_imagem(self):

        #captura o caminho da imagem
        filename = filedialog.askopenfilename()
        print(filename)

        #ler e carrega a imagem
        img = cv2.imread(filename, 0)

        ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
        ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
        ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
        ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

        titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
        images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

        for i in range(6):
            plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])

        plt.show()

    def detecta_bordas(self):

        #captura o caminho da imagem
        filename = filedialog.askopenfilename()
        print(filename)

        #ler e carrega a imagem
        img = cv2.imread(filename, 0)

        edges = cv2.Canny(img,100,200)

        plt.subplot(121),plt.imshow(img,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        plt.show()

    def gaussian_blur(self):

        #captura o caminho da imagem
        filename = filedialog.askopenfilename()
        print(filename)

        #ler e carrega a imagem
        img = cv2.imread(filename, 0)

        blur = cv2.GaussianBlur(img,(5,5),0)

        plt.subplot(121),plt.imshow(img),plt.title('Original')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
        plt.xticks([]), plt.yticks([])

        plt.show()

        
root = Tk()
Application(root)
root.mainloop()