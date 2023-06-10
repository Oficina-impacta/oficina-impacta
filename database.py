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

    def create_table_veiculos(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("""

                        CREATE TABLE IF NOT EXISTS Veiculos(
       PLACA TEXT NOT NULL,                     
       CPF TEXT,
       MARCA TEXT,
       MODELO TEXT,
       COR TEXT,
       ANO TEXT,

       PRIMARY KEY (PLACA)
       );

                            """)
        self.close_connection()

    def create_table_os_aberta(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("""

                        CREATE TABLE IF NOT EXISTS OsAbertas(
       PEDIDO TEXT NOT NULL,
       NOME TEXT,                     
       CPF TEXT,
       PLACA TEXT,
       MARCA TEXT,
       MODELO TEXT,
       VALOR TEXT,

       PRIMARY KEY (PEDIDO)
       );

                            """)
        self.close_connection()

    def create_table_os_fechadas(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("""

                        CREATE TABLE IF NOT EXISTS OsFechadas(
       PEDIDO TEXT NOT NULL,
       NOME TEXT,                     
       CPF TEXT,
       PLACA TEXT,
       MARCA TEXT,
       MODELO TEXT,
       VALOR TEXT,

       PRIMARY KEY (PEDIDO)
       );

                            """)
        self.close_connection()

    #Função registrar no banco de dados
    def registro_clientes(self, fullDataSet):      
      self.connect()
      campos_tabela = ('NOME','CPF','TELEFONE','CEP','LOGRADOURO','NUMERO',
                     'COMPLEMENTO','BAIRRO','CIDADE')
      qntd = ("?,?,?,?,?,?,?,?,?")
      cursor = self.connection.cursor()        
    
    # Verificar se o CPF está vazio ou é inválido
      cpf = fullDataSet[1]
      print("Valor de cpf:", cpf)
      if not cpf or len(cpf) != 14:
        return 'erro', 'CPF é obrigatório e deve ter 11 caracteres.'
    
    #VERIFICAR SE O CPF JÁ EXISTE
      cursor.execute("SELECT CPF FROM Clientes WHERE CPF=?", (cpf,))
      cpf_existente = cursor.fetchone()
      if cpf_existente:
        # CPF já existe, retornar erro
        return 'erro', 'CPF já cadastrado.'    

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

    # Função para registar os dados da tela de cadastro_produtos
    def registro_produtos(self, fullDataSet):

        self.connect()
        campos_tabela = ('COD', 'NOME', 'TIPO', 'PRECO')
        qntd = ("?,?,?,?")
        cursor = self.connection.cursor()

        ############################################################################
        # Esse IF não está sendo mais utilizado, pois foi implementado uma lógica
        # na feature Janela_principal
        # if fullDataSet[0] == '':
        #     return 'erro', 'O campo COD é obrigatório.'
        ############################################################################

        # Verifica se o código já foi cadastrado
        cursor.execute("SELECT * FROM Produtos WHERE COD = ?", (fullDataSet[0],))
        resultado = cursor.fetchone()
        if resultado is not None:
            return 'erro', 'Já existe esse código cadastrado.'
        
        if not fullDataSet[0].isnumeric():
            return 'erro', 'O código deve conter apenas caracteres numéricos.'
          
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

    # Função para registar os dados da tela de cadastro_veiculos    
    def registro_veiculos(self, fullDataSet):

        self.connect()
        campos_tabela = ('placa', 'cpf', 'marca', 'modelo','cor','ano')
        qntd = ("?,?,?,?,?,?")
        cursor = self.connection.cursor()
        
        #Verificar se o campo placa foi preenchido
        if fullDataSet[0] == '':
            print(fullDataSet)
            return 'erro', 'O campo Placa é obrigatório.'

        # Verifica se a placa já foi cadastrada
        cursor.execute("SELECT * FROM Veiculos WHERE placa = ?", (fullDataSet[0],))
        resultado = cursor.fetchone()
        if resultado is not None:
            return 'erro', 'Já existe um veículo cadastrado com esta placa.'
          
        #REGISTRAR OS DADOS
        try:
            cursor.execute(f"""INSERT INTO Veiculos {campos_tabela}
                    VALUES ({qntd})""", fullDataSet)
            self.connection.commit()

            return "OK", "Veiculo cadastrado com sucesso"
        except Exception as e:
            print(e)
            return 'erro', str(e)

        finally:
            self.close_connection()

    # Função para registar as ordens de serviços criadas    
    def registro_pedido(self, fullDataSet):
    
        print(fullDataSet)
        self.connect()
        campos_tabela = ('pedido', 'nome', 'cpf', 'placa', 'marca', 'modelo', 'valor')
        qntd = ("?,?,?,?,?,?,?")
        cursor = self.connection.cursor()

        #REGISTRAR OS DADOS
        try:
            cursor.execute(f"""INSERT INTO OsAbertas {campos_tabela}
                    VALUES ({qntd})""", fullDataSet)
            self.connection.commit()

            return "OK", "Pedido criado com sucesso"
        except Exception as e:
            print(e)
            return 'erro', str(e)

        finally:
            self.close_connection()            

    #Função selecionar Clientes
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

    #Função selecionar Produtos
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

    #Função selecionar Veiculos
    def select_all_veiculos(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Veiculos ORDER BY PLACA")
            veiculos = cursor.fetchall()
            return veiculos
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    #Função selecionar pedidos
    def select_all_pedidos(self):
        try:
            self.connect()
            # print("Conexão estabelecida com sucesso")
            
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM OsAbertas ORDER BY PEDIDO")
            OsAberta = cursor.fetchall()
            
            # print("Consulta executada com sucesso")
            # print("Resultados encontrados:")
            for row in OsAberta:
                print(row)
            
            return OsAberta
        except Exception as e:
            print("Ocorreu um erro durante a execução da consulta:")
            print(e)
        finally:
            self.close_connection()
            # print("Conexão fechada")

    def select_all_historico(self):
        try:
            self.connect()
            # print("Conexão estabelecida com sucesso")
            
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM OsFechadas ORDER BY PEDIDO")
            OsFechada = cursor.fetchall()
            
            # print("Consulta executada com sucesso")
            # print("Resultados encontrados:")
            for row in OsFechada:
                print(row)
            
            return OsFechada
        except Exception as e:
            print("Ocorreu um erro durante a execução da consulta:")
            print(e)
        finally:
            self.close_connection()
            # print("Conexão fechada")

    #Função deletar clientes
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

    #Função deletar produtos
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

    #Função deletar veiculos
    def delete_veiculos(self, placa):

        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE  FROM Veiculos WHERE PLACA = '{placa}'")
            self.connection.commit()
            return 'OK', 'Veiculo deletado com sucesso!' 
        except Exception as e:
            return 'erro', str(e)
        finally:
            self.close_connection()

    def delete_pedido(self, pedido):

        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE  FROM OsAbertas WHERE PEDIDO = '{pedido}'")
            self.connection.commit()
            return 'OK', 'Pedido deletado com sucesso!' 
        except Exception as e:
            return 'erro', str(e)
        finally:
            self.close_connection()

    #Função para atualizar dados dos registro da tabela clientes
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
 
    #Função para atualizar dados dos registro da tabela produtos
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

    #Função para atualizar dados dos registro da tabela veiculos

    def update_veiculos(self, placa, cpf, marca, modelo, cor, ano):
        self.connect()

        try:
            cursor = self.connection.cursor()
            placa = (placa)            
            cpf = (cpf)
            marca = (marca)
            modelo = (modelo)            
            cor = (cor)
            ano = (ano)
            cursor.execute("""UPDATE Veiculos SET placa = ?, cpf = ?, marca = ?, modelo = ?, cor = ?, ano = ?""",
               (placa, cpf, marca, modelo, cor, ano))
            self.connection.commit()
            return 'OK', 'Dados atualizados com sucesso!'
        except Exception as e:
            return 'erro', str(e)
        finally:
            self.close_connection()

    def select_veiculo_by_placa(self, placa):
       try:
           self.connect()
           cursor = self.connection.cursor()
           cursor.execute("SELECT * FROM Veiculos WHERE PLACA = ?", (placa,))
           veiculo = cursor.fetchone()
           return veiculo
       except Exception as e:
           print(e)
       finally:
           self.close_connection()

    def select_veiculos_by_cpf(self, cpf):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Veiculos WHERE REPLACE(CPF, '.', '') = REPLACE(?, '.', '') AND REPLACE(CPF, '-', '') = REPLACE(?, '-', '')", (cpf, cpf,))
            veiculos = cursor.fetchall()
            return veiculos
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def obter_dados_cliente_por_cpf_veiculo(self, cpf_veiculo):
       try:
           self.connect()
           cursor = self.connection.cursor()
           cursor.execute("SELECT c.nome, c.cpf, c.telefone, c.cep FROM Clientes c JOIN Veiculos v ON c.cpf = v.cpf WHERE REPLACE(v.CPF, '.', '') = REPLACE(?, '.', '') AND REPLACE(v.CPF, '-', '') = REPLACE(?, '-', '')", (cpf_veiculo, cpf_veiculo))
           cliente_correspondente = cursor.fetchone()  # Recupera apenas um cliente correspondente
           return cliente_correspondente
       except Exception as e:
           print(e)
       finally:
           self.close_connection()

    # função para mover o pedido da tabela Osabertas para OSfechadas e efetuar o delete da tabela inicial
    def mover_pedido_fechadas(self, pedido_data):
        try:
            self.connect()
            cursor = self.connection.cursor()

            # Extrai os dados do pedido
            pedido = pedido_data[0]
            nome = pedido_data[1]
            cpf = pedido_data[2]
            placa = pedido_data[3]
            marca = pedido_data[4]
            modelo = pedido_data[5]
            valor = pedido_data[6]

            # Insere os dados do pedido na tabela de pedidos fechados
            cursor.execute("INSERT INTO OsFechadas (PEDIDO, NOME, CPF, PLACA, MARCA, MODELO, VALOR) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (pedido, nome, cpf, placa, marca, modelo, valor))
            self.connection.commit()

            # Remove o pedido da tabela de pedidos em aberto
            cursor.execute("DELETE FROM OsAbertas WHERE PEDIDO=?", (pedido,))
            self.connection.commit()

            return "OK", "Pedido Faturado com Sucesso."
        except Exception as e:
            return "Erro", f"Erro ao mover o pedido para a tabela de pedidos fechados: {str(e)}"
        finally:
            self.close_connection()

    def selecionar_pedido(self, pedido):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM OsAbertas WHERE PEDIDO=?", (pedido,))
            pedido_data = cursor.fetchone()
            return pedido_data
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def numero_pedido(self):
    
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute('select count(*) from OsAbertas')
            tabela_aberta = cursor.fetchall()
            cursor.execute('select count(*) from OsFechadas')
            tabela_fechada = cursor.fetchall()
            numero_pedido = sum(tabela_aberta[0] + tabela_fechada[0])
            return (numero_pedido)

    def obter_registros_os_fechadas(self):
      try:
          self.connect()
          cursor = self.connection.cursor()

          # Execute a consulta SQL para obter os registros da tabela OsFechadas
          cursor.execute("SELECT * FROM OsFechadas")
          registros = cursor.fetchall()

          return registros
      except Exception as e:
          # Lide com erros de consulta ou conexão com o banco de dados
          return None
      finally:
          self.close_connection()

    def obter_servicos_em_aberto(self):
      try:
          self.connect()
          cursor = self.connection.cursor()
  
          # Execute a consulta SQL para obter os registros da tabela OsAbertas
          cursor.execute("SELECT * FROM OsAbertas")
          registros = cursor.fetchall()
  
          return registros
      except Exception as e:
          # Lide com erros de consulta ou conexão com o banco de dados
          return None
      finally:
          self.close_connection()
       