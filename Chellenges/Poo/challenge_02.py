class Venda:
    def __init__(self, produto, valor):
        self.produto = produto
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    def adicionar_venda(self, venda):
        """Adiciona uma venda à lista de vendas da categoria."""
        self.vendas.append(venda)

    def total_vendas(self):
        """Calcula e retorna o total das vendas na categoria, somando os valores fornecidos."""
        total = sum(venda.valor for venda in self.vendas)
        return total

def main():
    # Entrada fornecida
    # entrada = [
    #     {"categoria": "Eletrônicos", "produto": "Celular", "quantidade": 5, "valor": 1000},
    #     {"categoria": "Eletrônicos", "produto": "Fone de Ouvido", "quantidade": 10, "valor": 500},
    #     {"categoria": "Móveis", "produto": "Mesa", "quantidade": 2, "valor": 800},
    #     {"categoria": "Móveis", "produto": "Cadeira", "quantidade": 4, "valor": 400}
    # ]
    entrada = [
        {"categoria": "Alimentos", "produto": "Arroz", "quantidade": 10, "valor": 200},
        {"categoria": "Alimentos", "produto": "Feijão", "quantidade": 7, "valor": 140},
        {"categoria": "Jardinagem", "produto": "Planta", "quantidade": 2, "valor": 60},
        {"categoria": "Jardinagem", "produto": "Ferramentas", "quantidade": 1, "valor": 100}
    ]

    categorias_dict = {}

    # Processar cada entrada
    for item in entrada:
        nome_categoria = item["categoria"]
        produto = item["produto"]
        valor = item["valor"]  # Agora usamos diretamente o valor fornecido

        venda = Venda(produto, valor)

        # Verificar se a categoria já existe, senão cria uma nova
        if nome_categoria not in categorias_dict:
            categorias_dict[nome_categoria] = Categoria(nome_categoria)

        # Adicionar a venda à categoria existente
        categorias_dict[nome_categoria].adicionar_venda(venda)
    
    # Exibir os totais de vendas por categoria
    for nome_categoria, categoria in categorias_dict.items():

        total = categoria.total_vendas()
        print(f"Vendas em {categoria.nome}: {total:.1f}")

if __name__ == "__main__":
    main()
