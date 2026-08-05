#Importa a classe de produtos
from models.produtos import Produto

tomate = Produto(1, "tomate", 150.00, 10)

print("Produto 1")
print("Id: ", tomate.id)
print("Nome: ", tomate.nome)
print("Preço: R$", tomate.preco)
print("Estoque: ", tomate.estoque)

print("--- Estado Inicial ---")
tomate.exibir_detalhes()

print("\n--- Testando Recebimento de Estoque ---")
tomate.adicionar_estoque(5)
tomate.exibir_detalhes() # Esperado: 15 unidades

print("\n--- Testando Venda Com Sucesso ---")
tomate.remover_estoque(3)
tomate.exibir_detalhes() # Esperado: 12 unidades

print("\n--- Testando Venda Sem Estoque Suficiente ---")
tomate.remover_estoque(20) # Deve disparar o aviso de estoque insuficiente!
tomate.exibir_detalhes() # Deve continuar com 12 unidad