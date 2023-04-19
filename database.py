import sqlite3
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

    #função deletar
    def delete_clientes(self, cpf):

        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE  FROM Clientes WHERE CPF = '{cpf}'")
            self.connection.commit()
            return "OK"
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    #função update;; atualizar tabela
    def update_cliente(self, fullDataSet):

        self.connect()

        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" UPDATE CLIENTES SET

                            NOME = '{fullDataSet[0]}',
                            CPF = '{fullDataSet[1]}',
                            TELEFONE = '{fullDataSet[2]}',
                            CEP = '{fullDataSet[3]}',
                            LOGRADOURO = '{fullDataSet[4]}',
                            NUMERO = '{fullDataSet[5]}',
                            COMPLEMENTO = '{fullDataSet[6]}',
                            BAIRRO = '{fullDataSet[7]}',
                            CIDADE = '{fullDataSet[8]}'

                            WHERE CPF = '{fullDataSet[1]}'""")
            self.connection.commit()
            print('ok aqui')
            return 'OK', 'Dados atualizados com sucesso!'
        except Exception as e:
            return 'erro', str(e)
        finally:
                self.close_connection

    def update_produtos(self, fullDataSet):

        self.connect()

        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" UPDATE CLIENTES SET

                            NOME = '{fullDataSet[0]}',
                            CPF = '{fullDataSet[1]}',
                            TELEFONE = '{fullDataSet[2]}',
                            CEP = '{fullDataSet[3]}',
                            LOGRADOURO = '{fullDataSet[4]}',
                            NUMERO = '{fullDataSet[5]}',
                            COMPLEMENTO = '{fullDataSet[6]}',
                            BAIRRO = '{fullDataSet[7]}',
                            CIDADE = '{fullDataSet[8]}'

                            WHERE CPF = '{fullDataSet[1]}'""")
            self.connection.commit()
            print('ok aqui')
            return 'OK', 'Dados atualizados com sucesso!'
        except Exception as e:
            return 'erro', str(e)
        finally:
                self.close_connection

