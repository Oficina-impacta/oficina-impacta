import sys
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtCore import QSize, Qt
from PySide6 import QtCore
from PySide6.QtWidgets import *
from database import Data_base
# import pandas as pd
import pycep_correios
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QCheckBox




class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        # widgets de entrada de nome de usuário e senha
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # botão de login
        self.login_button = QPushButton("Login")

        # layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nome de usuário:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Senha:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        # conectar o botão de login à verificação de login
        self.login_button.clicked.connect(self.check_login)

        # variável para controlar o número de tentativas
        self.num_tentativas = 0

    def check_login(self):
        # verifique se o nome de usuário e a senha estão corretos
        username = self.username_input.text()
        password = self.password_input.text()
        if username == "admin" and password == "admin":
            # fecha a tela de login e abre a janela principal
            self.done(QDialog.Accepted)
        else:
            self.num_tentativas += 1
            if self.num_tentativas >= 3:
                self.reject()
            else:
                QMessageBox.warning(self, "Login incorreto", "Nome de usuário ou senha incorretos. Tente novamente.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

     # cria a tela de login
        self.login_window = LoginWindow()
        result = self.login_window.exec()
        if result == QDialog.Accepted:
            # abre a janela principal
            self.show()
        else:
            # encerra o programa
            sys.exit()

        self.w_cliente = clienteWindow()
        self.w_cadastro_cliente = cadastroClienteWindow()
        self.w_produtos = produtoWindow()
        self.w_cadastro_produto = cadastroProdutoWindow()
        self.w_veiculo = veiculoWindow()
        self.w_cadastro_veiculo = cadastroVeiculoWindow()
        self.w_servico = servicosWindow()
        
        self.setWindowTitle("Oficina Impacta")
        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap("imp.png"))
        self.lbl.setAlignment(Qt.AlignCenter)

        self.db = Data_base()

        toolbar = QToolBar('Minha toolbar')
        self.addToolBar(toolbar)

        self.setStatusBar(QStatusBar(self))

        self.button_cliente = QAction('Clientes')
        self.button_cliente.setStatusTip('Cadastro de clientes')
        self.button_cadastrar_cliente = QAction('Cadastrar clientes')
        self.button_cadastrar_cliente.setStatusTip('Cadastro de clientes')
        self.button_produtos = QAction('Produtos e Serviços')
        self.button_produtos.setStatusTip('Produtos e Serviços cadastrados')
        self.button_cadastro_produto = QAction('Cadastrar produtos e serviços')
        self.button_cadastro_produto.setStatusTip('Cadastrar produtos e serviços')
        self.button_veiculos = QAction('Veículos')
        self.button_veiculos.setStatusTip('Cadastro de veículos')
        self.button_cadastrar_veiculos = QAction('Cadastrar Veículos')
        self.button_cadastrar_veiculos.setStatusTip('Cadastro de Veículos')
        self.button_servico_aberto = QAction('Serviços em Aberto')
        self.button_servico_aberto.setStatusTip('Serviços em Aberto')
        self.button_historico_vendas = QAction('Historico de Vendas')
        self.button_historico_vendas.setStatusTip('Historico de Vendas')

        toolbar.addAction(self.button_cliente)
        toolbar.addAction(self.button_produtos)
        toolbar.addAction(self.button_veiculos)
        toolbar.addAction(self.button_servico_aberto) 
        toolbar.addAction(self.button_historico_vendas)
        
        menu = self.menuBar()
        menu_arquivo = menu.addMenu('Cadastro')
        menu_arquivo.addAction(self.button_cadastrar_cliente)
        menu_arquivo.addAction(self.button_produtos)
        menu_arquivo.addAction(self.button_veiculos)
        menu_arquivo = menu.addMenu('Serviço')
        menu_arquivo.addAction(self.button_servico_aberto)
        menu_arquivo = menu.addMenu('Histórico')
        menu_arquivo.addAction(self.button_historico_vendas)

        self.button_cliente.triggered.connect(self.show_clienteWindow)
        self.button_cadastrar_cliente.triggered.connect(self.show_cadastroCliente)
        
        self.button_produtos.triggered.connect(self.show_produtosWindow)
        self.button_cadastro_produto.triggered.connect(self.show_cadastroProduto)

        self.button_veiculos.triggered.connect(self.show_veiculosWindow)
        self.button_cadastrar_veiculos.triggered.connect(self.show_cadastro_veiculo)

        self.button_servico_aberto.triggered.connect(self.show_servicosWindow)
        

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
    
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.setFixedSize(QSize(1000,800))

    def show_clienteWindow(self):
        if  self.w_cliente.isVisible():
            self.w_cliente.hide()
        else:
            self.w_cliente.show()

    def show_cadastroCliente(self):
        if  self.w_cadastro_cliente.isVisible():
            self.w_cadastro_cliente.hide()
        else:
            self.w_cadastro_cliente.show()

    def show_produtosWindow(self):
        if  self.w_produtos.isVisible():
            self.w_produtos.hide()
        else:
            self.w_produtos.show()
    
    def show_cadastroProduto(self):
        if  self.w_cadastro_produto.isVisible():
            self.w_cadastro_produto.hide()
        else:
            self.w_cadastro_produto.show()

    def show_veiculosWindow(self):
        if  self.w_veiculo.isVisible():
            self.w_veiculo.hide()
        else:
            self.w_veiculo.show()

    def show_cadastro_veiculo(self):
        if  self.w_cadastro_veiculo.isVisible():
            self.w_cadastro_veiculo.hide()
        else:
            self.w_cadastro_veiculo.show()

    def show_servicosWindow(self):
        if  self.w_servico.isVisible():
            self.w_servico.hide()
        else:
            self.w_servico.show()       

class clienteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w_scadastro_cliente = cadastroClienteWindow()

        self.setWindowTitle("Clientes cadastrados")

        toolbar = QToolBar('toolbar')
        self.addToolBar(toolbar)

        self.setStatusBar(QStatusBar(self))

        self.bt_cadastrarCliente = QAction('Cadastrar cliente')
        self.bt_att_tb_cliente = QAction('Atualizar Tabela')
        self.bt_alt_dados = QAction('Alterar Dados')
        self.bt_del_dados = QAction('Deletar cadastro')

        self.tb_clientes = QTableWidget()
        self.tb_clientes.setColumnCount(9)
        self.tb_clientes.setHorizontalHeaderLabels(['Nome', 'Cpf', 'Telefone', 'CEP', 'Logradouro', 'Numero', 'Complemento', 'Bairro', 'Cidade'])

        self.db = Data_base()
        self.buscar_clientes()

        self.bt_cadastrarCliente.triggered.connect(self.show_cadastroClientes)
        self.bt_att_tb_cliente.triggered.connect(self.buscar_clientes)
        self.bt_alt_dados.triggered.connect(self.alterar_clientes)
        self.bt_del_dados.triggered.connect(self.deletar_clientes)
        
        toolbar.addAction(self.bt_cadastrarCliente)
        toolbar.addAction(self.bt_att_tb_cliente)
        toolbar.addAction(self.bt_alt_dados)
        toolbar.addAction(self.bt_del_dados)

        layout = QVBoxLayout()
        layout.addWidget(self.tb_clientes)
        
        container = QWidget()
        container.setLayout(layout)


        self.setCentralWidget(container)
        self.setFixedSize(QSize(950,800))

    def buscar_clientes(self):
        result = self.db.select_all_clientes()
        self.tb_clientes.clearContents()
        self.tb_clientes.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_clientes.setItem(row, column, QTableWidgetItem(str(data)))

    def msg(self, tipo, mensage):
        msgbox = QMessageBox()

        if tipo.lower() == 'ok':
            msgbox.setIcon(QMessageBox.Information)
        elif tipo.lower() == 'ERRO':
            msgbox.setIcon(QMessageBox.Critical)
        elif tipo.lower() == 'aviso':
            msgbox.setIcon(QMessageBox.Warning)
        
        msgbox.setText(mensage)
        msgbox.exec()
    
    def show_cadastroClientes(self):
        if  self.w_scadastro_cliente.isVisible():
            self.w_scadastro_cliente.hide()
        else:
            self.w_scadastro_cliente.show()
            
    def deletar_clientes(self):
        if not self.tb_clientes.selectedIndexes():
          QMessageBox.warning(self, "Erro", "Nenhum registro selecionado!")
          return
        msg = QMessageBox()
        msg.setWindowTitle('Excluir')
        msg.setText('Este registro será excluído.')
        msg.setInformativeText('Você tem certeza que deseja continuar?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cpf = self.tb_clientes.selectionModel().currentIndex().siblingAtColumn(1).data()
            print(cpf)
            result = self.db.delete_clientes(cpf)
            self.buscar_clientes()

            self.msg(result[0], result[1])
        else:
            self.msg('erro', 'Exclusão cancelada pelo usuário.')

    def alterar_clientes(self):
    # Obtém o índice da linha selecionada na tabela
      row = self.tb_clientes.currentRow()

      if row == -1:
        QMessageBox.warning(self, 'Erro', 'Por favor, selecione um cliente para alterar.')
        return

      # Obtém os dados da linha selecionada
      cpf = self.tb_clientes.item(row, 1).text()
      nome = self.tb_clientes.item(row, 0).text()
      telefone = self.tb_clientes.item(row, 2).text()
      cep = self.tb_clientes.item(row, 3).text()
      logradouro = self.tb_clientes.item(row, 4).text()
      numero = self.tb_clientes.item(row, 5).text()
      complemento = self.tb_clientes.item(row, 6).text()
      bairro = self.tb_clientes.item(row, 7).text()
      cidade = self.tb_clientes.item(row, 8).text()

      # Cria a janela de diálogo para alterar os dados
      dialog = QDialog(self)
      dialog.setWindowTitle('Alterar dados do cliente')
      dialog.setModal(True)

      # Adiciona os campos de texto para o usuário preencher os dados
      layout = QFormLayout(dialog)
      txt_nome = QLineEdit(nome)
      txt_telefone = QLineEdit(telefone)
      txt_cep = QLineEdit(cep)
      txt_logradouro = QLineEdit(logradouro)
      txt_numero = QLineEdit(numero)
      txt_complemento = QLineEdit(complemento)
      txt_bairro = QLineEdit(bairro)
      txt_cidade = QLineEdit(cidade)
      layout.addRow('Nome:', txt_nome)
      layout.addRow('Telefone:', txt_telefone)
      layout.addRow('CEP:', txt_cep)
      layout.addRow('Logradouro:', txt_logradouro)
      layout.addRow('Número:', txt_numero)
      layout.addRow('Complemento:', txt_complemento)
      layout.addRow('Bairro:', txt_bairro)
      layout.addRow('Cidade:', txt_cidade)

      # Adiciona os botões OK e Cancelar
      btn_ok = QPushButton('OK')
      btn_cancel = QPushButton('Cancelar')
      btn_ok.clicked.connect(dialog.accept)
      btn_cancel.clicked.connect(dialog.reject)
      btn_layout = QHBoxLayout()
      btn_layout.addWidget(btn_ok)
      btn_layout.addWidget(btn_cancel)
      layout.addRow(btn_layout)

      # Exibe a janela de diálogo e verifica se o usuário clicou em OK
      if dialog.exec() == QDialog.Accepted:
        # Obtém os dados preenchidos pelo usuário
        nome = txt_nome.text()
        telefone = txt_telefone.text()
        cep = txt_cep.text()
        logradouro = txt_logradouro.text()
        numero = txt_numero.text()
        complemento = txt_complemento.text()
        bairro = txt_bairro.text()
        cidade = txt_cidade.text()
        
        
        # Chama a função update_clientes() com os dados do cliente
        result = self.db.update_clientes(nome, telefone, cep, logradouro, numero, complemento, bairro, cidade, cpf)
        # Verifica se a atualização foi bem sucedida
        if result[0] == 'OK':          
            QApplication.processEvents()
            QMessageBox.information(self, 'Sucesso', 'Dados atualizados com sucesso.')
     
class cadastroClienteWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = Data_base()

        self.setWindowTitle("Cadastro de cliente")
        toolbar = QToolBar('toolbar')
        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar(self))

        self.button_salvar = QAction('Salvar cadastro')
        self.button_salvar.setStatusTip('Salvar cadastro de clientes')

        toolbar.addAction(self.button_salvar)

        self.button_salvar.triggered.connect(self.cadastrar_cliente_bd)

        self.lbl_nome = QLabel('Nome: ')
        self.txt_nome = QLineEdit()
        self.txt_nome.setMaxLength(50)

        self.lbl_cpf = QLabel('CPF: ')
        self.txt_cpf = QLineEdit()
        self.txt_cpf.setInputMask("000.000.000-00;_")

        self.lbl_telefone = QLabel('Telefone: ')
        self.txt_telefone = QLineEdit()
        self.txt_telefone.setInputMask("(00) 00000-0000;_")
        
        self.lbl_inf_cep = QLabel('Informe o CEP: ')
        self.txt_inf_cep = QLineEdit()
        self.txt_inf_cep.setInputMask("00000-000;_")

        self.lbl_logradouro = QLabel('Logradouro: ')
        self.txt_logradouro = QLineEdit()

        self.lbl_numero_res = QLabel('Número: ')
        self.txt_numero_res = QLineEdit()

        self.lbl_complemento = QLabel('Complemento: ')
        self.txt_complemento = QLineEdit()

        self.lbl_bairro = QLabel('Bairro: ')
        self.txt_bairro = QLineEdit()

        self.lbl_cidade = QLabel('Cidade: ')
        self.txt_cidade = QLineEdit()


        layout = QVBoxLayout()
        layout.addWidget(self.lbl_nome)
        layout.addWidget(self.txt_nome)
        layout.addWidget(self.lbl_cpf)
        layout.addWidget(self.txt_cpf)
        layout.addWidget(self.lbl_telefone)
        layout.addWidget(self.txt_telefone)
        layout.addWidget(self.lbl_inf_cep)
        layout.addWidget(self.txt_inf_cep)
        layout.addWidget(self.lbl_logradouro)
        layout.addWidget(self.txt_logradouro)
        layout.addWidget(self.lbl_numero_res)
        layout.addWidget(self.txt_numero_res)
        layout.addWidget(self.lbl_complemento)
        layout.addWidget(self.txt_complemento)
        layout.addWidget(self.lbl_bairro)
        layout.addWidget(self.txt_bairro)
        layout.addWidget(self.lbl_cidade)
        layout.addWidget(self.txt_cidade)

        container = QWidget()
        container.setLayout(layout)


        self.setCentralWidget(container)
        self.setFixedSize(QSize(800,800))

        
        self.txt_inf_cep.editingFinished.connect(self.buscar_cep)

    def buscar_cep(self):
        endereco = pycep_correios.get_address_from_cep(self.txt_inf_cep.text())
        self.txt_logradouro.setText(endereco['logradouro'])
        self.txt_bairro.setText(endereco['bairro'])
        self.txt_cidade.setText(endereco['cidade'])
        pass

    def cadastrar_cliente_bd(self):
        
        fullDataSet = (
            self.txt_nome.text(), self.txt_cpf.text(), self.txt_telefone.text(), self.txt_inf_cep.text(), self.txt_logradouro.text(),
            self.txt_numero_res.text(), self.txt_complemento.text(), self.txt_bairro.text(),
            self.txt_cidade.text(),
        )
        # cadastrar no banco
        resp = self.db.registro_clientes(fullDataSet)
        # exibir mensagem de sucesso ou erro
        self.msg(resp[0], resp[1])
         # Limpar campos de entrada de dados
        self.txt_nome.setText('')
        self.txt_cpf.setText('')
        self.txt_telefone.setText('')
        self.txt_inf_cep.setText('')
        self.txt_logradouro.setText('')
        self.txt_numero_res.setText('')
        self.txt_complemento.setText('')
        self.txt_bairro.setText('')
        self.txt_cidade.setText('')
        

    def msg(self, tipo, mensage):
        msgbox = QMessageBox()
        if tipo.lower() == 'ok':
            msgbox.setIcon(QMessageBox.Information)
        elif tipo.lower() == 'ERRO':
            msgbox.setIcon(QMessageBox.Critical)
        elif tipo.lower() == 'aviso':
            msgbox.setIcon(QMessageBox.Warning)
        
        msgbox.setText(mensage)
        msgbox.exec()

class produtoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w_cadastro_produto = cadastroProdutoWindow()

        self.setWindowTitle("Produtos cadastrados")

        toolbar = QToolBar('toolbar')
        self.addToolBar(toolbar)

        self.setStatusBar(QStatusBar(self))

        self.bt_cadastrarProduto = QAction('Cadastrar produto ou serviço')
        self.bt_att_tb_Produto = QAction('Atualizar Tabela')
        self.bt_alt_dados = QAction('Alterar Dados')
        self.bt_del_dados = QAction('Deletar Produto ou serviço')

        self.tb_Produtos = QTableWidget()
        self.tb_Produtos.setColumnCount(4)
        self.tb_Produtos.setHorizontalHeaderLabels(['COD', 'NOME', 'TIPO', 'PRECO'])

        self.db = Data_base()
        self.buscar_produtos()

        self.bt_cadastrarProduto.triggered.connect(self.show_cadastroProduto)
        self.bt_att_tb_Produto.triggered.connect(self.buscar_produtos)
        self.bt_alt_dados.triggered.connect(self.alterar_produtos)
        self.bt_del_dados.triggered.connect(self.deletar_produtos)
        
        toolbar.addAction(self.bt_cadastrarProduto)
        toolbar.addAction(self.bt_att_tb_Produto)
        toolbar.addAction(self.bt_alt_dados)
        toolbar.addAction(self.bt_del_dados)

        layout = QVBoxLayout()
        layout.addWidget(self.tb_Produtos)
        
        container = QWidget()
        container.setLayout(layout)


        self.setCentralWidget(container)
        self.setFixedSize(QSize(950,800))

    def msg(self, tipo, mensage):
        msgbox = QMessageBox()

        if tipo.lower() == 'ok':
            msgbox.setIcon(QMessageBox.Information)
        elif tipo.lower() == 'ERRO':
            msgbox.setIcon(QMessageBox.Critical)
        elif tipo.lower() == 'aviso':
            msgbox.setIcon(QMessageBox.Warning)
        
        msgbox.setText(mensage)
        msgbox.exec()

    def show_cadastroProduto(self):
        if  self.w_cadastro_produto.isVisible():
            self.w_cadastro_produto.hide()
        else:
            self.w_cadastro_produto.show()
    
    def buscar_produtos(self):
        result = self.db.select_all_produtos()
        self.tb_Produtos.clearContents()
        self.tb_Produtos.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_Produtos.setItem(row, column, QTableWidgetItem(str(data)))


    def deletar_produtos(self):
        if not self.tb_Produtos.selectedIndexes():
          QMessageBox.warning(self, "Erro", "Nenhum registro selecionado!")
          return

        msg = QMessageBox()
        msg.setWindowTitle('Excluir')
        msg.setText('Este registro será excluído.')
        msg.setInformativeText('Você tem certeza que deseja continuar?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cod = self.tb_Produtos.selectionModel().currentIndex().siblingAtColumn(0).data()
            print(cod)
            result = self.db.delete_produtos(cod)
            self.buscar_produtos()

            self.msg(result[0], result[1])            
       
    def alterar_produtos(self):
    # Obtém o índice da linha selecionada na tabela
      row = self.tb_Produtos.currentRow()

      if row == -1:
        QMessageBox.warning(self, 'Erro', 'Por favor, selecione um produto para alterar.')
        return

      # Obtém os dados da linha selecionada
      COD = self.tb_Produtos.item(row, 0).text()
      NOME = self.tb_Produtos.item(row, 1).text()
      TIPO = self.tb_Produtos.item(row, 2).text()
      PRECO = self.tb_Produtos.item(row, 3).text()

      # Cria a janela de diálogo para alterar os dados
      dialog = QDialog(self)
      dialog.setWindowTitle('Alterar produtos')
      dialog.setModal(True)


      # Adiciona os campos de texto para o usuário preencher os dados
      layout = QFormLayout(dialog)
      txt_COD = QLineEdit(str(COD))
      txt_NOME = QLineEdit(NOME)
      txt_TIPO = QLineEdit(TIPO)
      txt_PRECO = QLineEdit(PRECO)
      layout.addRow('COD:', txt_COD)
      layout.addRow('NOME:', txt_NOME)
      layout.addRow('TIPO:', txt_TIPO)
      layout.addRow('PRECO:', txt_PRECO)

      # Adiciona os botões OK e Cancelar
      btn_ok = QPushButton('OK')
      btn_cancel = QPushButton('Cancelar')
      btn_ok.clicked.connect(dialog.accept)
      btn_cancel.clicked.connect(dialog.reject)
      btn_layout = QHBoxLayout()
      btn_layout.addWidget(btn_ok)
      btn_layout.addWidget(btn_cancel)
      layout.addRow(btn_layout)

 # Exibe a janela de diálogo e verifica se o usuário clicou em OK
      if dialog.exec() == QDialog.Accepted:
        # Obtém os dados preenchidos pelo usuário
        COD = txt_COD.text()
        NOME = txt_NOME.text()
        TIPO = txt_TIPO.text()
        PRECO = txt_PRECO.text()
        
        
        # Chama a função update_produtos() com os dados do cliente
        result = self.db.update_produtos(COD, NOME, TIPO, PRECO)
        # Verifica se a atualização foi bem sucedida
        print(result[0])
        if result[0] == 'OK':                      
            QMessageBox.information(self, 'Sucesso', 'Dados atualizados com sucesso.')
        else:
            QMessageBox.warning(self, 'Erro', result[1])
        print(result[1])

class cadastroProdutoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = Data_base()

        self.setWindowTitle("Cadastro de Produtos e Serviços")
        toolbar = QToolBar('toolbar')
        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar(self))

        self.button_salvar = QAction('Salvar cadastro')
        self.button_salvar.setStatusTip('Salvar cadastro de produto ou serviço')

        toolbar.addAction(self.button_salvar)

        self.button_salvar.triggered.connect(self.cadastrar_produto_bd)

        self.lbl_cod = QLabel('Codigo interno: ')
        self.txt_cod = QLineEdit()

        self.lbl_nome_produto = QLabel('Nome do produto ou serviço: ')
        self.txt_nome_produto = QLineEdit()

        self.lbl_tipo = QLabel('tipo: ')
        self.txt_tipo = QLineEdit()
        
        self.lbl_preco = QLabel('Preço de venda: ')
        self.txt_preco = QLineEdit()
        self.txt_preco.setInputMask("R$ 0000,00")

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_cod)
        layout.addWidget(self.txt_cod)
        layout.addWidget(self.lbl_nome_produto)
        layout.addWidget(self.txt_nome_produto)
        layout.addWidget(self.lbl_tipo)
        layout.addWidget(self.txt_tipo)
        layout.addWidget(self.lbl_preco)
        layout.addWidget(self.txt_preco)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.setFixedSize(QSize(600,400))

    def cadastrar_produto_bd(self):
    
        fullDataSet = (self.txt_cod.text(), self.txt_nome_produto.text(), self.txt_tipo.text(), self.txt_preco.text())

        if any(x.strip() == '' for x in fullDataSet):
          self.msg('erro', 'Preencha todos os campos')
          return
    
        # cadastrar no banco
        resp = self.db.registro_produtos(fullDataSet)

        self.msg(resp[0], resp[1])
    
        # Limpa os campos após cadastrar
        self.txt_cod.clear()
        self.txt_nome_produto.clear()
        self.txt_tipo.clear()
        self.txt_preco.clear()

    def msg(self, tipo, mensage):
        msgbox = QMessageBox()
        if tipo.lower() == 'ok':
            msgbox.setIcon(QMessageBox.Information)
        elif tipo.lower() == 'ERRO':
            msgbox.setIcon(QMessageBox.Critical)
        elif tipo.lower() == 'aviso':
            msgbox.setIcon(QMessageBox.Warning)
        
        msgbox.setText(mensage)
        msgbox.exec()

class veiculoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w_cadastro_veiculos = cadastroVeiculoWindow()

        self.setWindowTitle("Cadastro Veículos")

        toolbar = QToolBar('toolbar')
        self.addToolBar(toolbar)

        self.setStatusBar(QStatusBar(self))

        self.bt_cadastrar_veiculos = QAction('Cadastrar Veículos')
        self.bt_att_tb_veiculos = QAction('Atualizar Tabela')
        self.bt_alt_dados = QAction('Alterar Dados')
        self.bt_del_dados = QAction('Deletar cadastro')

        #Definição da quantidade de campos que devem aparecer na interface grafica
        self.tb_veiculos = QTableWidget()
        self.tb_veiculos.setColumnCount(6)
        self.tb_veiculos.setHorizontalHeaderLabels(['Placa', 'Cpf', 'Marca', 'Modelo', 'Cor', 'Ano'])

        self.db = Data_base()
        self.buscar_veiculos()

        self.bt_cadastrar_veiculos.triggered.connect(self.show_cadastro_veiculos)
        self.bt_att_tb_veiculos.triggered.connect(self.buscar_veiculos)
        self.bt_alt_dados.triggered.connect(self.alterar_veiculos)
        self.bt_del_dados.triggered.connect(self.deletar_veiculos)
        
        toolbar.addAction(self.bt_cadastrar_veiculos)
        toolbar.addAction(self.bt_att_tb_veiculos)
        toolbar.addAction(self.bt_alt_dados)
        toolbar.addAction(self.bt_del_dados)

        layout = QVBoxLayout()
        layout.addWidget(self.tb_veiculos)
        
        container = QWidget()
        container.setLayout(layout)


        self.setCentralWidget(container)
        self.setFixedSize(QSize(600,800))

    def msg(self, tipo, mensage):
        msgbox = QMessageBox()
        if tipo.lower() == 'ok':
            msgbox.setIcon(QMessageBox.Information)
        elif tipo.lower() == 'ERRO':
            msgbox.setIcon(QMessageBox.Critical)
        elif tipo.lower() == 'aviso':
            msgbox.setIcon(QMessageBox.Warning)
        
        msgbox.setText(mensage)
        msgbox.exec()


    def show_cadastro_veiculos(self):
        if  self.w_cadastro_veiculos.isVisible():
            self.w_cadastro_veiculos.hide()
        else:
            self.w_cadastro_veiculos.show()

    
    def buscar_veiculos(self):
        result = self.db.select_all_veiculos()
        self.tb_veiculos.clearContents()
        self.tb_veiculos.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_veiculos.setItem(row, column, QTableWidgetItem(str(data)))   

    def deletar_veiculos(self):
        if not self.tb_veiculos.selectedIndexes():
          QMessageBox.warning(self, "Erro", "Nenhum registro selecionado!")
          return

        msg = QMessageBox()
        msg.setWindowTitle('Excluir')
        msg.setText('Este registro será excluído.')
        msg.setInformativeText('Você tem certeza que deseja continuar?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
          placa = self.tb_veiculos.selectionModel().currentIndex().siblingAtColumn(0).data()   
          print(placa)       
          result = self.db.delete_veiculos(placa)
          self.buscar_veiculos()          
          self.msg(result[0], result[1])            

    def alterar_veiculos(self):
      # Obtém o índice da linha selecionada na tabela
      row = self.tb_veiculos.currentRow()

      if row == -1:
        QMessageBox.warning(self, 'Erro', 'Por favor, selecione um produto para alterar.')
        return

      # Obtém os dados da linha selecionada
      placa = self.tb_veiculos.item(row, 0).text()      
      cpf = self.tb_veiculos.item(row, 1).text()
      marca = self.tb_veiculos.item(row, 2).text()
      modelo = self.tb_veiculos.item(row, 3).text()
      cor = self.tb_veiculos.item(row, 4).text()
      ano_item = self.tb_veiculos.item(row, 5)
      ano = ano_item.text() if ano_item is not None else ''

      # Cria a janela de diálogo para alterar os dados
      dialog = QDialog(self)
      dialog.setWindowTitle('Alterar veículos')
      dialog.setModal(True)

      # Adiciona os campos de texto para o usuário preencher os dados
      layout = QFormLayout(dialog)
      txt_placa = QLineEdit(str(placa))      
      txt_placa.setInputMask('AAA-9999')
      txt_cpf = QLineEdit(cpf)      
      txt_marca = QLineEdit(marca)
      txt_modelo = QLineEdit(modelo)
      txt_cor = QLineEdit(cor)
      txt_ano = QLineEdit(ano)
      layout.addRow('Placa:', txt_placa)
      layout.addRow('CPF:', txt_cpf)
      layout.addRow('Marca:', txt_marca)
      layout.addRow('Modelo:', txt_modelo)
      layout.addRow('Cor:', txt_cor)
      layout.addRow('Ano:', txt_ano)

      # Adiciona os botões OK e Cancelar
      btn_ok = QPushButton('OK')
      btn_cancel = QPushButton('Cancelar')
      btn_ok.clicked.connect(dialog.accept)
      btn_cancel.clicked.connect(dialog.reject)
      btn_layout = QHBoxLayout()
      btn_layout.addWidget(btn_ok)
      btn_layout.addWidget(btn_cancel)
      layout.addRow(btn_layout)

    # Exibe a janela de diálogo e verifica se o usuário clicou em OK
      if dialog.exec() == QDialog.Accepted:
          # Obtém os dados preenchidos pelo usuário
          placa = txt_placa.text()
          cpf = txt_cpf.text()
          marca = txt_marca.text()
          modelo = txt_modelo.text()
          cor = txt_cor.text()
          ano = txt_ano.text()     
        
          # Chama a função update_veiculos() com os dados do cliente
          result = self.db.update_veiculos(placa, cpf, marca, modelo, cor, ano)
          # Verifica se a atualização foi bem sucedida
          print(result[0])
          if result[0] == 'OK':                      
            QMessageBox.information(self, 'Sucesso', 'Dados atualizados com sucesso.')
          else:
            QMessageBox.warning(self, 'Erro', result[1])
            print(result[1])

class cadastroVeiculoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = Data_base()

        self.setWindowTitle("Cadastro de veículos")
        toolbar = QToolBar('toolbar')
        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar(self))

        self.button_salvar = QAction('Salvar cadastro')
        self.button_salvar.setStatusTip('Salvar cadastro de veículos')

        toolbar.addAction(self.button_salvar)

        self.button_salvar.triggered.connect(self.cadastrar_veiculos_bd)

        self.lbl_placa = QLabel('Placa: ')
        self.txt_placa = QLineEdit()
        self.txt_placa.setInputMask("AAA-9999;_")

        self.lbl_cpf = QLabel('CPF: ')
        self.txt_cpf = QLineEdit()
        self.txt_cpf.setInputMask("000.000.000-00;_")

        self.lbl_marca = QLabel('Marca: ')
        self.txt_marca = QLineEdit()
        
        self.lbl_modelo = QLabel('Modelo: ')
        self.txt_modelo = QLineEdit()

        self.lbl_cor = QLabel('Cor: ')
        self.txt_cor = QLineEdit()

        self.lbl_ano = QLabel('Ano: ')
        self.txt_ano = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_placa)
        layout.addWidget(self.txt_placa)
        layout.addWidget(self.lbl_cpf)
        layout.addWidget(self.txt_cpf)
        layout.addWidget(self.lbl_marca)
        layout.addWidget(self.txt_marca)
        layout.addWidget(self.lbl_modelo)
        layout.addWidget(self.txt_modelo)
        layout.addWidget(self.lbl_cor)
        layout.addWidget(self.txt_cor)
        layout.addWidget(self.lbl_ano)
        layout.addWidget(self.txt_ano)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.setFixedSize(QSize(500, 800))

    
    #Função para cadastrar os veiculos
    def cadastrar_veiculos_bd(self):        
                          
    # continuar com o cadastro        
        fullDataSet = (
            self.txt_placa.text(), self.txt_cpf.text(), self.txt_marca.text(), self.txt_modelo.text(), self.txt_cor.text(), self.txt_ano.text())
        
        if any(x.strip() == '' for x in fullDataSet):
          self.msg('erro', 'Preencha todos os campos')
          return

        # cadastrar no banco
        resp = self.db.registro_veiculos(fullDataSet)

        # exibir mensagem de sucesso ou erro        
        self.msg(resp[0], resp[1])

        # Limpar campos de entrada de dados
        self.txt_placa.setText('')
        self.txt_cpf.setText('')
        self.txt_marca.setText('')
        self.txt_modelo.setText('')
        self.txt_cor.setText('')
        self.txt_ano.setText('')

    def msg(self, tipo, mensage):
        msgbox = QMessageBox()
        if tipo.lower() == 'ok':
            msgbox.setIcon(QMessageBox.Information)
        elif tipo.lower() == 'ERRO':
            msgbox.setIcon(QMessageBox.Critical)
        elif tipo.lower() == 'aviso':
            msgbox.setIcon(QMessageBox.Warning)
        
        msgbox.setText(mensage)
        msgbox.exec()   

class servicosWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w_cadastroServicoWindow = cadastroServicoWindow()

        self.setWindowTitle("Serviços em Aberto")
        toolbar = QToolBar('toolbar')
        self.addToolBar(toolbar)

        self.bt_Gerar_nova_os = QAction('Gerar nova ordem de serviço')
        self.bt_alt_os = QAction('Alterar ordem de serviço')
        self.bt_del_os = QAction('Deletar ordem de serviço')

        self.bt_Gerar_nova_os.triggered.connect(self.show_cadastroProduto)

        toolbar.addAction(self.bt_Gerar_nova_os)
        toolbar.addAction(self.bt_alt_os)
        toolbar.addAction(self.bt_del_os)

        self.tb_servicos = QTableWidget()
        self.tb_servicos.setColumnCount(5)
        self.tb_servicos.setHorizontalHeaderLabels(['OS', 'Placa', 'Marca', 'Modelo', 'Cliente'])        

        layout = QVBoxLayout()
        layout.addWidget(self.tb_servicos)
    
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.setFixedSize(QSize(520,800))

    def show_cadastroProduto(self):
        if  self.w_cadastroServicoWindow.isVisible():
            self.w_cadastroServicoWindow.hide()
        else:
            self.w_cadastroServicoWindow.show()
        
class cadastroServicoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = Data_base()

        self.setWindowTitle("Criar ordem de serviço")
        toolbar = QToolBar('toolbar')
        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar(self))

        self.bt_buscar = QAction('Buscar cadastro')
        self.bt_buscar.setStatusTip('Buscar cadastro de clientes')
        self.bt_buscar.triggered.connect(self.buscar_placa)
        self.bt_buscar.triggered.connect(self.buscar_cpf)

        toolbar.addAction(self.bt_buscar)

        self.lbl_cpf = QLabel('CPF: ')
        self.txt_cpf = QLineEdit()
        self.txt_cpf.setInputMask("000.000.000-00;_")
        self.txt_cpf.setFixedWidth(100)

        self.lbl_placa = QLabel('Placa: ')
        self.txt_placa = QLineEdit()
        self.txt_placa.setInputMask('AAA-9999')
        self.txt_placa.setFixedWidth(100)
        

        self.tb_veiculos = QTableWidget()
        self.tb_veiculos.setColumnCount(6)
        self.tb_veiculos.setHorizontalHeaderLabels(['Placa', 'Cpf', 'Marca', 'Modelo', 'Cor', 'Ano'])
        # bloquear a edição dos campos da tabela
        self.tb_veiculos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        


        self.tb_produtos = QTableWidget()
        self.tb_produtos.setColumnCount(4)
        self.tb_produtos.setHorizontalHeaderLabels(['COD', 'NOME', 'TIPO', 'PRECO'])

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_placa)
        layout.addWidget(self.txt_placa)        
        layout.addWidget(self.lbl_cpf)
        layout.addWidget(self.txt_cpf)
        layout.addWidget(self.tb_veiculos)
        layout.addWidget(self.tb_produtos)

        container = QWidget()
        container.setLayout(layout)

        self.db = Data_base()
        self.buscar_produtos()
     
    
        self.setCentralWidget(container)
        self.setFixedSize(QSize(1000,1000))

    def buscar_produtos(self):
        result = self.db.select_all_produtos()
        self.tb_produtos.clearContents()
        self.tb_produtos.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_produtos.setItem(row, column, QTableWidgetItem(str(data)))

    

    def buscar_placa(self):
        placa = self.txt_placa.text().upper()
        if placa:
            veiculo = self.db.select_veiculo_by_placa(placa)
            if veiculo:
                # preencher os campos com as informações do veículo encontrado
                self.txt_placa.setText(veiculo[0])               

                # buscar informações do veículo na tabela e preencher a tabela com elas
                result = self.db.select_veiculo_by_placa(placa)
                self.tb_veiculos.clearContents()
                self.tb_veiculos.setRowCount(1)
                for column, data in enumerate(result):
                    self.tb_veiculos.setItem(0, column, QTableWidgetItem(str(data)))
                return 'placa' # retorna 'placa' para indicar que a busca foi bem sucedida
            
    def buscar_cpf(self):
        cpf = self.txt_cpf.text()
        if cpf:
            veiculos = self.db.select_veiculos_by_cpf(cpf)
            if veiculos:
                self.tb_veiculos.clearContents()
                self.tb_veiculos.setRowCount(len(veiculos))
                for row, veiculo in enumerate(veiculos):
                    for column, data in enumerate(veiculo):
                        self.tb_veiculos.setItem(row, column, QTableWidgetItem(str(data)))
                return 'cpf' # retorna 'cpf' para indicar que a busca foi bem sucedida
            

    def buscar_registros_selecionados(self):
        registros_selecionados = []
        for row in range(self.tb_veiculos.rowCount()):
            checkbox = self.tb_veiculos.item(row, 0)
            if checkbox.checkState() == Qt.Checked:
                placa = self.tb_veiculos.item(row, 1).text()
                cpf = self.tb_veiculos.item(row, 2).text()
                marca = self.tb_veiculos.item(row, 3).text()
                modelo = self.tb_veiculos.item(row, 4).text()
                cor = self.tb_veiculos.item(row, 5).text()
                ano = self.tb_veiculos.item(row, 6).text()
                registros_selecionados.append([placa, cpf, marca, modelo, cor, ano])
        return registros_selecionados

            
 
app = QApplication(sys.argv)
app.setStyle('Fusion')
db = Data_base()
db.create_table_clientes()
db.create_table_produtos()
db.create_table_veiculos()
w = MainWindow()
w.show()
app.exec()