#Criando Classes para Dados de Vendas
# Descrição
# Você está desenvolvendo um sistema para gerenciar dados de vendas que serão posteriormente importados para o Power BI. Você tem a estrutura de duas classes, Venda e Relatorio, já definidas. Sua tarefa é implementar partes específicas do código dentro dessas classes.

# Classe Venda:

# Já está definida e contém as informações sobre uma venda, como produto, quantidade e valor.

# Classe Relatorio:

# Você precisa implementar o método adicionar_venda, que deve verificar se o objeto passado é uma instância da classe Venda antes de adicioná-lo à lista de vendas.

# Também, no método calcular_total_vendas, você deve calcular o total de vendas multiplicando a quantidade pelo valor de cada venda adicionada ao relatório.

# Função main:
# Você deverá implementar a lógica para exibir o total de vendas utilizando o método calcular_total_vendas da classe Relatorio.

# Entrada
# A entrada consiste em dados de vendas com as seguintes colunas:

# Produto (string)
# Quantidade (inteiro)
# Valor (decimal)
# Saída
# A saída é o total de vendas calculado pela classe Relatorio.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.

# Entrada	                  Saída
# Notebook  3  1500.00
# Mouse    10  50.00        5500.0
# Teclado   5  100.00	      

class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # TODOS: Verifique se o objeto passado é uma instância da classe Venda.
        # Isso ajuda a garantir que apenas vendas válidas sejam adicionadas ao relatório.
        if isinstance(venda, Venda):
            self.vendas.append(venda)
        

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            # TODOS: Calcule o total de vendas baseado nas vendas adicionadas:
            # O cálculo deve multiplicar a quantidade pelo valor de cada venda e somar ao total.
            total += venda.quantidade * venda.valor
        return total
    
    def exibir_relatorio(self):
        print("Relatório de Vendas:")
        for venda in self.vendas:
            print(f"Produto: {venda.produto}, Quantidade: {venda.quantidade}, Valor Unitário: {venda.valor}, Total: {venda.quantidade * venda.valor:.2f}")


def main():
    relatorio = Relatorio()
    vendas = [
        Venda("Notebook", 2, 800.00),
        Venda("Mouse", 1, 120.00),
        Venda("Teclado", 4, 75.00)
    ]
    for venda in vendas:
        relatorio.adicionar_venda(venda)

    
    # Exibir o relatório de vendas
    relatorio.exibir_relatorio()
    
    # TODOS: Exiba o total de vendas usando o método calcular_total_vendas.
    # Utilize o método `calcular_total_vendas` da classe `Relatorio` para mostrar o total acumulado das vendas.
    # Calcular e exibir o total de vendas
    total = relatorio.calcular_total_vendas()
    print(f"\nTotal de Vendas: R$ {total:.2f}")

if __name__ == "__main__":
    main()