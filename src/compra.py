from src.arquivo_csv import salvar_produtos, gerar_relatorio_estoque, gerar_relatorio_vendas
from src.produto import imprimir_produtos


def adicionar_ao_carrinho(produtos:dict, carrinho:list)->list:
    """
        Adiciona produtos ao carrinho de compras, com base no estoque disponível

        Parâmtros:
        produtos(dict): Dicionário de produtos disponíveis, onda a chave é o ID do produto e o valor é um dicionário com as informações do produto
        carrinho(list): Lista de dicionários representando o carrinho de compras, contendo produtos adicionais 

        Return:
        list: Retorna a lista atualizada do carrinho de compras com os produtos adicionados
    """ 
    while True:
        imprimir_produtos(produtos)
        id_produto = input('Digite o ID do produto que deseja adicionar ao carrinho: ')
        if id_produto in produtos:
            try:
                quantidade = int(input('Digite a quantidade desejada: '))
                if quantidade <= produtos[id_produto]['quantidade_estoque']:
                    carrinho.append({
                        'id': id_produto,
                        'nome': produtos[id_produto]['nome'],
                        'quantidade': quantidade,
                        'preco_unitario': produtos[id_produto]['preco']
                    })
                    print('Produto adicionado ao carrinho.')
                else:
                    print('Quantidade desejada excede o estoque disponível.')
            except ValueError:
                print("Por favor, insira um número válido para a quantidade.")
        else:
            print('Produto não encontrado.')

        confirmar = input("Deseja adicionar mais produtos ao carrinho? (s/n): ").strip().lower()
        if confirmar != 's':
            break
    return carrinho
 

def excluir_do_carrinho(carrinho:list)->list:
    """
        Remove um produto do carrinho de compras com base no ID do produto

        Parâmetros:
        carrinho(list): Uma lista de dicionários representando o carrinho de compras, contendo produtos adicionados

        Return:
        list: Retorna a lista atualizada do carrinho após a remoção do produto

    """
    if not carrinho:
        print("O carrinho está vazio.")
        return carrinho
    id_produto = input('Digite o ID do produto que deseja remover do carrinho: ')
    carrinho = list(filter(lambda item: item['id'] != id_produto, carrinho))
    print('Produto removido do carrinho.')
    return carrinho


def alterar_quantidade_carrinho(carrinho:list)->list:
    """
    Altera a quantidade de um produto no carrinho de compras com base no ID do produto

    Parâmetros:
    carrinho(list): Lista de dicionários representando o carrinho de compras, contendo produtos e suas respectivas quantidades

    Return: 
    list: Retorna a lista atualizada do carrinho após a alteração da quantidade de um produto 
    """
    if not carrinho:
        print("O carrinho está vazio.")
        return carrinho
    id_produto = input('Digite o ID do produto cuja quantidade deseja alterar: ')
    for item in carrinho:
        if item['id'] == id_produto:
            try:
                nova_quantidade = int(input('Digite a nova quantidade: '))
                if nova_quantidade <= 0:
                    print("Quantidade inválida.")
                else:
                    item['quantidade'] = nova_quantidade
                    print('Quantidade atualizada.')
                return carrinho
            except ValueError:
                print("Por favor, insira um número válido para a nova quantidade.")
    print('Produto não encontrado no carrinho.')
    return carrinho


def visualizar_carrinho(carrinho:list, produtos:dict)->list:
    """
    Exibe o carrinho de compras, permitindo que o usuário visualize os produtos, exclua produtos ou altere suas quantidades

    Parâmetros:
    carrinho(list): Lista de dicionários representando o carrinho de compras, contendo produtos e suas respectivas quantidades
    produtos(dict): Dicionários de produtos disponíveis, onde a chave é o ID do produto e o valor é um dicionário com as informações do produto

    Return:
    lits: Retorna a lista atualizada do carrinho após as possíveis modificações feitas pelo usuário
    """
    if not carrinho:
        print("O carrinho está vazio.")
    else:
        while True:
            print("Carrinho de Compras:")
            total = 0
            for item in carrinho:
                valor_total = item['quantidade'] * item['preco_unitario']
                total += valor_total
                print(f"{item['nome']} - Quantidade: {item['quantidade']}, Preço Unitário: {item['preco_unitario']:.2f}, Valor Total: {valor_total:.2f}")
            print(f"Total da compra: {total:.2f}")
            print("1 - Excluir produto do carrinho")
            print("2 - Alterar quantidade de produto no carrinho")
            print("3 - Sair")
            
            sub_opcao = input("Escolha uma opção: ")
            
            if sub_opcao == '1':
                carrinho = excluir_do_carrinho(carrinho)
            elif sub_opcao == '2':
                carrinho = alterar_quantidade_carrinho(carrinho)
            elif sub_opcao == '3':
                print("Saindo do carrinho...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
    
    return carrinho


def finalizar_compra(produtos:dict, carrinho:list)->list:
    """
    Finaliza a compra dos itens no carrinho, atualiza o estoque dos produtos e gera relatórios de vendas e estoque

    Parâmetros:
    produtos(dict): Dicionário representando os produtos disponíveis, onde a chave é o ID do produto e o valor é um dicionário com as informações do produto
    carrinho(list): Lista de dicionários representando o carrinho de compras, contendo produtos e suas respectivas quantidades

    Return 
    list: Retorna a lista automatizada do carrinho, que será esvaziada após a finalização da compra
    """
    if not carrinho:
        print("O carrinho está vazio.")
        return carrinho
    
    confirmar = input("Deseja concretizar a compra? (s/n): ").strip().lower()
    if confirmar == 's':
        detalhes_venda = []
        for item in carrinho:
            id_produto = item['id']
            if produtos[id_produto]['quantidade_estoque'] >= item['quantidade']:
                produtos[id_produto]['quantidade_estoque'] -= item['quantidade']
                detalhes_venda.append({
                    'nome': item['nome'],
                    'quantidade_vendida': item['quantidade'],
                    'preco_unitario': item['preco_unitario'],
                    'valor_total': item['quantidade'] * item['preco_unitario']
                })
            else:
                print(f"Quantidade do produto {item['nome']} não disponível no estoque.")
        gerar_relatorio_vendas(detalhes_venda)
        gerar_relatorio_estoque(produtos)
        salvar_produtos(produtos)
        print("Compra finalizada com sucesso.")
        carrinho.clear()
    else:
        print("Compra cancelada.")
    return carrinho
