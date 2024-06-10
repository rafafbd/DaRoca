import sys
from PySide6.QtCore import QtMsgType
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QDialog, QTableWidgetItem
from FrmProduto_ui import Ui_FrmProd
from FrmConexao_ui import Ui_dlgConectar
import pyodbc as bd
from datetime import datetime

global conexao, meuCursor

class FormPrincipal(QMainWindow, Ui_FrmProd):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.show()
        self.situacao = "navegando"
        self.action_Sair.triggered.connect(self.sairDoPrograma)
        self.action_Novo.triggered.connect(self.novoRegistro)
        self.action_Editar.triggered.connect(self.editarRegistro)
        self.action_Salvar.triggered.connect(self.salvarRegistro)



    def novoRegistro(self):
        self.spbNumProd.setValue(0) # reseta o valor da spinbox chamada spxNumProd
        self.edNomeProd.setText("") # o mesmo
        self.situacao = "incluindo"
        self.spbNumProd.setFocus()
        self.statusBar.showMessage("Digite os dados acima")

    def editarRegistro(self):
        self.situacao = "editando"
        self.edNomeProd.setFocus()
        self.spbNumProd.setReadOnly(True)
        self.statusBar.showMessage("Altere os dados acima")

    def salvarRegistro(self):
        if self.situacao == "incluindo":
            sComando = "Insert into daroca.produtos "+\
            " (nome, imagem, valor, descricao, categoria) "+\
            " values (?, ?, ?, ?, ?) "
            try: # tente executar o comando abaixo:
                meuCursor.execute(sComando, 
                self.edNomeProd.text(), 
                self.imagem.text(),
                float(self.spbValor.value()),
                self.descricaoProd.text(),
                int(self.spbCategoria.value())
                )
                meuCursor.commit() # enviar as mudanças para o BD
                self.statusBar.showMessage("Inserido") 
            except Exception as erro: # em caso de erro
                if hasattr(erro, 'message'):
                    mensagem = erro.message
                else:
                    mensagem = erro.args[1]
                self.statusBar.showMessage(mensagem)
        elif self.situacao =="editando":
            sComando = "Update Empresa.Departamento "+\
            " set nome = ?, imagem = ?, "+\
            " valor = ?, descricao = ?, categoria = ? "+\
            " where id = ? "
            try: # tente executar o comando abaixo:
                meuCursor.execute(sComando, 
                self.edNomeProd.text(), 
                self.imagem.text(),
                float(self.spbValor.value()),
                self.descricaoProd.text(),
                int(self.spbCategoria.value()),
                int(self.spbNumProd.value())
                )
            except Exception as erro: # em caso de erro
                if hasattr(erro, 'message'):
                    mensagem = erro.message
                else:
                    mensagem = erro.args[1]
                self.statusBar.showMessage(mensagem)
        self.situacao = "navegando"
            
    def excluirRegistro(self):
        self.situacao = "excluindo"
        sComando = "Delete from daroca.produtos "+\
        " where numProd = ? "
        try: # tente executar o comando abaixo:
            meuCursor.execute(sComando, self.spbNumProd.value())
            meuCursor.commit() # enviar as mudanças para o BD
            self.statusBar.showMessage("Excluído") 
        except Exception as erro: # em caso de erro
            if hasattr(erro, 'message'):
                mensagem = erro.message
            else:
                mensagem = erro.args[1]
            self.statusBar.showMessage(mensagem)
        self.situacao = "navegando"

    def mudarTab(self):
        if self.Abas.currentIndex() == 1: # busca no BD os registros 
            try: 
                scomando = "SELECT D.numProd, NOMEProd, "+\
                " GERENTE_NUMSEGSOCIAL, "+\
                " PreNome+' '+InicialMeio+' '+Sobrenome as Nome, "+\
                " GERENTE_DATAINICIAL "+\
                " FROM EMPRESA.DEPARTAMENTO D, Empresa.Empregado E"+\
                " WHERE D.Gerente_numSegSocial = E.numSegSocial "+\
                " ORDER BY NomeProd"
                result = meuCursor.execute(scomando)
                regs = result.fetchall()
                numeroDeLinhas = len(regs)
                self.gridProd.setRowCount(numeroDeLinhas)
                for indice in range(0, numeroDeLinhas, 1):
                    item_numProd = QTableWidgetItem(regs[indice][0])
                    item_nomeProd = QTableWidgetItem(regs[indice][1])
                    item_numGerente = QTableWidgetItem(regs[indice][2])
                    item_nomeGerente = QTableWidgetItem(regs[indice][3])
                    item_dataGerente = QTableWidgetItem(regs[indice][4])
                    self.gridProd.setItem(indice, 0, item_numProd)
                    self.gridProd.setItem(indice, 1, item_nomeProd)
                    self.gridProd.setItem(indice, 2, item_numGerente)
                    self.gridProd.setItem(indice, 3, item_nomeGerente)
                    self.gridProd.setItem(indice, 4, item_dataGerente)
                self.gridProd.resizeColumnsToContents()
                self.gridProd.resizeRowsToContents()
                self.statusBar.showMessage("Listagem")
            except Exception as erro: # em caso de erro
                if hasattr(erro, 'message'):
                    mensagem = erro.message
                else:
                    mensagem = erro.args[1]
                self.statusBar.showMessage(mensagem)

    def sairDoPrograma(self):
        self.close()



class DialogoConexao(QDialog, Ui_dlgConectar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)

aplicacao = QApplication(sys.argv)

dlgCon = DialogoConexao()

if dlgCon.exec() == QDialog.Accepted:

    try:
        conexao = bd.connect(driver="SQL Server",
                            server=f"{dlgCon.edServidor.text()}",
                            database=f"{dlgCon.edBancoDeDados.text()}",
                            uid=f"{dlgCon.edUsuario.text()}",
                            pwd=f"{dlgCon.edSenha.text()}") 
        print("Conexão bem sucedida!")
        meuCursor = conexao.cursor() # cursor: objeto de acesso ao BD
        janela = FormPrincipal() 
        aplicacao.exec()
    except:
        print("Não foi possível conectar ao banco de dados")




