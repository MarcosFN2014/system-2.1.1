# Sistema de Gerenciamento de Inventário para Loja Virtual

## 1- Descrição

Este repositório contém o código-fonte do projeto de desenvolvimento de um **Sistema de Gerenciamento de Inventário** para uma loja virtual. O sistema permite o cadastro, atualização, exclusão e listagem de produtos, além de gerenciar vendas e gerar relatórios detalhados em formato CSV.

## Objetivo

O objetivo deste projeto é construir um sistema robusto e eficiente, capaz de lidar com erros de forma elegante, enquanto oferece funcionalidades completas para o gerenciamento de inventário.

## Funcionalidades

- **Cadastro de Produtos**: Adicionar novos produtos ao inventário.
- **Atualização de Produtos**: Modificar as informações de produtos existentes.
- **Exclusão de Produtos**: Remover produtos do inventário.
- **Listagem de Produtos**: Visualizar todos os produtos cadastrados.
- **Gestão de Vendas**: Registrar e processar vendas de produtos.
- **Geração de Relatórios**: Gerar relatórios detalhados em formato CSV sobre o estoque e vendas.

## Requisitos
Python 3
Nenhuma biblioteca externa adicional é necessária.

## Como Rodar o Projeto
- 1- Clone o repositório ou baixe os arquivos do projeto.
- 2- Navegue até a pasta do projeto em seu terminal.
- 3- Execute o arquivo main.py
- **python main.py**
- 4- O menu interativo será exibido no terminal, e você poderá navegar pelas opções


## 2. Documentação das Funções
## menu.py
`menu()`
Exibe o menu principal do sistema, carrega os produtos e gerencia as operações do sistema. O usuário pode cadastrar, listar, alterar e remover produtos, além de gerenciar carrinhos de compras e gerar relatórios.

## produto.py
`gerar_id`(produtos)
Gera um novo ID para o produto, incrementando o último ID existente.

**Parâmetro:** produtos - Dicionário de produtos.
**Retorno:** String com o novo ID no formato de quatro dígitos.

`selecionar_categoria`(categorias)
Exibe as categorias de produtos disponíveis e solicita ao usuário a seleção de uma.

**Parâmetro:** categorias - Lista de categorias disponíveis.
**Retorno**: Categoria selecionada pelo usuário.

`cadastrar_produto`(produtos)
Solicita informações do produto ao usuário e o adiciona ao dicionário de produtos.

**Parâmetro:** produtos - Dicionário onde o novo produto será adicionado.

`alterar_produto`(produtos)
Permite a alteração das informações de um produto existente.

**Parâmetro:** produtos - Dicionário de produtos a ser atualizado.

`imprimir_produtos`(produtos)
Exibe todos os produtos cadastrados com seus detalhes.

**Parâmetro:** produtos - Dicionário de produtos a serem exibidos.

`remover_produto`(produtos)
Remove um produto do dicionário de produtos.

**Parâmetro:** produtos - Dicionário de produtos.

## carrinho.py
`adicionar_ao_carrinho`(produtos, carrinho)
Adiciona um produto ao carrinho de compras.

**Parâmetros:**
produtos - Dicionário de produtos disponíveis.
carrinho - Lista que representa o carrinho de compras.
**Retorno:** Lista atualizada do carrinho.

`excluir_do_carrinho`(carrinho)
Remove um produto do carrinho de compras.

**Parâmetro:** carrinho - Lista do carrinho de compras.
Retorno: Lista atualizada do carrinho.

`alterar_quantidade_carrinho`(carrinho)
Permite alterar a quantidade de um produto no carrinho de compras.

**Parâmetro:** carrinho - Lista do carrinho de compras.
**Retorno**: Lista atualizada do carrinho.

`visualizar_carrinho`(carrinho, produtos)
Exibe o conteúdo do carrinho e permite ao usuário excluir ou alterar a quantidade de produtos.

**Parâmetros:**
carrinho - Lista do carrinho de compras.
produtos - Dicionário de produtos disponíveis.
**Retorno**: Lista atualizada do carrinho.

`finalizar_compra`(produtos, carrinho)
Processa a compra, atualiza o estoque e gera um relatório de vendas.

**Parâmetros:**
produtos - Dicionário de produtos disponíveis.
carrinho - Lista do carrinho de compras.
**Retorno:** Lista atualizada do carrinho (vazia após a compra).

# relatorio.py
`gerar_relatorio_vendas`(detalhes_venda)
Gera um relatório em CSV com os detalhes das vendas realizadas.

**Parâmetro:** 
`detalhes_venda` - Lista com os detalhes das vendas.

`gerar_relatorio_estoque(produtos)`
Gera um relatório em CSV com o estado atual do estoque.

**Parâmetro:** produtos - Dicionário de produtos cadastrados.

`carregar_produtos()`
Carrega os produtos do arquivo CSV `produtos.csv` e retorna um dicionário de produtos.

**Retorno:** Dicionário onde a chave é o ID do produto e o valor é outro dicionário com os dados do produto.

`salvar_produtos(produtos)`
Salva o dicionário de produtos no arquivo CSV `produtos.csv`.

**Parâmetro:** produtos - Dicionário de produtos a ser salvo.

## 3- Exemplo de Uso
Ao executar o programa, o menu principal será exibido:
---------------------------
        New System
---------------------------
- 1 - Cadastrar Novo Produto
- 2 - Listar Produtos Cadastrados
- 3 - Atualizar Cadastro de Produtos
- 4 - Remover Cadastro de Produto
- 5 - Adicionar ao Carrinho de Compras
- 6 - Visualizar Carrinho
- 7 - Finalizar Compra
- 8 - Gerar Relatório de Estoque
- 9 - Gerar Relatório de Vendas
- 10 - Sair
- Digite o número da opção desejada e siga as instruções.

## Tecnologias Utilizadas

**Linguagem de Programação**: Python

## Amostragem

## Autores

- **Giovanni Ornellas**  
  [GitHub](https://github.com/Giovanni-Ornellas) | [LinkedIn](https://www.linkedin.com/in/giovanni-ornellas-419610227/)

- **Matheus Gouveia**  
  [GitHub](https://github.com/gouveiamdb) | [LinkedIn](https://www.linkedin.com/in/matheus-gouveia-387a19258/)

- **Murilo Silva**  
  [GitHub](https://github.com/Mugah) | [LinkedIn](https://www.linkedin.com/in/murilo-silva-bb2741a1)

- **Marcos Carvalho**
  [GitHub](https://github.com/MarcosFN2014) | [LinkedIn](https://www.linkedin.com/in/marcos-carvalho-8173a2241/)