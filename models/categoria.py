'''
# não funcionou por erro de identação
class Categoria:
  def __init__(self, id, nome, descricao=""):
    self.id = id
    self.nome = nome
    self.descricao = descricao
    self.produtos = []

  def adicionar_produto(self, produto):
     self.produtos.append(produto)
     print(f"Produto '{produto.nome}' adicionado á categoria '{self.nome}' .")

  def listar_produto(self):
     print(f"Produtos da categoria: {self.nome} ")
     if not self.produtos:
        print("Nenhum produto cadastrado nesta categoria. ")
        return

     for prod in self.produtos:

         prod.exibir_detalhes()
'''
class Categoria:
    def __init__(self, id, nome, descricao=""):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado à categoria '{self.nome}'.")

    def listar_produtos(self):
        print(f"\n--- Produtos da Categoria: {self.nome} ---")
        if not self.produtos:
            print("Nenhum produto cadastrado nesta categoria.")
            return

        for prod in self.produtos:
            prod.exibir_detalhes()
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            id=dados["id"],
            nome=dados["nome"],
            descricao=dados["descricao"]
        )