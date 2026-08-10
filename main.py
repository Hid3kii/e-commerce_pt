'''
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

from models.produtos import Produto
from models.categoria import Categoria

# 1. Criando categorias
cat_hortifruti = Categoria(1, "Hortifrúti", "Produtos frescos da horta")
cat_eletronicos = Categoria(2, "Eletrônicos", "Dispositivos e acessórios")

# 2. Criando produtos
tomate = Produto(101, "Tomate Orgânico", 8.50, 50)
maca = Produto(102, "Maçã Fuji", 6.00, 30)
teclado = Produto(201, "Teclado Mecânico", 150.00, 10)

# 3. Associando produtos às suas categorias
cat_hortifruti.adicionar_produto(tomate)
cat_hortifruti.adicionar_produto(maca)
cat_eletronicos.adicionar_produto(teclado)

# 4. Listando produtos por categoria
cat_hortifruti.listar_produtos()
cat_eletronicos.listar_produtos()

from models.cliente import Cliente

cliente1 = Cliente(1, "João", "15151515151", "joão@gmail.com")

print("Dados do Cliente")
cliente1.exibir_DETALHES()

print("atualização de cadastro")
cliente1.atualizar_email("jpgmailcom")
cliente1.atualizar_email("jp@gmail.com")

cliente1.exibir_DETALHES()
'''
from models.produtos import Produto
from models.categoria import Categoria
from models.cliente import Cliente
from models.pedido import Pedido

# 1. Criando Entidades Base
cat_eletronicos = Categoria(1, "Eletrônicos")

teclado = Produto(101, "Teclado Mecânico", 150.00, 10)
mouse = Produto(102, "Mouse Gamer", 80.00, 5)
cat_eletronicos.adicionar_produto(teclado)
cat_eletronicos.adicionar_produto(mouse)

cliente1 = Cliente(1, "Carlos Eduardo", "111.222.333-44", "carlos@gmail.com")

# 2. Criando o Pedido
pedido1 = Pedido(id=1001, cliente=cliente1)

# 3. Adicionando Produtos ao Carrinho
pedido1.adicionar_produto(teclado, quantidade=2)
pedido1.adicionar_produto(mouse, quantidade=1)

# 4. Exibindo Resumo Antes de Finalizar
pedido1.exibir_resumo()

# 5. Finalizando a Compra (deve atualizar o estoque dos produtos)
pedido1.finalizar_pedido()

# 6. Verificando se o Estoque Realmente Baixou
print("--- Estoque Atualizado dos Produtos ---")
teclado.exibir_detalhes() # Esperado: 8 unidades em estoque
mouse.exibir_detalhes()   # Esperado: 4 unidades em estoque