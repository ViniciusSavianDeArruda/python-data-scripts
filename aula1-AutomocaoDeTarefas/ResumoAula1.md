# 🐍 Aula 01 - Automação de Tarefas com Python ⚡

Nesta primeira aula da **Jornada Python**, aprendemos a usar o **PyAutoGUI** para automatizar tarefas no computador e o **Pandas** para ler dados de arquivos CSV.  
O projeto consistiu em abrir o navegador, acessar um sistema online, fazer login automaticamente e cadastrar produtos com base em uma planilha (`produtos.csv`).

O sistema utilizado para o cadastro foi disponibilizado pela própria Hostang e pode ser acessado [neste link](https://dlp.hashtagtreinamentos.com/python/intensivao/login).

---

## 📌 O que foi feito na aula

- Abrir programas automaticamente (Chrome).
- Acessar sites e preencher formulários.
- Fazer login automático com e-mail e senha.
- Ler uma base de dados (`produtos.csv`) com **Pandas**.
- Preencher campos de forma automática no sistema, linha por linha.
- Usar um script auxiliar para capturar coordenadas da tela.

---

## 🚀 Comandos usados

### 🔹 PyAutoGUI

```python
import pyautogui

pyautogui.PAUSE = 0.2          # Define uma pausa entre os comandos
pyautogui.press("enter")       # Aperta uma tecla
pyautogui.write("texto")       # Digita um texto
pyautogui.click(x=100, y=200)  # Clica em uma posição da tela
pyautogui.scroll(1000)         # Rola a tela (positivo = sobe, negativo = desce)
print(pyautogui.position())    # Mostra a posição atual do mouse
```

### 🔹 Time

```python
import time

time.sleep(3)  # Espera X segundos antes de executar o próximo comando
```

### 🔹 Pandas

```python
import pandas as pd

tabela = pd.read_csv("produtos.csv")  # Lê arquivo CSV em formato de tabela
print(tabela)                         # Exibe a tabela

for linha in tabela.index:            # Percorre todas as linhas da tabela
    codigo = tabela.loc[linha, "codigo"]   # Pega valor de uma coluna
    marca = tabela.loc[linha, "marca"]
```

---

## 🔧 Dependências

Antes de rodar os scripts, instale as bibliotecas necessárias:

```bash
pip install pyautogui pandas
```

---

## 🌐 Link do Sistema Utilizado

- [Acessar o sistema para cadastro](https://dlp.hashtagtreinamentos.com/python/intensivao/login)