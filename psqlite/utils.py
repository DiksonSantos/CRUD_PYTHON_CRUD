import sqlite3


def conectar():
    """
    Função para conectar ao servidor
    """
    conn = sqlite3.connect('psqlite3.Dikson')

    conn.execute("""CREATE TABLE IF NOT EXISTS produtos(
    id integer primary key autoincrement,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL);""")

    return conn



def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    conn.close()

    print('Desconectando do servidor...')


def listar():
    """
    Função para listar os produtos
    """
    print('Listando produtos...')
    # COnecta com o banco
    conn = conectar()
    # Acessa o banco
    cur = conn.cursor()
    # A partir do cursor, usa-se os comandos pertinente a operação do banco.
    cur.execute('SELECT * FROM produtos')
    # Coloca tudo numa lista
    produtos = cur.fetchall()

    if len(produtos) > 0:
        print('Listando Produtos')
        print(11*'-')
        for produto in produtos:
            print(f'ID {produto[0]}')
            print(f'Produto {produto[1]}')
            print(f'Preço {produto[2]}')
            print(f'Estoque {produto[3]}')
            print(11*'--')
    else:
        print("Não há produtos cadastrados")
    desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    """  
    print('Inserindo produto...')
    conn = conectar()
    cur = conn.cursor()

    nome = input("Nome: ")
    preco = float(input("Preço: "))
    estoque = int(input("Quant em Estoque: "))

    cur.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}','{preco}','{estoque}')")
    conn.commit()

    if cur.rowcount == 1:
        print(f"O produto {nome} foi inserido com sucesso")
        desconectar(conn)

def atualizar():
    """
    Função para atualizar um produto
    """
    print('Atualizando produto...')
    conn = conectar()
    cur = conn.cursor()

    codigo = int(input("Informe Codigo: "))
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    estoque = int(input("Quant em Estoque: "))

    cur.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
    conn.commit()

    if cur.rowcount == 1:
        print(f"Produto {nome} Atualizado com sucesso!!")
    else:
        print("Erro ao atualizar")
    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """  
    print('Deletando produto...')
    conn = conectar()
    cur = conn.cursor()

    codigo = int(input("Informe o codigo do produto: "))

    cur.execute(f"DELETE FROM produtos WHERE id={codigo}")
    conn.commit()

    if cur.rowcount == 1:
        print("Produto Deletado com sucesso!")
    else:
        print("Falha ao tentar excluir  :/")


def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
