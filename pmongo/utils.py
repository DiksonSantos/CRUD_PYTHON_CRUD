from pymongo import MongoClient, errors
from bson.objectid import ObjectId
from bson import errors as beeson


def conectar():
    """
    Função para conectar ao servidor
    """
    conn = MongoClient('localhost', 27017)

    return conn


def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    # 'pmongo' Foi criado no MongoCompass (é um banco de dados)
    db = conn.pmongo

    try:
        if db.produtos.count_documents({}) > 0:
            # Esta variavel recebe tudo o que for encontrado:
            produtos = db.produtos.find()
            print('Listando Produtos')
            print(11*'-')
            for produto in produtos:
                print(f"ID:{produto['_id']}")
                print(f"Produtos: {produto['nome']}")
                print(f"Preço: {produto['preço']}")
                print(f"Estoque: {produto['estoque']}")
                print(11*'-')
        else:
            print("Nada Cadastrado")
    except errors.PyMongoError as e:
        print(f"Erro {e} Ao acessar o Banco de Dados")
    desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    DENTRO DO BANCO 'PMONGO' EXISTE A COLEÇÃO 'PRODUTOS',
    Caso ela não exista, ela sera criada
    """  
    conn = conectar()
    db = conn.pmongo

    nome = input('Nome Do Produto: ')
    preco = float(input("Preço: "))
    estoque = int(input('Estoque: '))

    try:
        db.produtos.insert_one(
            {
                "nome": nome,
                "preço": preco,
                "estoque": estoque
            }
        )
        print(f"O Produto {nome} foi Inserido com sucesso!")
    except errors.PyMongoError as e:
        print(f"Erro {e} foi encontrado PRODUTO NÃO INSERIDO")
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    db = conn.pmongo

    _id = input('ID do Produto: ')
    nome = input("Nome: ")
    preco = float(input("Preço Do Produto: "))
    estoque = int(input('Estoque: '))

    try:
        if db.produtos.count_documents({}) > 0:
            res = db.produtos.update_one(
                {"_id": ObjectId(_id)}, {
                    "$set":{
                        "nome": nome,
                        "preço": preco,
                        "estoque": estoque
                    }
                }
            )
            if res.modified_count == 1:
                print(f'O produto foi atualizado com sucesso')
            else:
                print("Produto Não atualizado")
        else:
            print("Não existem documentos para serem atualizados")
    except errors.PyMongoError as e:
        print(f"Erro {e}")
    except beeson.InvalidId as f:
        print(f"Object ID errors {f}")
    desconectar(conn)



def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    db = conn.pmongo

    _id = input("Informe o ID do Produto: ")

    try:
        if db.produtos.count_documents({}) > 0:
            res = db.produtos.delete_one(
                {
                    "_id": ObjectId(_id)
                }
            )
            if res.deleted_count > 0:
                print(f"Produto Deletado com sucesso")
            else:
                print("Não foi possivel deletar /:")
        else:
            print("Nçao existem produtos a serem deletados")
    except errors.PyMongoError as e:
        print(f"Erro {e} ao acessar o Banco de dados")
    except beeson.InvalidId as f:
        print(f"Object ID errors {f}")
    desconectar(conn)


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
