import sqlite3
import re
# #Criando o Banco de Dados:
# FUNÇÃO CRIANDO BANCO DE DADOS

class Data_base:

    def __init__(self, name= 'system.db') -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)
    
    #função criando tabelas
    def create_table_clientes(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("""

                        CREATE TABLE IF NOT EXISTS Clientes(

       NOME TEXT,
       CPF TEXT,
       TELEFONE TEXT,
       CEP TEXT,
       LOGRADOURO TEXT,
       NUMERO TEXT,
       COMPLEMENTO TEXT,
       BAIRRO TEXT,
       CIDADE, TEXT,

       PRIMARY KEY (CPF)
       );

                            """)
        self.close_connection()

    def create_table_produtos(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("""

                        CREATE TABLE IF NOT EXISTS Produtos(
       COD TEXT,                     
       NOME TEXT,
       TIPO TEXT,
       PRECO TEXT,

       PRIMARY KEY (COD)
       );

                            """)
        self.close_connection()

    #função registrar no banco de dados
    def registro_clientes(self, fullDataSet):

        self.connect()
        campos_tabela = ('NOME','CPF','TELEFONE','CEP','LOGRADOURO','NUMERO',
        'COMPLEMENTO','BAIRRO','CIDADE')
        qntd = ("?,?,?,?,?,?,?,?,?")
        cursor = self.connection.cursor()
        #REGISTRAR OS DADOS
        try:
            cursor.execute(f"""INSERT INTO Clientes {campos_tabela}

                    VALUES ({qntd})""", fullDataSet)
            self.connection.commit()
            return "OK", "Cliente cadastrado com sucesso!"
        except Exception as e:
            print(e)
            return 'erro', str(e)

        finally:
            self.close_connection()

    def registro_produtos(self, fullDataSet):

        self.connect()
        campos_tabela = ('COD', 'NOME', 'TIPO', 'PRECO')
        qntd = ("?,?,?,?")
        cursor = self.connection.cursor()
        #REGISTRAR OS DADOS
        try:
            cursor.execute(f"""INSERT INTO Produtos {campos_tabela}

                    VALUES ({qntd})""", fullDataSet)
            self.connection.commit()
            return "OK", "Produto ou Serviço cadastrado com sucesso!"
        except Exception as e:
            print(e)
            return 'erro', str(e)

        finally:
            self.close_connection()

    #função selecionar
    def select_all_clientes(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Clientes ORDER BY NOME")
            clientes = cursor.fetchall()
            return clientes
        except Exception as e:
            print(e)
        finally:
            self.close_connection()
    
    def select_all_produtos(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Produtos ORDER BY COD")
            produtos = cursor.fetchall()
            return produtos
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    #função deletar clientes
    def delete_clientes(self, cpf):

        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE  FROM Clientes WHERE CPF = '{cpf}'")
            self.connection.commit()
            return 'OK', 'Cliente deletado com sucesso!' 
        except Exception as e:
            return 'erro', str(e)
        finally:
            self.close_connection()

    #função deletar produtos
    def delete_produtos(self, cod):

        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE  FROM Produtos WHERE COD = '{cod}'")
            self.connection.commit()
            return 'OK', 'Produto ou serviço deletado com sucesso!' 
        except Exception as e:
            return 'erro', str(e)
        finally:
            self.close_connection()

    

    def update_clientes(self, nome, telefone, cep, logradouro, numero, complemento, bairro, cidade, cpf):
        self.connect()

        try:
            cursor = self.connection.cursor()
            nome = (nome)
            telefone = (telefone)
            cep = (cep)
            logradouro = (logradouro)
            numero = (numero)
            complemento = (complemento)
            bairro = (bairro)
            cidade = (cidade)
            cursor.execute("""UPDATE CLIENTES SET NOME = ?, TELEFONE = ?, CEP = ?, LOGRADOURO = ?, NUMERO = ?, 
                  COMPLEMENTO = ?, BAIRRO = ?, CIDADE = ? WHERE CPF = ?""",
               (nome, telefone, cep, logradouro, numero, complemento, bairro, cidade, cpf))
            self.connection.commit()
            return 'OK', 'Dados atualizados com sucesso!'
        except Exception as e:
            return 'erro', str(e)
        finally:
            self.close_connection()

          

    def update_produtos(self, COD, NOME, TIPO, PRECO):
        self.connect()

        try:
            cursor = self.connection.cursor()
            COD = (COD)            
            NOME = (NOME)
            TIPO = (TIPO)
            PRECO = (PRECO)            
            cursor.execute("""UPDATE Produtos SET COD = ?, NOME = ?, TIPO = ?, PRECO = ?""",
               (COD, NOME, TIPO, PRECO))
            self.connection.commit()
            return 'OK', 'Dados atualizados com sucesso!'
        except Exception as e:
            return 'erro', str(e)
        finally:
            self.close_connection()