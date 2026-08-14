# Análise de Cancelamentos de Clientes

Análise exploratória de uma base de dados com aproximadamente **881 mil registros** de clientes, com o objetivo de identificar padrões e fatores associados ao cancelamento de contratos (churn).

## 🎯 Objetivo

Investigar quais características e comportamentos estão mais associados aos clientes que cancelaram seus serviços, gerando insights que possam auxiliar a redução da taxa de cancelamento.

## 🔍 Etapas da análise

1. **Carregamento** da base de dados com Pandas
2. **Inspeção inicial** — estrutura, tipos de dados e valores nulos
3. **Tratamento dos dados**:
   - Remoção de colunas irrelevantes (ex: `CustomerID`)
   - Remoção de linhas com valores nulos
4. **Análise descritiva**:
   - Contagem absoluta de cancelamentos (`value_counts()`)
   - Distribuição percentual (`value_counts(normalize=True)`)
5. **Análise exploratória visual**:
   - Histogramas por coluna, comparando clientes que cancelaram vs. permaneceram
   - Identificação visual de padrões e outliers

## 📊 Dataset

| Arquivo | Descrição | Tamanho |
|---|---|---|
| `cancelamentos.csv` | Base completa | ~881 mil registros (~58MB) |
| `cancelamentos_sample.csv` | Amostra reduzida para testes | ~50k registros |
| `cancelamentos_github.csv` | Amostra para visualização no GitHub | 1000 registros |

**Colunas principais:** idade, sexo, tempo como cliente, ligações ao call center, dias de atraso, tipo de contrato, cancelou (target).

> ⚠️ O arquivo `cancelamentos.csv` é grande e está versionado via **Git LFS**. Execute `git lfs pull` após clonar o repositório para baixá-lo.

## 🛠️ Tecnologias

- **Python 3.12**
- **Pandas** — manipulação e análise de dados
- **Plotly Express** — visualizações interativas
- **Jupyter Notebook** — ambiente de análise

## 🚀 Como executar

**1. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**2. Baixe os dados grandes (Git LFS):**

```bash
git lfs pull
```

**3. Abra o Jupyter:**

```bash
jupyter notebook
```

**4. Abra o notebook** `notebooks/analise_cancelamentos.ipynb` e execute as células na ordem.

## 📈 Principais insights

*Preencher com o que você tirou dos dados. Exemplos possíveis:*

- Clientes com mais de **X dias de atraso** têm forte tendência ao cancelamento
- **Tempo como cliente** curto está associado a maior churn
- **Ligações frequentes ao call center** sinalizam risco de cancelamento
- Clientes com contratos **mensais** cancelam mais que anuais

## 📚 Contexto

Projeto desenvolvido durante o curso **Jornada Python (Hashtag Treinamentos)**, mantido como estudo prático de análise exploratória de dados com Python e Pandas.
