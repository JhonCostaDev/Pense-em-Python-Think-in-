class Produto:
    def __init__(self, nome_produto: str, quantidade: int, valor:float) -> None:
        self._nome_produto = nome_produto
        self._quantidade = quantidade
        self._valor = valor
        self._valor_em_estoque = self._quantidade * self._valor

    def __repr__(self):
        return f'''
        Produto: {self._nome_produto}
        Quantidade: {self._quantidade}
        Valor Unitário: R$ {self._valor}
        Valor em Estoque: R$ {self._valor_em_estoque}
        '''
    