import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from telaInicio import Tela_inical
from tela_cad import Tela_cad
from telaAbout import About_us
from home import Tela_home
from usuario import Usuairo
from Servidor import Metodos
from jogos import Jogos
from cad_jogos import Tela_jogos

class Ui_main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.Qstack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()

        self.tela_inical = Tela_inical()
        self.tela_inical.setupUi(self.stack0)

        self.tela_cadastro = Tela_cad()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_about = About_us()
        self.tela_about.setupUi(self.stack2)

        self.tela_home = Tela_home()
        self.tela_home.setupUi(self.stack3)

        self.tela_jogos = Tela_jogos()
        self.tela_jogos.setupUi(self.stack4)

        self.Qstack.addWidget(self.stack0)
        self.Qstack.addWidget(self.stack1)
        self.Qstack.addWidget(self.stack2)
        self.Qstack.addWidget(self.stack3)
        self.Qstack.addWidget(self.stack4)


class Main(QMainWindow, Ui_main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.metodos = Metodos()
        self.tela_inical.Botao_sair.clicked.connect(self.sair)
        self.tela_inical.Botao_sobre.clicked.connect(self.Tela_sobre)
        self.tela_inical.botaoCadastro.clicked.connect(self.Tela_cad)
        self.tela_inical.botaoLogin.clicked.connect(self.login)
        self.tela_cadastro.Botao_voltar.clicked.connect(self.voltar)
        self.tela_cadastro.Botao_cadastrar.clicked.connect(self.cadastrar)
        self.tela_about.pushButton.clicked.connect(self.voltar)
        self.tela_home.voltar.clicked.connect(self.voltar)
        self.tela_home.pushButton.clicked.connect(self.ir_jogos)
        self.tela_jogos.pushButton.clicked.connect(self.cadastrar_jogos)

    def cadastrar(self):
        nome = self.tela_cadastro.lineEdit_3.text()
        email = self.tela_cadastro.lineEdit_4.text()
        endereco = self.tela_cadastro.lineEdit.text()
        user = self.tela_cadastro.lineEdit_2.text()
        senha = self.tela_cadastro.lineEdit_5.text()
       
        u = Usuairo(nome, email, endereco, user, senha)
        if not (nome == None or email == None or senha == None or endereco == None or nome == '' or email == '' or senha == '' or endereco == ''):
            if not (self.metodos.verifica_tamsenha(senha)):
                if not (self.metodos.verifica_tamuser(user)):
                    if self.metodos.verifica_cadastro(user, email):
                            QMessageBox.information(
                                None, 'Atenção', 'O seu Email ou o user name informado já foi cadastrado na base de dados!')
                    else:
                            self.metodos.cadastrar(u)
                            QMessageBox.information(
                                None, 'Sucesso', 'Cadastro realizado com sucesso')
                            self.tela_cadastro.lineEdit_3.clear()
                            self.tela_cadastro.lineEdit_4.clear()
                            self.tela_cadastro.lineEdit_2.clear()
                            self.tela_cadastro.lineEdit.clear()
                            self.tela_cadastro.lineEdit_5.clear()
                else:
                    QMessageBox.information(None, "error", "O nome de usuario deve ser maior que 6 digitos")
            else:
                QMessageBox.information(None,'error', 'Sua senha deve ser maior que 8 digitos')
        else:
             QMessageBox.information(None, 'Atenção', 'Todos os valores devem ser preenchidos!')
    def login(self):
        email = self.tela_inical.campoUsuario.text()  
        senha = self.tela_inical.campoSenha.text()
        user = self.tela_inical.campoUsuario.text()
        if not (email == None or senha == None or email == '' or senha == ''):
            if self.metodos.login(email, senha):
                self.tela_inical.campoUsuario.clear()
                self.tela_inical.campoSenha.clear()
                self.Qstack.setCurrentIndex(3)
                QMessageBox.information(
                    None, 'Sucesso', 'Login realizado com sucesso')
            else:
                QMessageBox.information(
                    None, 'Atenção', 'Login ou senha incorretos')
                self.tela_inical.campoSenha.clear()
        else:
            QMessageBox.information(
                None, 'Atenção', 'Todos os valores devem ser preenchidos!')
    def cadastrar_jogos(self):
        nome = self.tela_jogos.lineEdit.text()
        data = self.tela_jogos.lineEdit_2.text()
        descricao = self.tela_jogos.lineEdit_3.text()
        dica = self.tela_jogos.lineEdit_4.text()
        j = Jogos(nome, data, descricao,dica)
        self.metodos.cad_jogos(j)
        QMessageBox.information(None,"Alerta","Sua dica foi cadastrada!")
        self.tela_jogos.lineEdit.clear()
        self.tela_jogos.lineEdit_2.clear()
        self.tela_jogos.lineEdit_3.clear()
        self.tela_jogos.lineEdit_4.clear()
    

    
    def voltar(self):
        self.Qstack.setCurrentIndex(0)

    def Tela_cad(self):
        self.Qstack.setCurrentIndex(1)

    def Tela_sobre(self):
        self.Qstack.setCurrentIndex(2)

    def sair(self):
        exit()

    def ir_jogos(self):
        self.Qstack.setCurrentIndex(4)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
