class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Usuario:
    def __init__(self, nome):
        self.nome = nome

class Venda:
    def __init__(self, usuario):
        self.usuario = usuario
        self.produtos = []

    def inserir(self, produto):
        self.produtos.append(produto)

banana = Produto("banana", 4)
usuario = Usuario("Pedro")
vendaInicial = Venda(usuario)
vendaInicial.inserir(banana)
primeiro = vendaInicial.produtos[0]
print(primeiro.nome)