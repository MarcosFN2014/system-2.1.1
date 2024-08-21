import csv

def gerar_relatorio_vendas(detalhes_venda:list)->None:
    """
        Função que gera um arquivo CSV contendo os detalhes de cada venda.

        Parâmetros:
        detalhes_venda (list): lista de dicionários  

        Return:
        None
    """
    try:
        with open('vendas.csv', mode='r', encoding='utf8') as file:
            conteudo_existente = file.read().strip()
    except FileNotFoundError:
        conteudo_existente = ''
    
    with open('vendas.csv', mode='a', newline='', encoding='utf8') as file:
        if not conteudo_existente:
            file.write('Nome,Quantidade Vendida,Preço Unitário,Valor Total\n')
        
        for venda in detalhes_venda:
            linha = f"{venda['nome']},{venda['quantidade_vendida']},{venda['preco_unitario']},{venda['valor_total']}\n"
            file.write(linha)


def gerar_relatorio_estoque(produtos:dict)->None:
    """
        Gera um relatório de estoque e grava os dados no arquivo 'estoque.csv'

        Parâmetros:
        produtos (dict): Um dicionário onde a chave é o ID do produto (int) e o valor é outro dicionário

        Return:
        None
    """
    with open('estoque.csv', mode='w', newline='', encoding='utf8') as file:
        fieldnames = ['ID', 'Nome', 'Categoria', 'Preço', 'Quantidade', 'Descrição']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for id_produto, dados_produto in produtos.items():
            writer.writerow({
                'ID': id_produto,
                'Nome': dados_produto['nome'],
                'Categoria': dados_produto['categorias'],
                'Preço': dados_produto['preco'],
                'Quantidade': dados_produto['quantidade_estoque'],
                'Descrição': dados_produto['descricao']
            })


def carregar_produtos()->None:
    """
        Carrega os produtos a partir de um arquivo CSV e retorna um dicionário de produtos

        Parâmetros:
        None

        Return:
        Um dicionário onde as chaves são os IDs dos produtos (int) e os valores são dicionários 
    """
    produtos = {}
    try:
        with open('produtos.csv', mode='r', newline='', encoding='utf8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    produtos[row['ID']] = {
                        'nome': row['Nome'],
                        'categorias': row['Categoria'],
                        'preco': float(row['Preço']),
                        'quantidade_estoque': int(row['Quantidade']),
                        'descricao': row['Descrição']
                    }
                except ValueError as e:
                    print(f"Erro ao processar a linha {row}: {e}")
    except FileNotFoundError:
        print("Arquivo produtos.csv não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar produtos: {e}")
    return produtos


def salvar_produtos(produtos:dict)->None:
    """ 
        Função que salva os produtos em um arquivo CSV ('produtos.csv'). Caso o arquivo já exista, ele será sobrescrito.

        Parâmetros:
        produtos(dict): Um dicionário onde as chaves são os IDs dos produtos (int) e os valores são dicionários
        
        Return:
        None
    """
    try:
        with open('produtos.csv', mode='r', newline='', encoding='utf8') as file:
            conteudo_existente = file.read().strip()
    except FileNotFoundError:
        conteudo_existente = ''

    with open('produtos.csv', mode='w+', newline='', encoding='utf8') as file:
        fieldnames = ['ID', 'Nome', 'Categoria', 'Preço', 'Quantidade', 'Descrição']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        if not conteudo_existente:
            writer.writeheader()

        for id_produto, dados_produto in produtos.items():
            writer.writerow({
                'ID': id_produto,
                'Nome': dados_produto['nome'],
                'Categoria': dados_produto['categorias'],
                'Preço': dados_produto['preco'],
                'Quantidade': dados_produto['quantidade_estoque'],
                'Descrição': dados_produto['descricao']
            })