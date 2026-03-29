import pandas as pd
tabela = pd.read_csv("produtos.csv", sep="\t")
print(tabela.columns)