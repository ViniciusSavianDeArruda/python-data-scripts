import pyautogui
import time  # importa a biblioteca pyautogui e time serve para pausas
import pandas as pd # importa a biblioteca pandas para manipulação de dados

pyautogui.PAUSE = 0.2  # pausa menor em cada comando (mais rápido)

# pyautogui.click -> clicar em algum lugar
# pyautogui.write -> escrever algo
# pyautogui.press -> apertar alguma tecla


# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o navegador e digitar o site
pyautogui.press("win")  # abre o menu iniciar
pyautogui.write("chrome")  # escreve "chrome" para buscar o navegador
pyautogui.press("enter")  # confirma a abertura
time.sleep(2)  # espera o navegador abrir (reduzido)

# Clicar no perfil do Chrome (ajuste as coordenadas para a sua tela)
pyautogui.click(x=983, y=600)  # troque pelas coordenadas corretas
time.sleep(1)  # reduzido

# Digitar o site do sistema e abrir
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1)  # reduzido


# Passo 2: Fazer Login
pyautogui.click(x=863, y=406)  # clicar no campo email (ajuste coordenadas)
pyautogui.write("vini.arruda@gmail.com")

# Preencher o campo senha
pyautogui.press("tab")  # vai para o campo senha
pyautogui.write("Hashtag@123")

# Confirmar login
pyautogui.press("enter")


# Passo 3: Importar a base de dados
# (aqui você vai colocar os cliques e comandos para importar os dados)
tabela = pd.read_csv("aula1/produtos.csv")  # ler a base de dados

print(tabela)

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:  # para cada linha na tabela

    pyautogui.click(x=871, y=293)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])

    if obs  != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")



pyautogui.click(x=871, y=293)

pyautogui.scroll(10000)


# Observação:
# Para instalar o pyautogui -> pip install pyautogui
