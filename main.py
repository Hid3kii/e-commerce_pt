#Importa a classe de produtos
from models.produtos import Produto

produto1 = Produto(1, "tomate", 150.00, 10)

print("Produto 1")
print("Id: ", produto1.id)
print("Nome: ", produto1.nome)
print("Preço: R$", produto1.preco)
print("Estoque: ", produto1.estoque)