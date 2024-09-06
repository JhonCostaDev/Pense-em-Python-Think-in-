class Produto:
    def __init__(self, nome_produto: str, quantidade: int, valor:float) -> None:
        self._nome_produto = nome_produto
        self._quantidade = quantidade
        self._valor = valor
        self._valor_em_estoque = self._quantidade * self._valor

    def valor_valido(self) -> int:
        while True:
            entrada = input("Digite o Valor:\n")
            try:
                valor = int(entrada)
            except ValueError:
                print('Valor Incorreto')
            
    # Getters ========================================
    @property
    def nome_produto(self) -> str:
        return self._nome_produto
    
    @property
    def quantidade(self)->int:
        return self._quantidade
    
    @property
    def valor(self)->float:
        return self._valor
    
    @property 
    def valor_em_estoque(self) ->float:
        return self._valor_em_estoque
    
    #Setters ========================================
    @nome_produto.setter
    def nome_produto(self, update_produto):
        self._nome_produto = update_produto

    @quantidade.setter
    def quantidade(self, update_quantidade):
        if valor_valido():
            self._quantidade = update_quantidade

    @valor.setter
    def valor(self, update_valor):
        self._valor = update_valor

    

    def __repr__(self):
        return f'''
        Produto: {self._nome_produto}
        Quantidade: {self._quantidade}
        Valor Unitário: R$ {self._valor}
        Valor em Estoque: R$ {self._valor_em_estoque}
        '''
    