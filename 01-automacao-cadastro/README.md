# Automação de Cadastro de Produtos

Script de automação em Python para cadastro em massa de produtos em sistema web, utilizando PyAutoGUI para simular interações do usuário e Pandas para ler dados de um arquivo CSV.

## 🎯 Objetivo

Automatizar a tarefa repetitiva de cadastrar múltiplos produtos em uma interface web, eliminando o trabalho manual de preenchimento formulário por formulário. O script lê os dados de um CSV e executa todo o fluxo (login, navegação e cadastro) de forma automatizada.

## 🔧 Como funciona

1. **Leitura dos dados** — Carrega o arquivo `produtos.csv` com Pandas
2. **Login automatizado** — Abre o navegador e realiza login no sistema
3. **Cadastro em loop** — Para cada linha do CSV, preenche o formulário e envia
4. **Retorno ao início** — Após cada cadastro, retorna à tela inicial para o próximo

## 🛠️ Tecnologias

- **Python 3.12**
- **PyAutoGUI** — automação de interface gráfica (mouse e teclado)
- **Pandas** — leitura e manipulação de arquivos CSV

## 📁 Estrutura

```
01-automacao-cadastro/
├── data/
│   └── produtos.csv        # Base de dados dos produtos
├── src/
│   ├── automacao.py        # Script principal
│   └── helpers.py          # Funções auxiliares (ex: captura de coordenadas)
├── requirements.txt
└── README.md
```

## 🚀 Como executar

**1. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**2. Ajuste as coordenadas** de tela no arquivo `src/automacao.py` conforme o sistema alvo e a resolução do seu monitor.

**3. Abra o sistema alvo** na tela onde a automação deve rodar.

**4. Execute o script:**

```bash
python src/automacao.py
```

## ⚠️ Observações importantes

- **Não mova o mouse** durante a execução — a automação usa coordenadas fixas
- **Coordenadas de tela** variam por resolução — use `helpers.py` para capturá-las no seu ambiente
- **Teste com poucos registros** antes de rodar em massa
- Para **abortar** durante a execução, mova o mouse para o canto superior esquerdo da tela

## 📚 Contexto

Projeto desenvolvido durante o curso **Jornada Python (Hashtag Treinamentos)**, mantido como estudo prático de automação de tarefas com Python.
