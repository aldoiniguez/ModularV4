# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 862)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 1101, 821))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_camara = QtWidgets.QWidget()
        self.tab_camara.setObjectName("tab_camara")
        self.view_camera = QtWidgets.QLabel(self.tab_camara)
        self.view_camera.setGeometry(QtCore.QRect(20, 10, 780, 440))
        self.view_camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.view_camera.setFrameShadow(QtWidgets.QFrame.Plain)
        self.view_camera.setText("")
        self.view_camera.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.view_camera.setObjectName("view_camera")
        self.label_2 = QtWidgets.QLabel(self.tab_camara)
        self.label_2.setGeometry(QtCore.QRect(810, 220, 251, 16))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_camara)
        self.layoutWidget.setGeometry(QtCore.QRect(840, 240, 221, 48))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lowerBox1 = QtWidgets.QSpinBox(self.layoutWidget)
        self.lowerBox1.setMaximum(255)
        self.lowerBox1.setProperty("value", 36)
        self.lowerBox1.setObjectName("lowerBox1")
        self.gridLayout.addWidget(self.lowerBox1, 0, 0, 1, 1)
        self.lowerBox2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.lowerBox2.setMaximum(255)
        self.lowerBox2.setProperty("value", 58)
        self.lowerBox2.setObjectName("lowerBox2")
        self.gridLayout.addWidget(self.lowerBox2, 0, 1, 1, 1)
        self.lowerBox3 = QtWidgets.QSpinBox(self.layoutWidget)
        self.lowerBox3.setMaximum(255)
        self.lowerBox3.setProperty("value", 100)
        self.lowerBox3.setObjectName("lowerBox3")
        self.gridLayout.addWidget(self.lowerBox3, 0, 2, 1, 1)
        self.upperBox1 = QtWidgets.QSpinBox(self.layoutWidget)
        self.upperBox1.setMaximum(255)
        self.upperBox1.setProperty("value", 255)
        self.upperBox1.setObjectName("upperBox1")
        self.gridLayout.addWidget(self.upperBox1, 1, 0, 1, 1)
        self.upperBox2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.upperBox2.setMaximum(255)
        self.upperBox2.setProperty("value", 255)
        self.upperBox2.setObjectName("upperBox2")
        self.gridLayout.addWidget(self.upperBox2, 1, 1, 1, 1)
        self.upperBox3 = QtWidgets.QSpinBox(self.layoutWidget)
        self.upperBox3.setMaximum(255)
        self.upperBox3.setProperty("value", 255)
        self.upperBox3.setObjectName("upperBox3")
        self.gridLayout.addWidget(self.upperBox3, 1, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_camara)
        self.layoutWidget1.setGeometry(QtCore.QRect(810, 10, 251, 59))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Boton_Cargar_Imagen = QtWidgets.QPushButton(self.layoutWidget1)
        self.Boton_Cargar_Imagen.setObjectName("Boton_Cargar_Imagen")
        self.gridLayout_2.addWidget(self.Boton_Cargar_Imagen, 0, 0, 1, 2)
        self.Boton_Iniciar_Camara = QtWidgets.QPushButton(self.layoutWidget1)
        self.Boton_Iniciar_Camara.setEnabled(True)
        self.Boton_Iniciar_Camara.setCheckable(False)
        self.Boton_Iniciar_Camara.setObjectName("Boton_Iniciar_Camara")
        self.gridLayout_2.addWidget(self.Boton_Iniciar_Camara, 1, 0, 1, 1)
        self.Stop_Camera = QtWidgets.QPushButton(self.layoutWidget1)
        self.Stop_Camera.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Modular_V2/pictures/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Stop_Camera.setIcon(icon)
        self.Stop_Camera.setIconSize(QtCore.QSize(20, 20))
        self.Stop_Camera.setObjectName("Stop_Camera")
        self.gridLayout_2.addWidget(self.Stop_Camera, 1, 1, 1, 1)
        self.GraphicsP1 = QtWidgets.QFrame(self.tab_camara)
        self.GraphicsP1.setGeometry(QtCore.QRect(20, 460, 781, 321))
        self.GraphicsP1.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius: 15px;\n"
"border: 1px solid #000000;")
        self.GraphicsP1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.GraphicsP1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.GraphicsP1.setObjectName("GraphicsP1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.GraphicsP1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 761, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.grafica_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.grafica_1.setContentsMargins(0, 0, 0, 0)
        self.grafica_1.setObjectName("grafica_1")
        self.GraphicsP1_2 = QtWidgets.QFrame(self.tab_camara)
        self.GraphicsP1_2.setGeometry(QtCore.QRect(810, 460, 251, 321))
        self.GraphicsP1_2.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius: 15px;\n"
"border: 1px solid #000000;")
        self.GraphicsP1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.GraphicsP1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.GraphicsP1_2.setObjectName("GraphicsP1_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.GraphicsP1_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 231, 301))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.grafica_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.grafica_2.setContentsMargins(0, 0, 0, 0)
        self.grafica_2.setObjectName("grafica_2")
        self.label = QtWidgets.QLabel(self.tab_camara)
        self.label.setGeometry(QtCore.QRect(810, 240, 21, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.tab_camara)
        self.label_3.setGeometry(QtCore.QRect(810, 270, 21, 16))
        self.label_3.setObjectName("label_3")
        self.GiroIzq = QtWidgets.QPushButton(self.tab_camara)
        self.GiroIzq.setGeometry(QtCore.QRect(810, 430, 121, 21))
        self.GiroIzq.setObjectName("GiroIzq")
        self.GiroDer = QtWidgets.QPushButton(self.tab_camara)
        self.GiroDer.setGeometry(QtCore.QRect(940, 430, 121, 21))
        self.GiroDer.setObjectName("GiroDer")
        self.label_4 = QtWidgets.QLabel(self.tab_camara)
        self.label_4.setGeometry(QtCore.QRect(810, 400, 251, 20))
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.view_camera_2 = QtWidgets.QLabel(self.tab_camara)
        self.view_camera_2.setGeometry(QtCore.QRect(810, 70, 251, 141))
        self.view_camera_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.view_camera_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.view_camera_2.setText("")
        self.view_camera_2.setAlignment(QtCore.Qt.AlignCenter)
        self.view_camera_2.setObjectName("view_camera_2")
        self.Pixel = QtWidgets.QLabel(self.tab_camara)
        self.Pixel.setGeometry(QtCore.QRect(810, 320, 51, 21))
        self.Pixel.setFrameShape(QtWidgets.QFrame.Box)
        self.Pixel.setText("")
        self.Pixel.setObjectName("Pixel")
        self.area_pb = QtWidgets.QSpinBox(self.tab_camara)
        self.area_pb.setGeometry(QtCore.QRect(810, 370, 51, 21))
        self.area_pb.setMaximum(15000)
        self.area_pb.setProperty("value", 1500)
        self.area_pb.setObjectName("area_pb")
        self.sliderB = QtWidgets.QSlider(self.tab_camara)
        self.sliderB.setGeometry(QtCore.QRect(900, 310, 161, 22))
        self.sliderB.setMaximum(40)
        self.sliderB.setProperty("value", 15)
        self.sliderB.setOrientation(QtCore.Qt.Horizontal)
        self.sliderB.setObjectName("sliderB")
        self.sliderG = QtWidgets.QSlider(self.tab_camara)
        self.sliderG.setGeometry(QtCore.QRect(900, 340, 161, 22))
        self.sliderG.setMaximum(40)
        self.sliderG.setProperty("value", 15)
        self.sliderG.setOrientation(QtCore.Qt.Horizontal)
        self.sliderG.setObjectName("sliderG")
        self.sliderR = QtWidgets.QSlider(self.tab_camara)
        self.sliderR.setGeometry(QtCore.QRect(900, 370, 161, 22))
        self.sliderR.setMaximum(40)
        self.sliderR.setProperty("value", 15)
        self.sliderR.setOrientation(QtCore.Qt.Horizontal)
        self.sliderR.setObjectName("sliderR")
        self.label_5 = QtWidgets.QLabel(self.tab_camara)
        self.label_5.setGeometry(QtCore.QRect(820, 350, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_camara)
        self.label_6.setGeometry(QtCore.QRect(820, 300, 31, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_camara)
        self.label_7.setGeometry(QtCore.QRect(880, 310, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_camara)
        self.label_8.setGeometry(QtCore.QRect(880, 340, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_camara)
        self.label_9.setGeometry(QtCore.QRect(880, 370, 47, 13))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_camara, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGenerar_Reporte = QtWidgets.QAction(MainWindow)
        self.actionGenerar_Reporte.setObjectName("actionGenerar_Reporte")
        self.menuFile.addAction(self.actionGenerar_Reporte)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Parametros de mascara de Color"))
        self.Boton_Cargar_Imagen.setText(_translate("MainWindow", "Cargar Imagen"))
        self.Boton_Iniciar_Camara.setText(_translate("MainWindow", "Camara"))
        self.label.setText(_translate("MainWindow", "Baja"))
        self.label_3.setText(_translate("MainWindow", "Alta"))
        self.GiroIzq.setText(_translate("MainWindow", "Girar Izquierda"))
        self.GiroDer.setText(_translate("MainWindow", "Girar Derecha"))
        self.label_4.setText(_translate("MainWindow", "Motor a pasos"))
        self.label_5.setText(_translate("MainWindow", "Area"))
        self.label_6.setText(_translate("MainWindow", "Color"))
        self.label_7.setText(_translate("MainWindow", "B"))
        self.label_8.setText(_translate("MainWindow", "G"))
        self.label_9.setText(_translate("MainWindow", "R"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_camara), _translate("MainWindow", "Inicio"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionGenerar_Reporte.setText(_translate("MainWindow", "Generar Reporte"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())