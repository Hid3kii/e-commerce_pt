class Pedido:
    def __init__(self, id, cliente):
        self.id = id
        self.cliente = cliente      # Instância da classe Cliente
        self.itens = []             # Lista de objetos Produto adicionados ao carrinho
        self.status = "Pendente"    # Status inicial do pedido

    # Adiciona um produto ao carrinho do pedido
    def adicionar_produto(self, produto, quantidade=1):
        if self.status != "Pendente":
            print(f"Não é possível adicionar itens. Pedido #{self.id} já está {self.status}.")
            return

        # Verifica se há estoque suficiente antes de colocar no carrinho
        if produto.estoque >= quantidade:
            # Armazenamos uma tupla com o produto e a quantidade desejada
            self.itens.append({"produto": produto, "quantidade": quantidade})
            print(f"Adicionado: {quantidade}x '{produto.nome}' ao Pedido #{self.id}.")
        else:
            print(f"Estoque insuficiente para '{produto.nome}'. Disponível: {produto.estoque}")

    # Calcula o valor total dos itens no carrinho
    def calcular_total(self):
        total = 0.0
        for item in self.itens:
            prod = item["produto"]
            qtd = item["quantidade"]
            total += prod.preco * qtd
        return total

    # Finaliza a compra: debita o estoque de cada produto e altera o status
    def finalizar_pedido(self):
        if self.status != "Pendente":
            print(f"Pedido #{self.id} já foi finalizado ou cancelado.")
            return

        if not self.itens:
            print(f"Não é possível finalizar o Pedido #{self.id}: o carrinho está vazio!")
            return

        # Debita o estoque de cada item comprado
        for item in self.itens:
            prod = item["produto"]
            qtd = item["quantidade"]
            prod.remover_estoque(qtd)

        self.status = "Pago"
        print(f"\n✅ Pedido #{self.id} finalizado com sucesso! Status: {self.status}")

    # Exibe o resumo do pedido
    def exibir_resumo(self):
        print(f"\n================ RESUMO DO PEDIDO #{self.id} ================")
        print(f"Cliente: {self.cliente.nome} | CPF: {self.cliente.cpf}")
        print(f"Status: {self.status}")
        print("---------------------------------------------------------")
        if not self.itens:
            print("Carrinho vazio.")
        else:
            for item in self.itens:
                prod = item["produto"]
                qtd = item["quantidade"]
                subtotal = prod.preco * qtd
                print(f"- {qtd}x {prod.nome} (R${prod.preco:.2f} cada) = R${subtotal:.2f}")
            print("---------------------------------------------------------")
            print(f"VALOR TOTAL: R${self.calcular_total():.2f}")
        print("=========================================================\n")