# Form implementation generated from reading ui file 'c:\Users\kawig\Documents\GitHub\pyqtt-paiint\src\ui\paint.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Paint(object):
    def setupUi(self, Paint):
        Paint.setObjectName("Paint")
        Paint.resize(1059, 677)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Paint.sizePolicy().hasHeightForWidth())
        Paint.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=Paint)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.maincontainer = QtWidgets.QHBoxLayout()
        self.maincontainer.setObjectName("maincontainer")
        self.container = QtWidgets.QVBoxLayout()
        self.container.setObjectName("container")
        self.columnaTools = QtWidgets.QHBoxLayout()
        self.columnaTools.setObjectName("columnaTools")
        self.columnaHerramientas1 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.columnaHerramientas1.setObjectName("columnaHerramientas1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.columnaHerramientas1)
        self.formLayout_2.setObjectName("formLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem)
        self.btnBorrador = QtWidgets.QPushButton(parent=self.columnaHerramientas1)
        self.btnBorrador.setAutoFillBackground(False)
        self.btnBorrador.setStyleSheet("image: url(:/borrador.png);")
        self.btnBorrador.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/borrador.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.btnBorrador.setIcon(icon)
        self.btnBorrador.setIconSize(QtCore.QSize(32, 32))
        self.btnBorrador.setObjectName("btnBorrador")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.btnBorrador)
        self.btnCuentaGotas = QtWidgets.QPushButton(parent=self.columnaHerramientas1)
        self.btnCuentaGotas.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/cuenta_gotas.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCuentaGotas.setIcon(icon1)
        self.btnCuentaGotas.setIconSize(QtCore.QSize(32, 32))
        self.btnCuentaGotas.setObjectName("btnCuentaGotas")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.btnCuentaGotas)
        self.btnLapiz = QtWidgets.QPushButton(parent=self.columnaHerramientas1)
        self.btnLapiz.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/lapiz.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnLapiz.setIcon(icon2)
        self.btnLapiz.setIconSize(QtCore.QSize(32, 32))
        self.btnLapiz.setObjectName("btnLapiz")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.btnLapiz)
        self.btnCuadrado = QtWidgets.QPushButton(parent=self.columnaHerramientas1)
        self.btnCuadrado.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/cuadrado.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCuadrado.setIcon(icon3)
        self.btnCuadrado.setIconSize(QtCore.QSize(32, 32))
        self.btnCuadrado.setObjectName("btnCuadrado")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.btnCuadrado)
        self.btnCuadradoRedondo = QtWidgets.QPushButton(parent=self.columnaHerramientas1)
        self.btnCuadradoRedondo.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/cuadrado_redondo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCuadradoRedondo.setIcon(icon4)
        self.btnCuadradoRedondo.setIconSize(QtCore.QSize(32, 32))
        self.btnCuadradoRedondo.setObjectName("btnCuadradoRedondo")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.btnCuadradoRedondo)
        self.checkBox_6 = QtWidgets.QCheckBox(parent=self.columnaHerramientas1)
        self.checkBox_6.setIconSize(QtCore.QSize(32, 32))
        self.checkBox_6.setObjectName("checkBox_6")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.checkBox_6)
        self.columnaTools.addWidget(self.columnaHerramientas1)
        self.columnaHerramientas2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.columnaHerramientas2.setObjectName("columnaHerramientas2")
        self.formLayout = QtWidgets.QFormLayout(self.columnaHerramientas2)
        self.formLayout.setObjectName("formLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem1)
        self.btnCubeta = QtWidgets.QPushButton(parent=self.columnaHerramientas2)
        self.btnCubeta.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/cubetas.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.btnCubeta.setIcon(icon5)
        self.btnCubeta.setIconSize(QtCore.QSize(32, 32))
        self.btnCubeta.setObjectName("btnCubeta")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.btnCubeta)
        self.btnPincel = QtWidgets.QPushButton(parent=self.columnaHerramientas2)
        self.btnPincel.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/pincel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnPincel.setIcon(icon6)
        self.btnPincel.setIconSize(QtCore.QSize(32, 32))
        self.btnPincel.setObjectName("btnPincel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.btnPincel)
        self.btnLinea = QtWidgets.QPushButton(parent=self.columnaHerramientas2)
        self.btnLinea.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/linea.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnLinea.setIcon(icon7)
        self.btnLinea.setIconSize(QtCore.QSize(32, 32))
        self.btnLinea.setObjectName("btnLinea")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.btnLinea)
        self.btnCirculo = QtWidgets.QPushButton(parent=self.columnaHerramientas2)
        self.btnCirculo.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/circulo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCirculo.setIcon(icon8)
        self.btnCirculo.setIconSize(QtCore.QSize(32, 32))
        self.btnCirculo.setObjectName("btnCirculo")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.btnCirculo)
        self.btnTriangulo = QtWidgets.QPushButton(parent=self.columnaHerramientas2)
        self.btnTriangulo.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/triangulo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnTriangulo.setIcon(icon9)
        self.btnTriangulo.setIconSize(QtCore.QSize(32, 32))
        self.btnTriangulo.setObjectName("btnTriangulo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.btnTriangulo)
        self.columnaTools.addWidget(self.columnaHerramientas2)
        self.container.addLayout(self.columnaTools)
        self.container.setStretch(0, 2)
        self.maincontainer.addLayout(self.container)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.maincontainer.addWidget(self.line)
        self.columnaColores = QtWidgets.QVBoxLayout()
        self.columnaColores.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.columnaColores.setObjectName("columnaColores")
        self.filaColores = QtWidgets.QVBoxLayout()
        self.filaColores.setObjectName("filaColores")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnNegro = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnNegro.setAutoFillBackground(False)
        self.btnNegro.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.btnNegro.setText("")
        self.btnNegro.setDefault(False)
        self.btnNegro.setFlat(False)
        self.btnNegro.setObjectName("btnNegro")
        self.horizontalLayout_2.addWidget(self.btnNegro)
        self.btnGris = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnGris.setStyleSheet("background-color: rgb(118, 118, 118);")
        self.btnGris.setText("")
        self.btnGris.setFlat(False)
        self.btnGris.setObjectName("btnGris")
        self.horizontalLayout_2.addWidget(self.btnGris)
        self.btnMarron = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnMarron.setStyleSheet("background-color: rgb(85, 0, 0);")
        self.btnMarron.setText("")
        self.btnMarron.setFlat(False)
        self.btnMarron.setObjectName("btnMarron")
        self.horizontalLayout_2.addWidget(self.btnMarron)
        self.btnRojo = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRojo.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btnRojo.setText("")
        self.btnRojo.setFlat(False)
        self.btnRojo.setObjectName("btnRojo")
        self.horizontalLayout_2.addWidget(self.btnRojo)
        self.btnAmarillo = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAmarillo.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.btnAmarillo.setText("")
        self.btnAmarillo.setFlat(False)
        self.btnAmarillo.setObjectName("btnAmarillo")
        self.horizontalLayout_2.addWidget(self.btnAmarillo)
        self.btnAzul = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAzul.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.btnAzul.setText("")
        self.btnAzul.setFlat(False)
        self.btnAzul.setObjectName("btnAzul")
        self.horizontalLayout_2.addWidget(self.btnAzul)
        self.btnVerde = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnVerde.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.btnVerde.setText("")
        self.btnVerde.setFlat(False)
        self.btnVerde.setObjectName("btnVerde")
        self.horizontalLayout_2.addWidget(self.btnVerde)
        self.filaColores.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnBlanco = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnBlanco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnBlanco.setText("")
        self.btnBlanco.setFlat(False)
        self.btnBlanco.setObjectName("btnBlanco")
        self.horizontalLayout_3.addWidget(self.btnBlanco)
        self.btnHueso = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnHueso.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.btnHueso.setText("")
        self.btnHueso.setFlat(False)
        self.btnHueso.setObjectName("btnHueso")
        self.horizontalLayout_3.addWidget(self.btnHueso)
        self.btnCafe = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCafe.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.btnCafe.setText("")
        self.btnCafe.setFlat(False)
        self.btnCafe.setObjectName("btnCafe")
        self.horizontalLayout_3.addWidget(self.btnCafe)
        self.btnRosa = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRosa.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.btnRosa.setText("")
        self.btnRosa.setFlat(False)
        self.btnRosa.setObjectName("btnRosa")
        self.horizontalLayout_3.addWidget(self.btnRosa)
        self.btnLima = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLima.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.btnLima.setText("")
        self.btnLima.setFlat(False)
        self.btnLima.setObjectName("btnLima")
        self.horizontalLayout_3.addWidget(self.btnLima)
        self.btnCyan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCyan.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.btnCyan.setText("")
        self.btnCyan.setFlat(False)
        self.btnCyan.setObjectName("btnCyan")
        self.horizontalLayout_3.addWidget(self.btnCyan)
        self.btnMenta = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnMenta.setStyleSheet("background-color: rgb(0, 255, 127)")
        self.btnMenta.setText("")
        self.btnMenta.setFlat(False)
        self.btnMenta.setObjectName("btnMenta")
        self.horizontalLayout_3.addWidget(self.btnMenta)
        self.filaColores.addLayout(self.horizontalLayout_3)
        self.columnaColores.addLayout(self.filaColores)
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.columnaColores.addWidget(self.line_2)
        self.WPaint = QtWidgets.QWidget(parent=self.centralwidget)
        self.WPaint.setAutoFillBackground(False)
        self.WPaint.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WPaint.setObjectName("WPaint")
        self.columnaColores.addWidget(self.WPaint)
        self.columnaColores.setStretch(2, 2)
        self.maincontainer.addLayout(self.columnaColores)
        self.maincontainer.setStretch(0, 1)
        self.maincontainer.setStretch(2, 5)
        self.horizontalLayout_5.addLayout(self.maincontainer)
        Paint.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Paint)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 21))
        self.menubar.setObjectName("menubar")
        Paint.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Paint)
        self.statusbar.setObjectName("statusbar")
        Paint.setStatusBar(self.statusbar)

        self.retranslateUi(Paint)
        QtCore.QMetaObject.connectSlotsByName(Paint)

    def retranslateUi(self, Paint):
        _translate = QtCore.QCoreApplication.translate
        Paint.setWindowTitle(_translate("Paint", "MainWindow"))
        self.checkBox_6.setText(_translate("Paint", "Relleno"))
