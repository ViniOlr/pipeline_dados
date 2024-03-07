from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinados = 'data_processed/dados_combinados.csv'

dados_empresa_a = Dados(path_json, 'json')
dados_empresa_b = Dados(path_csv, 'csv')

# Associando as colunas do csv com as do json
key_mapping = {
    'Nome do Item' : 'Nome do Produto',
    'Classificação do Produto' : 'Categoria do Produto',
    'Valor em Reais (R$)':'Preço do Produto (R$)',
    'Quantidade em Estoque':'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda':'Data da Venda'
}

dados_empresa_b.rename_columns(key_mapping)

dados_fusao = Dados.join([dados_empresa_a, dados_empresa_b])

dados_fusao.salvando_dados(path_dados_combinados)