# Aula 02 - Análise de Dados 📊

Nesta aula trabalhamos com análise exploratória de uma base de cancelamentos de clientes (`cancelamentos_sample.csv`). O objetivo foi entender motivos de cancelamento por meio de contagens, percentuais e visualizações.

### O que foi feito
- Carregar a base com **pandas**.
- Inspecionar dados com `info()` e `display()`.
- Tratar dados (remoção de colunas irrelevantes e linhas nulas).
- Análises iniciais: `value_counts()` e percentuais.
- Visualizações: histogramas por coluna com **plotly.express** para comparar clientes que cancelaram e os que não cancelaram.

### Dicas práticas
- Executar as células na ordem: leitura → tratamento → análise → gráficos.
- Se o notebook acusar variáveis indefinidas, provavelmente faltou rodar a célula de leitura.
- Para arquivos grandes, considerar usar Git LFS.

---

## Objetivo
Identificar fatores que impactam o cancelamento de clientes usando a base `cancelamentos_sample.csv`.

---

## Passos realizados
1. Importar bibliotecas: `pandas`, `plotly.express`.
2. Carregar a base de dados:
```python
import pandas as pd

data_frame = pd.read_csv("cancelamentos_sample.csv")
```
3. Inspecionar a base:
```python
display(data_frame)
data_frame.info()
```
4. Tratar dados:
- Remover colunas irrelevantes, ex.: `CustomerID`.
- Remover linhas com valores nulos:
```python
data_frame = data_frame.drop(columns="CustomerID")
data_frame = data_frame.dropna()
```
5. Análises iniciais:
```python
# contagem de cancelamentos
display(data_frame["cancelou"].value_counts())
# em percentual
display(data_frame["cancelou"].value_counts(normalize=True))
```
6. Visualizações com Plotly:
```python
import plotly.express as px
# gráfico para cada coluna (exceto a coluna alvo)
for coluna in data_frame.columns:
	if coluna == "cancelou":
		continue
	grafico = px.histogram(data_frame, x=coluna, color="cancelou")
	grafico.show()
```

---

## Comandos úteis (PowerShell)
- Instalar dependências:
```powershell
pip install pandas plotly jupyterlab
```
- Rodar notebook (jupyter lab):
```powershell
jupyter lab
```

---

## Observações e dicas
- Execute as células na ordem para evitar variáveis indefinidas.
- Se o Pylance apontar `reportUndefinedVariable` em notebooks, isso é apenas um aviso estático (execute as células para validar).
- Para arquivos grandes (>50MB), considere Git LFS.

---

