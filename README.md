# Python Data Scripts

Repositório de estudos com scripts Python desenvolvidos durante o curso **Jornada Python (Hashtag Treinamentos)**, cobrindo automação, análise de dados e desenvolvimento web.

## 📁 Projetos

### 🤖 [01 — Automação de Cadastro](./01-automacao-cadastro)
Script de automação com **PyAutoGUI** para cadastro em massa de produtos em sistema web, lendo dados de arquivo CSV.

**Stack:** Python · PyAutoGUI · Pandas

### 📊 [02 — Análise de Dados](./02-analise-dados)
Análise exploratória de base com ~881 mil registros de cancelamentos de clientes, identificando padrões e fatores associados ao churn.

**Stack:** Python · Pandas · Plotly · Jupyter

### 🌐 [03 — Desenvolvimento Web](./03-web)
Projetos web com integração de IA (ChatBot com OpenAI + Streamlit) e comunicação em tempo real (Chat com Flask + WebSockets).

**Stack:** Python · Streamlit · Flask · OpenAI API · WebSockets

## 🚀 Como usar

Cada projeto é independente e possui seu próprio `README.md` com instruções específicas:

```bash
cd 01-automacao-cadastro       # ou 02-analise-dados, 03-web
pip install -r requirements.txt
```

## 🛠️ Tecnologias gerais

- **Python 3.12**
- **Análise de dados:** Pandas, Plotly, Jupyter Notebook
- **Automação:** PyAutoGUI
- **Web:** Streamlit, Flask, Flask-SocketIO
- **Integrações:** OpenAI API

## 🔧 Refatorações e melhorias

O código original dos projetos foi **refatorado e aprimorado por conta** ao longo do estudo, com as seguintes melhorias:

- **Reorganização em estrutura modular** — separação em pastas `src/` e `data/` para melhor organização e legibilidade
- **Uso de variáveis de ambiente** — chaves de API (como OpenAI) removidas do código-fonte e movidas para `os.getenv()`, seguindo boas práticas de segurança
- **Versão demonstrativa** — criação de arquivos `demo.py` para permitir testes sem consumo de APIs pagas
- **Documentação profissional** — READMEs reescritos com foco em objetivo, uso e execução dos projetos
- **Nomes padronizados** — renomeação de arquivos (ex: `auxiliar.py` → `helpers.py`) seguindo convenções mais claras
- **Git LFS** — arquivos CSV grandes versionados via Git Large File Storage
- **Limpeza dos notebooks** — remoção das saídas dos notebooks Jupyter para reduzir tamanho e melhorar apresentação no GitHub

## 📚 Contexto

Repositório de estudos práticos em Python, desenvolvido a partir dos fundamentos aprendidos no curso Jornada Python (Hashtag Treinamentos) e adaptado com melhorias próprias de organização, segurança e documentação.
