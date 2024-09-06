import produto
class Estoque:
    def __init__(self) -> None:
        self.estoque = {}
        self.itens_estoque = len(self.estoque)

    def exibir_estoque(self):
        if self.itens_estoque == 0:
            return 'O estoque está vazio'
        else:
            for chave, valor in self.estoque.items():
                print(f'{chave}: {valor}')

    # def cadastrar_produto(self, nome):
    #     if nome == self.estoque.get(nome):




    