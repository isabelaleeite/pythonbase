"""Cadastro de produto"""
__version__ = "0.1.0"

produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}

compra = ("Bruno", produto["nome"],3)
total_compra = compra[2] * produto["preco"]

print(
    f"O cliente {compra[0]} comprou {compra[1]}"
    f" e pagou o total de {total_compra}"
)