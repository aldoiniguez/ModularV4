from re import S
import sys
from tkinter.messagebox import NO
from traceback import print_tb
from tracemalloc import stop
import numpy as np
from pandas_datareader import test
from ui import*
from PySide2 import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import cv2, imutils
import sys
import numpy as np
from qt_material import apply_stylesheet
#import sip.
from PIL import ImageQt
import seaborn as sns
import serial, time
sns.set_style("darkgrid", {"axes.facecolor": ".9"})

#arduino = serial.Serial('COM3', baudrate = 9600, timeout = 1)
time.sleep(2)

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.ui.Boton_Iniciar_Camara.clicked.connect(self.iniciarCamara)
        self.ui.Stop_Camera.clicked.connect(self.StopCamera)
        self.ui.view_camera.mousePressEvent = self.getPos
        self.ui.GiroDer.clicked.connect(self.giroDer)
        self.ui.GiroIzq.clicked.connect(self.giroIzq)
        self.ui.Boton_Cargar_Imagen.clicked.connect(self.button_cargar_clicked)
        self.fig, self.ax = plt.subplots(2, sharex=False, sharey=True,figsize=(8,8))
        self.canvas1 = FigureCanvas(self.fig)
        self.ui.grafica_1.addWidget(self.canvas1)
        self.picFlag = False
        self.image = 0

        insert_axs(self.ax,self.fig,"Camara",1,1)

        self.fig2, self.ax2 = plt.subplots(1, sharex=False, sharey=True,figsize=(8,8))
        self.canvas2 = FigureCanvas(self.fig2)
        self.ui.grafica_2.addWidget(self.canvas2)

    def getPos(self, pos):
        desfaceB = self.ui.sliderB.value()
        desfaceG = self.ui.sliderG.value()
        desfaceR = self.ui.sliderR.value()
        print(desfaceB)
        x = pos.x()
        y = pos.y() 
        print(x,y)
        pixMap = QPixmap( self.ui.view_camera.pixmap())
        image = pixMap.toImage()
        print(type(image))
        color = image.pixelColor( x, y )
        r, g, b, a = color.getRgb()
        print(color.getRgb())
        print(color.getHsv())
        self.ui.Pixel.setStyleSheet('background-color: rgb({},{},{});'.format(r, g, b))


        self.ui.lowerBox1.setValue(b-desfaceB)
        self.ui.lowerBox2.setValue(g-desfaceG)
        self.ui.lowerBox3.setValue(r-desfaceR)
        self.ui.upperBox1.setValue(b+desfaceB)
        self.ui.upperBox2.setValue(g+desfaceG)
        self.ui.upperBox3.setValue(r+desfaceR)
        if self.picFlag:
            print("Foto ya cargada")
            self.setPhoto(self.image)

    def iniciarCamara(self):
        self.Worker1 = Worker1(self.ui,self.canvas1,self.ax,self.fig,self.canvas2,self.ax2,self.fig2)
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.Worker1.ImageColor.connect(self.ImageUpdateColor)
        self.picFlag = False

    def ImageUpdateSlot(self, Image):
        self.ui.view_camera.setPixmap(QtGui.QPixmap.fromImage(Image))


    def ImageUpdateColor(self, Image):
        self.ui.view_camera_2.setPixmap(QtGui.QPixmap.fromImage(Image))

    def StopCamera(self):
        try:
            self.Worker1.stop()
        except:
            pass
 
    def giroIzq(self):
        print("Giro a la izq")
        #arduino.write(b'1') #activar cuando se tenga en conexion el arduino
        time.sleep(0.1)

    def giroDer(self):
        print("Giro a la der")
        #arduino.write(b'2')
        time.sleep(0.1)

    def button_cargar_clicked(self):
        try:
            self.StopCamera()
        except:
            pass

        print("Cargar imagen")
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)
        print("Imagen mostrada")
    
    def setPhoto(self,image):
        global area_pb 
        colorimage = QImage(image, image.shape[1],image.shape[0],image.strides[0],QImage.Format_RGB888)
        colorimage = colorimage.scaled(251, 141, Qt.KeepAspectRatio)
        self.ventana2 = self.findChild(QLabel,"view_camera_2")
        self.ventana2.setPixmap(QtGui.QPixmap.fromImage(colorimage))
        
        tmp = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        tmp = imutils.resize(image,height=440)
        frame = cv2.cvtColor(tmp, cv2.COLOR_BGR2RGB)
        lower_color = np.array([self.ui.lowerBox1.value(), self.ui.lowerBox2.value(), self.ui.lowerBox3.value()])
        upper_color = np.array([self.ui.upperBox1.value(), self.ui.upperBox2.value(), self.ui.upperBox3.value()])
        area_pb = self.ui.area_pb.value()
        Pic,cX,cY = ProcesarBordes(frame,lower_color,upper_color)

        tmp = QImage(Pic, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.ventana = self.findChild(QLabel,"view_camera")
        self.ventana.setPixmap(QtGui.QPixmap.fromImage(tmp))
        self.picFlag =True
        graficar_cross(frame,cX,cY,self.canvas1,self.ax,self.fig,"Imagen cargada")
        histogram(frame,self.canvas2,self.ax2)

################################# Class Worker

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    ImageColor = pyqtSignal(QImage)

    def __init__(self,ui,canvas1,ax,fig,canvas2,ax2,fig2):
        super().__init__()
        self.ui = ui
        self.canvas1 = canvas1
        self.ax = ax
        self.fig = fig
        self.canvas2 = canvas2
        self.ax2 = ax2
        self.fig2 = fig2
        

    def run(self):   
        
        print("Camara activada")
        #
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        Capture.set(3, 780)
        Capture.set(4, 440)
        while self.ThreadActive:
            ret, frame = Capture.read()
            
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                L,U = self.update_umbral()
                FlippedImage,cX,cY = ProcesarBordes(frame,L,U)
                
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(780, 440, Qt.KeepAspectRatio)

                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                new = ConvertToQtFormat.scaled(468, 264, Qt.KeepAspectRatio)

                self.ImageUpdate.emit(Pic)
                self.ImageColor.emit(new)
                graficar_cross(Image,cX,cY,self.canvas1,self.ax,self.fig,"Camara")
                histogram(frame,self.canvas2,self.ax2)


        Capture.release()

        

    def stop(self):
        print("Camara detenida")
        self.ThreadActive = False
        #self.ui.grafica_1.removeWidget(self.canvas1)
        self.quit()


    def update_umbral(self):
        global area_pb
        global Bslide
        global Gslide
        global Rslide
        Bslide = self.ui.sliderB.value()
        Gslide = self.ui.sliderG.value()
        Rslide = self.ui.sliderR.value()
        lower_color = np.array([self.ui.lowerBox1.value()-Bslide, self.ui.lowerBox2.value()-Gslide, self.ui.lowerBox3.value()-Rslide])
        upper_color = np.array([self.ui.upperBox1.value()+Bslide, self.ui.upperBox2.value()+Gslide, self.ui.upperBox3.value()+Rslide])
        area_pb = self.ui.area_pb.value()

        return lower_color,upper_color#,area
    
    
#################### Funciones fuera de las clases

def ProcesarBordes(img,lower_color,upper_color):#, lower_color, upper_color): # Esta funcion procesa los bordes de un color definido ademas de calcular el centro de masa y agregar un cursor 
    # Procesar Bordes
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blurred_frame = cv2.GaussianBlur(hsv, (15, 15), 0)
    
    mask = cv2.inRange(img, lower_color, upper_color)
    ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(mask, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE) #image=thresh
    image_temp = cv2.cvtColor(mask,cv2.COLOR_BGR2RGB)

    #image_contours = cv2.cvtColor(img_gray,cv2.COLOR_BGR2RGB)#gray
    image_contours = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#rgb
    cX = 0
    cY = 0
    count = 1
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area>area_pb: # este 5000 adherirlo al UI
            cv2.drawContours(image=image_contours, contours=contours, contourIdx=-1, color=(255, 0, 0), thickness=1, lineType=cv2.LINE_4)
            peri = cv2.arcLength(cnt,True)
            #approx= cv2.approxPolyDP(cnt,0.02*peri,True) #marca varios cross
            approx = max(contours, key = cv2.contourArea) #marca el predominante
            x,y,w,h = cv2.boundingRect(approx)
            cX = x+int(w/2)
            cY = y+int(h/2)
            cv2.circle(image_contours, (cX, cY), 5, (255, 0, 255), -1)
            cv2.putText(image_contours, "P"+str(count), (cX + 20, cY + 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 1)
            cv2.line(image_contours,(0,cY),(img.shape[1],cY),(255,127,0), 1)
            cv2.line(image_contours,(cX,0),(cX,img.shape[0]),(255,127,0), 1)
            count+=1
    
    finalmask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)

    return(image_contours,cX,cY)

def graficar_cross(img,cX,cY,canvas,ax,fig,str):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ax[0].cla()
    ax[0].plot(gray[cY])
    ax[0].axvline(x=cX,color='r',linestyle='dashed')
    ax[1].cla()
    ax[1].plot(horizontal_array(gray,cX)) # cx tines que mandar el resultado de self.horizontal_array(gray,cX)
    ax[1].axvline(x=cY,color='r',linestyle='dashed')
    h, w = gray.shape[0], gray.shape[1]
    insert_axs(ax,fig,str,w,h)
    canvas.draw()

def horizontal_array(args,X):
        arr_temp = []
        [arr_temp.append(i[X]) for i in args]
        return arr_temp

def insert_axs(ax,fig,str,w,h):
    
    font = {
        'weight': 'normal',
        'size': 6
    }

    plt.rc('font', **font)
    ax[0].set_title('Horizontal cross ' + str)
    ax[0].grid(True)
    ax[0].set_ylim(0,270)
    ax[0].set_xlim(0,w)
    fig.supylabel(r"Intensidad del Pixel $(bits)$", fontsize=9, color="blue")

    ax[1].set_title('Vertical cross ' + str)
    ax[1].grid(True)
    ax[1].set_ylim(0,270)
    ax[1].set_xlim(0,h)

def histogram(img,canvas,ax):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    arr = np.matrix.flatten(gray)
    ax.cla()
    ax.hist(arr,bins=range(0,255,5))
    ax.set_ylim(0,35000)
    canvas.draw()

################### Funcion Main

if __name__ == "__main__":
    app = QApplication(sys.argv)
    extra = {
        # Font
        'font_family': 'system-ui',
        'font_size': '11px',
        'line_height': '11px',
        # Density Scale
        'density_scale': '-2',
    }
    #apply_stylesheet(app, 'dark_amber.xml', invert_secondary=False, extra=extra)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())  
