import json
import os
from models.produtos import Produto
from models.cliente import Cliente
from models.categoria import Categoria

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_DADOS = os.path.join(BASE_DIR, "dados.json")

def salvar_dados(produtos, clientes, categorias):
    dados = {
        "produtos": [p.to_dict() for p in produtos],
        "clientes": [c.to_dict() for c in clientes],
        "categorias": [cat.to_dict() for cat in categorias]
    }
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print("💾 Dados salvos com sucesso!")

def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return [], [], []

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            dados = json.load(f)
            
            produtos = [Produto.from_dict(p) for p in dados.get("produtos", [])]
            clientes = [Cliente.from_dict(c) for c in dados.get("clientes", [])]
            categorias = [Categoria.from_dict(cat) for cat in dados.get("categorias", [])]
            
            return produtos, clientes, categorias
    except Exception as e:
        print(f"⚠️ Erro ao carregar dados: {e}")
        return [], [], []