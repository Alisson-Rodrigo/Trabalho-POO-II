import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from telaInicio import  Tela_inical
from tela_cad import Tela_cad
from telaAbout import About_us
from usuario import Usuairo
from cadastro import metodos


class Ui_main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.Qstack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inical = Tela_inical()
        self.tela_inical.setupUi(self.stack0)

        self.tela_cadastro = Tela_cad()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_about = About_us()
        self.tela_about.setupUi(self.stack2)

        self.Qstack.addWidget(self.stack0)
        self.Qstack.addWidget(self.stack1)
        self.Qstack.addWidget(self.stack2)


class Main(QMainWindow, Ui_main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.metodos = metodos()
        self.tela_inical.Botao_sair.clicked.connect(self.sair)
        self.tela_inical.Botao_sobre.clicked.connect(self.Tela_sobre)
        self.tela_inical.botaoCadastro.clicked.connect(self.Tela_cad)
        #self.tela_inical.botaoLogin.connect(self.Tela_login)
        self.tela_cadastro.Botao_voltar.clicked.connect(self.voltar)
        self.tela_cadastro.Botao_cadastrar.clicked.connect(self.cadastrar)
        self.tela_about.pushButton.clicked.connect(self.voltar)
    '''
        self.tela_inical.Botao_buscar.clicked.connect(
            self.abrirTelaBuscar)
        self.tela_inical.Botao_sair.clicked.connect(self.sair)

        self.tela_cadastro.Botao_cadastrar.clicked.connect(
            self.botao_cadastrar)
        self.tela_cadastro.Botao_voltar.clicked.connect(self.voltarTela)
        self.tela_busca.Botao_buscar.clicked.connect(
            self.botao_buscar)
        self.tela_busca.pushButton_2.clicked.connect(self.voltarTela)
        self.tela_busca.Botao_excluir.clicked.connect(self.excluir)

    def botao_cadastrar(self):
        nome = self.tela_cadastro.lineEdit_3.text()
        endereco = self.tela_cadastro.lineEdit_4.text()
        nascimento = self.tela_cadastro.lineEdit_2.text()
        cpf = self.tela_cadastro.lineEdit.text()
        p = Pessoa(nome,endereco,nascimento,cpf)
        if not (nome == None or endereco == None or nascimento == None or cpf == None or cpf == '' or nome == '' or endereco == '' or nascimento == ''):
            
            if self.cad.cadastrar(p):
                QMessageBox.information(
                    None, 'Sucesso', 'Cadastro realizado com sucesso!')
                self.tela_cadastro.lineEdit_3.clear()
                self.tela_cadastro.lineEdit_4.clear()
                self.tela_cadastro.lineEdit_2.clear()
                self.tela_cadastro.lineEdit.clear()
            else:
                QMessageBox.information(
                    None, 'Atenção', 'O CPF informado já foi cadastrado na base de dados!')
        else:
            QMessageBox.information(
                None, 'Atenção', 'Todos os valores devem ser preenchidos!')
            self.tela_cadastro.lineEdit_3.clear()
            self.tela_cadastro.lineEdit_4.clear()
            self.tela_cadastro.lineEdit_2.clear()
            self.tela_cadastro.lineEdit.clear()

    def botao_buscar(self):
        cpf = self.tela_busca.lineEdit.text()

        if cpf:
            pessoa = self.cad.busca(cpf)

            if pessoa:
                self.tela_busca.lineEdit_2.setText(pessoa.nome)
                self.tela_busca.lineEdit_4.setText(pessoa.nascimento)
                self.tela_busca.lineEdit_3.setText(pessoa.endereco)
            else:
                QMessageBox.information(
                    None, 'Atenção', 'CPF não encontrado na base de dados!')
        else:
            QMessageBox.information(
                None, 'Atenção', 'Por favor, informe o CPF para buscar!')

    def abrirTelaCad(self):
        self.Qstack.setCurrentIndex(1)

    def abrirTelaBuscar(self):
        self.Qstack.setCurrentIndex(2)

    def voltarTela(self):
        self.Qstack.setCurrentIndex(0)
    
    def excluir(self):
        cpf = self.tela_busca.lineEdit.text()
        busca = self.cad.busca(cpf)
        if busca != None:
            retorno = QMessageBox.question(
                None,'Exlcuir', 'Deseja realmente excluir',QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
            
            if retorno == QMessageBox.Yes:
                self.cad.excluir(cpf)
                QMessageBox.information(None,'Funcionou','Excluido com sucesso')
                self.tela_busca.lineEdit_3.clear()
                self.tela_busca.lineEdit_4.clear()
                self.tela_busca.lineEdit_2.clear()
                self.tela_busca.lineEdit.clear()

        else:
            QMessageBox.information(None,'Funcionou','Pessoa não econtrada')

    '''
    def cadastrar(self):
        nome = self.tela_cadastro.lineEdit_3.text()
        email = self.tela_cadastro.lineEdit_4.text()
        endereco = self.tela_cadastro.lineEdit.text()
        cpf = self.tela_cadastro.lineEdit_2.text()
        senha = self.tela_cadastro.lineEdit_5.text()
        u = Usuairo(nome,email,endereco,cpf,senha)
        if not (nome == None  or email == None or endereco == None or cpf == None
                or senha == None or nome == '' or email == '' or endereco == '' or cpf == ''):
            if self.metodos.verifica_cadastro(cpf):
                QMessageBox.information(None,'Atenção','O CPF informado já foi cadastrado na base de dados!')
            else:
                self.metodos.cadastrar(u)
                QMessageBox.information(None,'Sucesso','Cadastro realizado com sucesso')
                self.tela_cadastro.lineEdit_3.clear()
                self.tela_cadastro.lineEdit_4.clear()
                self.tela_cadastro.lineEdit_2.clear()
                self.tela_cadastro.lineEdit.clear()
                self.tela_cadastro.lineEdit_5.clear()
                metodos.exibir()
        else:
            QMessageBox.information(None,'Atenção','Todos os valores devem ser preenchidos!')
    def voltar(self):
        self.Qstack.setCurrentIndex(0)
    def Tela_cad(self):
        self.Qstack.setCurrentIndex(1)
    def Tela_sobre(self):
        self.Qstack.setCurrentIndex(2)
    def sair(self):
        exit()    
if __name__ =='__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
