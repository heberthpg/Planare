# Planare
📅 Sistema de Calendário em Python

Este projeto é um sistema simples de calendário desenvolvido em Python, capaz de gerenciar tarefas e reuniões, com suporte a persistência de dados em arquivo JSON.

Ele é ideal para estudos de Programação Orientada a Objetos (POO), manipulação de datas com datetime e leitura/escrita de arquivos JSON.

🚀 Funcionalidades

✅ Adicionar tarefas com data limite

✅ Adicionar reuniões com data e horário

✅ Remover tarefas e reuniões pelo título

✅ Listar todos os eventos do calendário

✅ Salvar dados em arquivo .json

✅ Carregar dados salvos automaticamente

🧠 Estrutura do Projeto

O sistema é composto por três classes principais:

🔹 Classe Tarefa

Representa uma tarefa com:

Título

Descrição

Data limite

🔹 Classe Reuniao

Representa uma reunião com:

Título

Descrição

Data

Horário

🔹 Classe Calendario

Responsável por:

Armazenar tarefas e reuniões

Gerenciar inclusão e remoção

Listar eventos

Salvar e carregar dados em JSON

📂 Persistência de Dados

Os dados são armazenados no arquivo dados.json no seguinte formato:

{
  "tarefas": [
    {
      "titulo": "Exemplo",
      "descricao": "Descrição da tarefa",
      "data_limite": "2026-01-15"
    }
  ],
  "reunioes": [
    {
      "titulo": "Reunião Exemplo",
      "data": "2026-01-20",
      "hora": "14:00",
      "descricao": "Descrição da reunião"
    }
  ]
}

▶️ Como Usar
1️⃣ Importar as classes
from calendario import Calendario, Tarefa, Reuniao

2️⃣ Criar o calendário
calendario = Calendario()
calendario.carregar_dados()

3️⃣ Adicionar uma tarefa
tarefa = Tarefa(
    "Estudar Python",
    "Revisar POO e JSON",
    "2026-01-20"
)
calendario.adicionar_tarefa(tarefa)

4️⃣ Adicionar uma reunião
reuniao = Reuniao(
    "Reunião de Projeto",
    "2026-01-22",
    "15:30",
    "Alinhar requisitos"
)
calendario.adicionar_reuniao(reuniao)

5️⃣ Listar eventos
for evento in calendario.listar_eventos():
    print(evento)

6️⃣ Salvar dados
calendario.salvar_dados()

🛠 Tecnologias Utilizadas

Python 3

Módulo datetime

Módulo json

📌 Observações

As datas devem seguir o formato YYYY-MM-DD

O horário deve seguir o formato HH:MM

Caso o arquivo dados.json não exista, o sistema inicia vazio

📚 Objetivo Educacional

Este projeto foi desenvolvido com foco em:

Programação Orientada a Objetos

Manipulação de datas e horários


