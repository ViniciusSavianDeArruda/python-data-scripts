# ChatBot IA

Chatbot conversacional desenvolvido com **Streamlit**, integrado à **API da OpenAI (GPT-4)** para respostas inteligentes em tempo real. Inclui versão demonstrativa que roda sem chave de API.

## 🎯 Objetivo

Criar uma interface de chat web interativa que se comunica com um modelo de linguagem (GPT-4), permitindo conversas naturais através de uma UI simples e responsiva, com memória de contexto durante a sessão.

## 🔧 Como funciona

- **Interface web** construída com Streamlit
- **Comunicação** com a API da OpenAI via chamadas HTTP
- **Histórico de mensagens** mantido durante a sessão do usuário
- **Duas versões disponíveis:**
  - `main.py` — versão completa com integração real à OpenAI
  - `demo.py` — versão demonstrativa que simula respostas (sem consumir a API)

## ⚙️ Funcionalidades

- Interface de chat interativa
- Histórico de conversas na sessão
- Integração com GPT-4
- Respostas em tempo real
- Memória de contexto da conversa
- Versão demo para testes sem custo

## 🛠️ Tecnologias

- **Python 3.12**
- **Streamlit** — framework para interfaces web
- **OpenAI API** — modelo GPT-4

## 📁 Estrutura

```
chatbot-ia/
├── src/
│   ├── main.py         # ChatBot com integração real à OpenAI
│   ├── demo.py         # Versão demonstrativa (sem API key)
│   └── helpers.py      # Funções auxiliares
├── requirements.txt
└── README.md
```

## 🚀 Como executar

**1. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**2. Rode a versão demonstrativa** (recomendado para testes — sem custo, sem API key):

```bash
streamlit run src/demo.py
```

Acesse em: `http://localhost:8501`

**3. Ou rode a versão completa com OpenAI:**

Primeiro, configure sua chave da OpenAI como variável de ambiente:

```powershell
# Windows PowerShell
$env:OPENAI_API_KEY="sua-chave-aqui"
```

```bash
# Linux / macOS
export OPENAI_API_KEY="sua-chave-aqui"
```

Depois execute:

```bash
streamlit run src/main.py
```

## ⚠️ Observações importantes

- **Nunca commite** sua chave da OpenAI no código — sempre use variáveis de ambiente
- A versão `main.py` **consome créditos** da OpenAI a cada mensagem enviada
- Para testes e demonstrações, use `demo.py`
- Certifique-se de que sua chave da OpenAI está ativa em: https://platform.openai.com/api-keys

## 📝 Fluxo de uso

1. Execute o Streamlit com o comando acima
2. Digite sua mensagem no campo de input
3. Pressione Enter ou clique no botão
4. A IA responde em tempo real
5. O histórico da conversa fica mantido durante a sessão

## 📚 Contexto

Projeto desenvolvido durante o curso **Jornada Python (Hashtag Treinamentos)**, mantido como estudo prático de integração com APIs de IA em aplicações web com Streamlit.
