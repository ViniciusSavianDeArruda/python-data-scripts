# ChatBot Demo - Funciona sem API Key da OpenAI
# Este arquivo demonstra a interface do chatbot sem conectar com a API real

import streamlit as st
import random
import time

st.write("### 🤖 ChatBot Demo (Versão de Demonstração)")
st.info("💡 Este é um demo do ChatBot. Para usar com IA real, configure sua chave da OpenAI no arquivo main.py")

# Respostas predefinidas para demonstração
respostas_demo = [
    "Interessante! Pode me contar mais sobre isso?",
    "Entendi. Como posso te ajudar com isso?",
    "Ótima pergunta! Vou pensar sobre isso...",
    "Hmm, deixe-me processar essa informação.",
    "Essa é uma perspectiva muito interessante!",
    "Claro! Posso explicar melhor sobre esse tópico.",
    "Você tem razão, é importante considerar isso.",
    "Excelente observação! O que você acha de...",
]

# session_state = memoria do streamlit
if not "lista_mensagens_demo" in st.session_state:
    st.session_state["lista_mensagens_demo"] = []

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens_demo"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui (Demo)")

if mensagem_usuario:
    # Exibir mensagem do usuário
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens_demo"].append(mensagem)

    # Simular "pensamento" da IA
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("🤔 Pensando...")
        time.sleep(1)
        
        # Resposta simulada
        resposta_ia = random.choice(respostas_demo)
        message_placeholder.markdown(resposta_ia)

    # Salvar resposta da IA
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens_demo"].append(mensagem_ia)

# Instruções na barra lateral
with st.sidebar:
    st.write("### 📚 Como usar:")
    st.write("1. **Demo**: Execute `streamlit run demo.py`")
    st.write("2. **IA Real**: Configure API key e execute `streamlit run main.py`")
    st.write("3. **Chat Web**: Execute `python main.py` no projeto2")
    
    st.write("### 🔧 Configuração:")
    st.code('set OPENAI_API_KEY=sua_chave_aqui', language='bash')