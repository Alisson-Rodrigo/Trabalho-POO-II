# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pesquisa_dica.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Pesquisa_dica(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 120, 601))
        self.frame.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 #D3D3D3);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 120, 81, 23))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 30, 81, 23))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 80, 81, 23))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color:  #AABAF2 ;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.voltar = QtWidgets.QPushButton(self.frame)
        self.voltar.setGeometry(QtCore.QRect(20, 570, 75, 23))
        self.voltar.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.voltar.setObjectName("voltar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 110, 75, 23))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color:  #add8e6;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#AABAF2 ;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 180, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 330, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 210, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 250, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(260, 170, 401, 31))
        self.plainTextEdit.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"\n"
"")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(260, 210, 401, 31))
        self.plainTextEdit_2.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"\n"
"")
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(260, 250, 401, 61))
        self.plainTextEdit_3.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"\n"
"\n"
"")
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(260, 320, 401, 71))
        self.plainTextEdit_4.setStyleSheet("color: black;\n"
"background-color: transparent;\n"
"\n"
"")
        self.plainTextEdit_4.setReadOnly(True)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 60, 421, 22))
        self.comboBox.setStyleSheet("background-color: transparent;\n"
"border: 1px solid black;")
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Cadastrar Dicas"))
        self.pushButton_2.setText(_translate("MainWindow", "Perfil"))
        self.pushButton_3.setText(_translate("MainWindow", "Pesquisar Dicas"))
        self.voltar.setText(_translate("MainWindow", "Deslogar"))
        self.label.setText(_translate("MainWindow", "ENCONTRE A DICA QUE DESEJA"))
        self.pushButton_4.setText(_translate("MainWindow", "Pesquisar"))
        self.label_2.setText(_translate("MainWindow", "Jogo"))
        self.label_4.setText(_translate("MainWindow", "Dica"))
        self.label_5.setText(_translate("MainWindow", "Data de lançamento"))
        self.label_3.setText(_translate("MainWindow", "Descrição"))
