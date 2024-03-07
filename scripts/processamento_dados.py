import json
import csv

class Dados:
    def __init__(self, path, tipo_dados):
        self._path = path
        self._tipo_dados = tipo_dados
        self._dados = self.leitura_dados()
        self._nome_colunas = self.get_columns()
        self._qtd_dados = len(self._dados)

    def __str__(self) -> str:
        return f"<Dados tipo='{self._tipo_dados}'>"
    
    def leitura_json(self):
        # Lendo os arquicos json
        with open(file=self._path, mode='r') as f:
            dados_json = json.load(f)

        return dados_json

    def leitura_csv(self):
        # Lendo dados em csv, já transformando em dicionário.
        dados_csv = []
        with open(file=self._path, mode='r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                dados_csv.append(row)
        return dados_csv

    def leitura_dados(self):
        dados = []
        if self._tipo_dados == 'csv':
            dados = self.leitura_csv()
        elif self._tipo_dados == 'json':
            dados = self.leitura_json()
        elif self._tipo_dados == 'list':
            dados = self._path
            self._path = 'lista em memoria'

        return dados
    
    def get_columns(self):

        return list(self._dados[-1].keys())
    
    def rename_columns(self, key_mapping):
        # Substituindo as velhas chaves, pelas novas chaves
        new_dados = []

        for old_dict in self._dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)

        self._dados = new_dados
        self._nome_colunas = self.get_columns()

    def join(list_list):
        combined_list = []
        for list in list_list:
            combined_list.extend(list._dados)

        return Dados(combined_list, 'list')

    def transformando_dados_tabela(self):
        # Transformando os dados em uma lista de lista (formato de tabela)
        dados_combinados_tabela = [self._nome_colunas]

        for row in self._dados:
            linha = []
            for coluna in self._nome_colunas:
                linha.append(row.get(coluna, 'Indisponível'))

            dados_combinados_tabela.append(linha)
        return dados_combinados_tabela
    
    def salvando_dados(self, path):
        dados_combinados_tabela = self.transformando_dados_tabela()

        with open(path, 'w') as f:
            writer = csv.writer(f)

            writer.writerows(dados_combinados_tabela)



