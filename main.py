from models.produtos import Produto
from models.categoria import Categoria
from models.cliente import Cliente
from models.pedido import Pedido
from database import salvar_dados, carregar_dados

# Carrega os dados do arquivo ao iniciar o programa
produtos, clientes, categorias = carregar_dados()
# Armazenamento em memória (Simulação de Banco de Dados)
categorias = []
produtos = []
clientes = []
pedidos = []

# Geradores simples de ID
proximo_id_cat = 1
proximo_id_prod = 101
proximo_id_cli = 1
proximo_id_ped = 1001


def exibir_menu():
    print("\n==========================================")
    print("      🛒 SISTEMA DE E-COMMERCE PY        ")
    print("==========================================")
    print("1. Cadastrar Categoria")
    print("2. Cadastrar Produto")
    print("3. Cadastrar Cliente")
    print("4. Criar e Finalizar Pedido")
    print("5. Listar Tudo (Categorias, Produtos, Clientes)")
    print("0. Sair")
    print("==========================================")


while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print("\n--- CADASTRO DE CATEGORIA ---")
        nome = input("Nome da categoria: ").strip()
        descricao = input("Descrição (opcional): ").strip()
        
        nova_cat = Categoria(proximo_id_cat, nome, descricao)
        categorias.append(nova_cat)
        proximo_id_cat += 1
        print(f"✅ Categoria '{nome}' cadastrada com sucesso!")

    elif opcao == "2":
        print("\n--- CADASTRO DE PRODUTO ---")
        if not categorias:
            print("⚠️ Cadastre ao menos uma Categoria antes de cadastrar produtos!")
            continue

        nome = input("Nome do produto: ").strip()
        preco = float(input("Preço (R$): "))
        estoque = int(input("Quantidade em estoque: "))

        print("\nCategorias disponíveis:")
        for idx, cat in enumerate(categorias):
            print(f"[{idx}] {cat.nome}")
        
        idx_cat = int(input("Selecione o número da categoria: "))
        categoria_selecionada = categorias[idx_cat]

        novo_prod = Produto(proximo_id_prod, nome, preco, estoque)
        produtos.append(novo_prod)
        categoria_selecionada.adicionar_produto(novo_prod)
        proximo_id_prod += 1
        salvar_dados(produtos, clientes, categorias)
        print(f"✅ Produto '{nome}' cadastrado com sucesso!")

    elif opcao == "3":
        print("\n--- CADASTRO DE CLIENTE ---")
        nome = input("Nome do cliente: ").strip()
        cpf = input("CPF: ").strip()
        email = input("E-mail: ").strip()

        novo_cli = Cliente(proximo_id_cli, nome, cpf, email)
        clientes.append(novo_cli)
        proximo_id_cli += 1
        salvar_dados(produtos, clientes, categorias)
        print(f"✅ Cliente '{nome}' cadastrado com sucesso!")

    elif opcao == "4":
        print("\n--- CRIAR PEDIDO ---")
        if not clientes:
            print("⚠️ Cadastre ao menos um Cliente primeiro!")
            continue
        if not produtos:
            print("⚠️ Cadastre ao menos um Produto primeiro!")
            continue

        print("\nClientes disponíveis:")
        for idx, cli in enumerate(clientes):
            print(f"[{idx}] {cli.nome} (CPF: {cli.cpf})")
        
        idx_cli = int(input("Selecione o número do cliente: "))
        cliente_sel = clientes[idx_cli]

        novo_pedido = Pedido(proximo_id_ped, cliente_sel)

        # Adicionando produtos ao carrinho
        while True:
            print("\nProdutos disponíveis:")
            for idx, prod in enumerate(produtos):
                print(f"[{idx}] {prod.nome} - R${prod.preco:.2f} (Estoque: {prod.estoque})")
            
            idx_prod = int(input("Selecione o número do produto (ou -1 para finalizar carrinho): "))
            if idx_prod == -1:
                break
            
            qtd = int(input("Quantidade desejada: "))
            novo_pedido.adicionar_produto(produtos[idx_prod], qtd)

        # Resumo e Finalização
        novo_pedido.exibir_resumo()
        confirmar = input("Deseja finalizar o pedido agora? (s/n): ").strip().lower()
        if confirmar == 's':
            novo_pedido.finalizar_pedido()
            pedidos.append(novo_pedido)
            proximo_id_ped += 1
            salvar_dados(produtos, clientes, categorias)

    elif opcao == "5":
        print("\n================ RELATÓRIO GERAL ================")
        print("\n--- CLIENTES ---")
        if not clientes:
            print("Nenhum cliente cadastrado.")
        for c in clientes:
            c.exibir_detalhes()

        print("\n--- CATEGORIAS E PRODUTOS ---")
        if not categorias:
            print("Nenhuma categoria cadastrada.")
        for cat in categorias:
            cat.listar_produtos()

    elif opcao == "0":
        print("\nSaindo do sistema... Até logo! 👋")
        break

    else:
        print("❌ Opção inválida! Tente novamente.")
