class Produto:
    def __init__(self, id, nome, preco, estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir_detalhes(self):
        print(f"ID: {self.id} | Nome: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque}")

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.estoque += quantidade
            print(f"Adicionadas {quantidade} unidades ao estoque de {self.nome}.")
        else:
            print("A quantidade para adicionar deve ser maior que zero!")

    def remover_estoque(self, quantidade):
        if quantidade <= 0:
            print("A quantidade para remover deve ser maior que zero!")
        elif quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f"Removidas {quantidade} unidades do estoque de {self.nome}.")
        else:
            print(f"Venda não permitida! Estoque insuficiente para {self.nome}. Disponível: {self.estoque}")


    def to_dict(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "estoque": self.estoque,
        }          

    @classmethod
    def from_dict(cls, dados):
        return cls(
            id=dados["id"],
            nome=dados["nome"],
            preco=dados["preco"],
            estoque=dados["estoque"]
        )