# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmDepto.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolBar,
    QWidget)
import recursos_rc

class Ui_FrmProd(object):
    def setupUi(self, FrmDepto):
        if not FrmDepto.objectName():
            FrmDepto.setObjectName(u"FrmDepto")
        FrmDepto.resize(571, 441)
        self.actionConex_o = QAction(FrmDepto)
        self.actionConex_o.setObjectName(u"actionConex_o")
        self.actionSair = QAction(FrmDepto)
        self.actionSair.setObjectName(u"actionSair")
        self.action_Novo = QAction(FrmDepto)
        self.action_Novo.setObjectName(u"action_Novo")
        icon = QIcon()
        icon.addFile(u":/depto/Add.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Novo.setIcon(icon)
        self.action_Editar = QAction(FrmDepto)
        self.action_Editar.setObjectName(u"action_Editar")
        icon1 = QIcon()
        icon1.addFile(u":/depto/WINNEXT.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Editar.setIcon(icon1)
        self.action_Salvar = QAction(FrmDepto)
        self.action_Salvar.setObjectName(u"action_Salvar")
        icon2 = QIcon()
        icon2.addFile(u":/depto/Save.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Salvar.setIcon(icon2)
        self.action_Excluir = QAction(FrmDepto)
        self.action_Excluir.setObjectName(u"action_Excluir")
        icon3 = QIcon()
        icon3.addFile(u":/depto/Minus.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Excluir.setIcon(icon3)
        self.action_Cancelar = QAction(FrmDepto)
        self.action_Cancelar.setObjectName(u"action_Cancelar")
        icon4 = QIcon()
        icon4.addFile(u":/depto/UNDO.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Cancelar.setIcon(icon4)
        self.action_Buscar = QAction(FrmDepto)
        self.action_Buscar.setObjectName(u"action_Buscar")
        icon5 = QIcon()
        icon5.addFile(u":/depto/Oeil2.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Buscar.setIcon(icon5)
        self.action_Inicio = QAction(FrmDepto)
        self.action_Inicio.setObjectName(u"action_Inicio")
        icon6 = QIcon()
        icon6.addFile(u":/depto/first.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Inicio.setIcon(icon6)
        self.action_Anterior = QAction(FrmDepto)
        self.action_Anterior.setObjectName(u"action_Anterior")
        icon7 = QIcon()
        icon7.addFile(u":/depto/prior.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Anterior.setIcon(icon7)
        self.action_Proximo = QAction(FrmDepto)
        self.action_Proximo.setObjectName(u"action_Proximo")
        icon8 = QIcon()
        icon8.addFile(u":/depto/next.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Proximo.setIcon(icon8)
        self.action_Fim = QAction(FrmDepto)
        self.action_Fim.setObjectName(u"action_Fim")
        icon9 = QIcon()
        icon9.addFile(u":/depto/last.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Fim.setIcon(icon9)
        self.action_Sair = QAction(FrmDepto)
        self.action_Sair.setObjectName(u"action_Sair")
        icon10 = QIcon()
        icon10.addFile(u":/depto/CLOSE1.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Sair.setIcon(icon10)
        self.centralwidget = QWidget(FrmDepto)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Abas = QTabWidget(self.centralwidget)
        self.Abas.setObjectName(u"Abas")
        self.Abas.setGeometry(QRect(10, 0, 501, 331))
        font = QFont()
        font.setPointSize(11)
        self.Abas.setFont(font)
        self.tabCadastro = QWidget()
        self.tabCadastro.setObjectName(u"tabCadastro")
        self.layoutWidget = QWidget(self.tabCadastro)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 371, 270))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.spbValor = QSpinBox(self.layoutWidget)
        self.spbValor.setObjectName(u"spbValor")

        self.gridLayout.addWidget(self.spbValor, 4, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.edNomeProd = QLineEdit(self.layoutWidget)
        self.edNomeProd.setObjectName(u"edNomeProd")
        self.edNomeProd.setMaxLength(20)

        self.gridLayout.addWidget(self.edNomeProd, 1, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.descricaoProd = QTextEdit(self.layoutWidget)
        self.descricaoProd.setObjectName(u"descricaoProd")

        self.gridLayout.addWidget(self.descricaoProd, 3, 1, 1, 1)

        self.spbCategoria = QSpinBox(self.layoutWidget)
        self.spbCategoria.setObjectName(u"spbCategoria")

        self.gridLayout.addWidget(self.spbCategoria, 5, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.imagem = QLineEdit(self.layoutWidget)
        self.imagem.setObjectName(u"imagem")

        self.gridLayout.addWidget(self.imagem, 2, 1, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.spbNumProd = QSpinBox(self.layoutWidget)
        self.spbNumProd.setObjectName(u"spbNumProd")

        self.gridLayout.addWidget(self.spbNumProd, 0, 1, 1, 1)

        icon11 = QIcon()
        icon11.addFile(u":/depto/COPY.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.Abas.addTab(self.tabCadastro, icon11, "")
        self.tabListagem = QWidget()
        self.tabListagem.setObjectName(u"tabListagem")
        self.gridDepto = QTableWidget(self.tabListagem)
        if (self.gridDepto.columnCount() < 5):
            self.gridDepto.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.gridDepto.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.gridDepto.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.gridDepto.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.gridDepto.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.gridDepto.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.gridDepto.setObjectName(u"gridDepto")
        self.gridDepto.setGeometry(QRect(0, 0, 481, 261))
        icon12 = QIcon()
        icon12.addFile(u":/depto/WINPREV.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.Abas.addTab(self.tabListagem, icon12, "")
        FrmDepto.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FrmDepto)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 571, 21))
        self.menuCadastro = QMenu(self.menubar)
        self.menuCadastro.setObjectName(u"menuCadastro")
        self.menuListagem = QMenu(self.menubar)
        self.menuListagem.setObjectName(u"menuListagem")
        self.menuSobre = QMenu(self.menubar)
        self.menuSobre.setObjectName(u"menuSobre")
        self.menuSair = QMenu(self.menubar)
        self.menuSair.setObjectName(u"menuSair")
        FrmDepto.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FrmDepto)
        self.statusbar.setObjectName(u"statusbar")
        FrmDepto.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(FrmDepto)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        FrmDepto.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuListagem.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        self.menubar.addAction(self.menuSair.menuAction())
        self.menuCadastro.addAction(self.actionConex_o)
        self.menuCadastro.addSeparator()
        self.menuCadastro.addAction(self.actionSair)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Novo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Editar)
        self.toolBar.addAction(self.action_Salvar)
        self.toolBar.addAction(self.action_Excluir)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Sair)

        self.retranslateUi(FrmDepto)

        self.Abas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FrmDepto)
    # setupUi

    def retranslateUi(self, FrmDepto):
        FrmDepto.setWindowTitle(QCoreApplication.translate("FrmDepto", u"Cadastro de Departamentos", None))
        self.actionConex_o.setText(QCoreApplication.translate("FrmDepto", u"Conex\u00e3o", None))
        self.actionSair.setText(QCoreApplication.translate("FrmDepto", u"Sair", None))
        self.action_Novo.setText(QCoreApplication.translate("FrmDepto", u"&Novo", None))
#if QT_CONFIG(tooltip)
        self.action_Novo.setToolTip(QCoreApplication.translate("FrmDepto", u"Incluir novo registro", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Novo.setShortcut(QCoreApplication.translate("FrmDepto", u"Ctrl++", None))
#endif // QT_CONFIG(shortcut)
        self.action_Editar.setText(QCoreApplication.translate("FrmDepto", u"&Editar", None))
#if QT_CONFIG(tooltip)
        self.action_Editar.setToolTip(QCoreApplication.translate("FrmDepto", u"Altera dados do registro em exibi\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.action_Salvar.setText(QCoreApplication.translate("FrmDepto", u"&Salvar", None))
#if QT_CONFIG(tooltip)
        self.action_Salvar.setToolTip(QCoreApplication.translate("FrmDepto", u"Grava o registro atual no banco de dados", None))
#endif // QT_CONFIG(tooltip)
        self.action_Excluir.setText(QCoreApplication.translate("FrmDepto", u"E&xcluir", None))
#if QT_CONFIG(tooltip)
        self.action_Excluir.setToolTip(QCoreApplication.translate("FrmDepto", u"Exclui o registro cujo c\u00f3digo foi digitado", None))
#endif // QT_CONFIG(tooltip)
        self.action_Cancelar.setText(QCoreApplication.translate("FrmDepto", u"&Cancelar", None))
#if QT_CONFIG(tooltip)
        self.action_Cancelar.setToolTip(QCoreApplication.translate("FrmDepto", u"Cancela a opera\u00e7\u00e3o atualmente em execu\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.action_Buscar.setText(QCoreApplication.translate("FrmDepto", u"&Buscar", None))
#if QT_CONFIG(tooltip)
        self.action_Buscar.setToolTip(QCoreApplication.translate("FrmDepto", u"Busca o registro cujo c\u00f3digo foi digitado e o exibe", None))
#endif // QT_CONFIG(tooltip)
        self.action_Inicio.setText(QCoreApplication.translate("FrmDepto", u"&In\u00edcio", None))
#if QT_CONFIG(tooltip)
        self.action_Inicio.setToolTip(QCoreApplication.translate("FrmDepto", u"Posiciona visualiza\u00e7\u00e3o no primeiro registro e o exibe", None))
#endif // QT_CONFIG(tooltip)
        self.action_Anterior.setText(QCoreApplication.translate("FrmDepto", u"&Anterior", None))
#if QT_CONFIG(tooltip)
        self.action_Anterior.setToolTip(QCoreApplication.translate("FrmDepto", u"Posiciona visualiza\u00e7\u00e3o no registro anterior ao atualmente exibido", None))
#endif // QT_CONFIG(tooltip)
        self.action_Proximo.setText(QCoreApplication.translate("FrmDepto", u"&Pr\u00f3ximo", None))
#if QT_CONFIG(tooltip)
        self.action_Proximo.setToolTip(QCoreApplication.translate("FrmDepto", u"Posiciona visualiza\u00e7\u00e3o no registro seguinte ao atual", None))
#endif // QT_CONFIG(tooltip)
        self.action_Fim.setText(QCoreApplication.translate("FrmDepto", u"&Fim", None))
#if QT_CONFIG(tooltip)
        self.action_Fim.setToolTip(QCoreApplication.translate("FrmDepto", u"Posiciona visualiza\u00e7\u00e3o no \u00faltimo registro e o exibe", None))
#endif // QT_CONFIG(tooltip)
        self.action_Sair.setText(QCoreApplication.translate("FrmDepto", u"Sai&r", None))
#if QT_CONFIG(tooltip)
        self.action_Sair.setToolTip(QCoreApplication.translate("FrmDepto", u"Fecha a conex\u00e3o, salva dados e fecha o formul\u00e1rio", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("FrmDepto", u"Nome do produto:", None))
        self.label_3.setText(QCoreApplication.translate("FrmDepto", u"Descri\u00e7\u00e3o do produto", None))
        self.label_4.setText(QCoreApplication.translate("FrmDepto", u"Valor do produto", None))
        self.label_5.setText(QCoreApplication.translate("FrmDepto", u"Categoria", None))
        self.label_6.setText(QCoreApplication.translate("FrmDepto", u"Imagem(SemAcento)", None))
        self.imagem.setText(QCoreApplication.translate("FrmDepto", u".png", None))
        self.label.setText(QCoreApplication.translate("FrmDepto", u"Numero do produto", None))
        self.Abas.setTabText(self.Abas.indexOf(self.tabCadastro), QCoreApplication.translate("FrmDepto", u"Cadastro", None))
#if QT_CONFIG(tooltip)
        self.Abas.setTabToolTip(self.Abas.indexOf(self.tabCadastro), QCoreApplication.translate("FrmDepto", u"Manuten\u00e7\u00e3o de Dados de Departamento", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.gridDepto.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FrmDepto", u"Num. Prod", None));
        ___qtablewidgetitem1 = self.gridDepto.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FrmDepto", u"Nome", None));
        ___qtablewidgetitem2 = self.gridDepto.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FrmDepto", u"Valor", None));
        ___qtablewidgetitem3 = self.gridDepto.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FrmDepto", u"Categoria", None));
        ___qtablewidgetitem4 = self.gridDepto.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FrmDepto", u"Descri\u00e7\u00e3o", None));
        self.Abas.setTabText(self.Abas.indexOf(self.tabListagem), QCoreApplication.translate("FrmDepto", u"Listagem", None))
#if QT_CONFIG(tooltip)
        self.Abas.setTabToolTip(self.Abas.indexOf(self.tabListagem), QCoreApplication.translate("FrmDepto", u"Exibe lista de departamentos cadastrados", None))
#endif // QT_CONFIG(tooltip)
        self.menuCadastro.setTitle(QCoreApplication.translate("FrmDepto", u"Cadastro", None))
        self.menuListagem.setTitle(QCoreApplication.translate("FrmDepto", u"Listagem", None))
        self.menuSobre.setTitle(QCoreApplication.translate("FrmDepto", u"Sobre", None))
        self.menuSair.setTitle(QCoreApplication.translate("FrmDepto", u"Sair", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("FrmDepto", u"toolBar", None))
    # retranslateUi

