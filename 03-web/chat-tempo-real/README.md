# Chat em Tempo Real

Sistema de chat web com comunicação bidirecional em tempo real, desenvolvido com **Flask** e **Socket.IO**, permitindo múltiplos usuários conversarem simultaneamente através de WebSockets.

## 🎯 Objetivo

Implementar um chat funcional que troca mensagens em tempo real entre múltiplos usuários conectados, aplicando conceitos de comunicação bidirecional com WebSockets, sem necessidade de atualização da página.

## 🔧 Como funciona

- **Backend:** servidor Flask com Socket.IO gerencia conexões WebSocket
- **Frontend:** interface HTML/JavaScript conecta ao servidor via WebSocket
- **Mensagens:** transmitidas em broadcast para todos os usuários conectados em tempo real
- **Persistência:** mensagens ficam apenas na sessão (não há banco de dados)

## ⚙️ Funcionalidades

- Chat em tempo real via WebSockets
- Suporte a múltiplos usuários simultâneos
- Interface responsiva
- Broadcast de mensagens para todos os conectados
- Identificação por nickname

## 🛠️ Tecnologias

- **Python 3.12**
- **Flask** — framework web minimalista
- **Flask-SocketIO** — WebSockets para Flask
- **HTML / CSS / JavaScript** — frontend do chat

## 📁 Estrutura

```
chat-tempo-real/
├── src/
│   └── main.py             # Servidor Flask + Socket.IO
├── templates/
│   ├── homepage.html       # Página inicial (entrada)
│   └── index.html          # Interface do chat
├── requirements.txt
└── README.md
```

## 🚀 Como executar

**1. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**2. Execute o servidor:**

```bash
python src/main.py
```

**3. Acesse no navegador:**

```
http://localhost:5000
```

**4. Para testar múltiplos usuários** — abra o mesmo endereço em várias abas do navegador (ou em dispositivos diferentes na mesma rede).

## 📝 Fluxo de uso

1. Acesse `http://localhost:5000`
2. Informe um nickname
3. Envie mensagens que serão transmitidas em tempo real
4. Abra em outras abas para simular usuários adicionais

## 📚 Contexto

Projeto desenvolvido durante o curso **Jornada Python (Hashtag Treinamentos)**, mantido como estudo prático de comunicação em tempo real com WebSockets em Python.
