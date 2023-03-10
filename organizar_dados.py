import os
import pandas as pd
import plotly.express as px

class OrganizarDados():
    """Faz o tratamento dos dados e exibe as informações solicitadas para análise"""
    def __init__(self, filename):
        """Inicializa as informações necessárias para a análise"""
        self.filename = filename
        self.lista_de_arquivos = os.listdir(self.filename)
        self.tabela_total = pd.DataFrame()

    def percorrer_arquivos(self):
        """Percorre arquivo por arquivo dentro do diretório e faz a leitura dos dados """
        for arquivo in self.lista_de_arquivos:
            if "Vendas" in arquivo:
                self.tabela = pd.read_csv(self.filename+'/'+arquivo)
                self.tabela_total = pd.concat([self.tabela, self.tabela_total], ignore_index=True)

    def quantidade_vendas_produto(self):
        """Gera uma tabela e um gráfico contendo o total de vendas realizadas por produto """
        self.percorrer_arquivos()
        self.tabela_produtos = self.tabela_total.groupby('Produto').sum()
        self.tabela_qtdvendas_produto = self.tabela_produtos[['Quantidade Vendida']]\
            .sort_values(by='Quantidade Vendida', ascending=False)
        print(self.tabela_qtdvendas_produto)
        self.grafico = px.bar(self.tabela_qtdvendas_produto, x=self.tabela_qtdvendas_produto.index,
                              y='Quantidade Vendida')
        self.grafico.show()

    def faturamento_produto(self):
        """Gera uma tabela e um gráfico contendo o total de faturamento por produto """
        self.percorrer_arquivos()
        self.tabela_total['Faturamento'] = self.tabela_total['Quantidade Vendida'] * self.tabela_total['Preco Unitario']
        self.tabela_produtos = self.tabela_total.groupby('Produto').sum()
        self.tabela_faturamento_produto = self.tabela_produtos[['Faturamento']]\
            .sort_values(by='Faturamento', ascending=False)
        print(self.tabela_faturamento_produto)
        self.grafico = px.bar(self.tabela_faturamento_produto, x=self.tabela_faturamento_produto.index, y='Faturamento')
        self.grafico.show()

    def quantidade_vendas_loja(self):
        """Gera uma tabela e um gráfico contendo o total de vendas realizadas por loja """
        self.percorrer_arquivos()
        self.tabela_loja = self.tabela_total.groupby('Loja').sum()
        self.tabela_qtdvendas_loja = self.tabela_loja[['Quantidade Vendida']]\
            .sort_values(by='Quantidade Vendida', ascending=False)
        print(self.tabela_qtdvendas_loja)
        self.grafico = px.bar(self.tabela_qtdvendas_loja, x=self.tabela_qtdvendas_loja.index, y='Quantidade Vendida')
        self.grafico.show()

    def faturamento_loja(self):
        """Gera uma tabela e um gráfico contendo o total de faturamento por produto """
        self.percorrer_arquivos()
        self.tabela_total['Faturamento'] = self.tabela_total['Quantidade Vendida'] * self.tabela_total['Preco Unitario']
        self.tabela_loja = self.tabela_total.groupby('Loja').sum()
        self.tabela_faturamento_loja = self.tabela_loja[['Faturamento']] \
            .sort_values(by='Faturamento', ascending=False)
        print(self.tabela_faturamento_loja)
        self.grafico = px.bar(self.tabela_faturamento_loja, x=self.tabela_faturamento_loja.index, y='Faturamento')
        self.grafico.show()










