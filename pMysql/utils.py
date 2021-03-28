import MySQLdb


def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = MySQLdb.connect(
            db='pmysql',
            host='localhost',
            user='root',
            passwd='%alpha%')
        return conn
    except MySQLdb.Error as e:
        print('Conectando ao servidor...')
        print(f"Erro Na Conexão {e}")




def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()

    print('Desconectando do servidor...')


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * from produtos')
    # Transforma o retorno da linha de cima em uma Lista
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando Produtos')
        print(10*'-')
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'Nome: {produto[1]}')
            print(f'Preço: {produto[2]}')
            print(f'Estoque: {produto[3]}')
            print(11*'--')
    else:
        print('No Products ')
    desconectar(conn)



def inserir():
    """
    Função para inserir um produto
    """  
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input("Preço do Produto: "))
    estoque = int(input('Informe A Quant Em Estoque: '))
    # nome é uma String por isso esta entre aspas.
    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}',{preco},{estoque})")
    conn.commit()
    if cursor.rowcount == 1:
        print(f'O Produto {nome} foi inserido Com sucesso')
    else:
        print("Nenhum Produto Inserido")
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input("Codigo: "))
    nome = str(input('Nome: '))
    preco = float(input("Preço: "))
    estoque = int(input("Nova Quantidade Em Estoque: "))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
    conn.commit()
    # print('Atualizando produto...')

    if cursor.rowcount == 1:
        print(f"Produto {nome} foi atualizado com sucesso!")
    else:
        print('Erro ao atualizar a bagaça')
    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input("Codigo do Produto: "))

    cursor.execute(f'DELETE FROM produtos WHERE id={codigo}')
    print('Deletando produto...')
    conn.commit()

    if cursor.rowcount == 1:
        print(f"Produto Excluido")

    else:
        print("Erro ao excluir o trem")


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
