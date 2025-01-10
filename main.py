import json
from datetime import datetime

class Tarefa:
    def __init__(self, titulo, descricao, data_limite):
        self.titulo = titulo
        self.descricao = descricao
        self.data_limite = datetime.strptime(data_limite, "%Y-%m-%d")

    def __str__(self):
        return f"[Tarefa] {self.titulo} - {self.descricao} (Limite: {self.data_limite.strftime('%d/%m/%Y')})"

class Reuniao:
    def __init__(self, titulo, data, hora, descricao):
        self.titulo = titulo
        self.data = datetime.strptime(data, "%Y-%m-%d")
        self.hora = datetime.strptime(hora, "%H:%M").time()
        self.descricao = descricao

    def __str__(self):
        return f"[Reunião] {self.titulo} - {self.descricao} (Data: {self.data.strftime('%d/%m/%Y')} às {self.hora})"

class Calendario:
    def __init__(self):
        self.tarefas = []
        self.reunioes = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def adicionar_reuniao(self, reuniao):
        self.reunioes.append(reuniao)

    def listar_eventos(self):
        print("\n--- Tarefas ---")
        for tarefa in self.tarefas:
            print(tarefa)
        print("\n--- Reuniões ---")
        for reuniao in self.reunioes:
            print(reuniao)

    def salvar_dados(self, arquivo="dados.json"):
        dados = {
            "tarefas": [
                {
                    "titulo": tarefa.titulo,
                    "descricao": tarefa.descricao,
                    "data_limite": tarefa.data_limite.strftime("%Y-%m-%d"),
                }
                for tarefa in self.tarefas
            ],
            "reunioes": [
                {
                    "titulo": reuniao.titulo,
                    "data": reuniao.data.strftime("%Y-%m-%d"),
                    "hora": reuniao.hora.strftime("%H:%M"),
                    "descricao": reuniao.descricao,
                }
                for reuniao in self.reunioes
            ],
        }
        with open(arquivo, "w") as f:
            json.dump(dados, f, indent=4)

    def carregar_dados(self, arquivo="dados.json"):
        try:
            with open(arquivo, "r") as f:
                dados = json.load(f)
                self.tarefas = [
                    Tarefa(t["titulo"], t["descricao"], t["data_limite"])
                    for t in dados["tarefas"]
                ]
                self.reunioes = [
                    Reuniao(r["titulo"], r["data"], r["hora"], r["descricao"])
                    for r in dados["reunioes"]
                ]
        except FileNotFoundError:
            print("Nenhum dado encontrado. Começando com um calendário vazio.")

class GerenciadorSistema:
    def __init__(self):
        self.calendario = Calendario()
        self.calendario.carregar_dados()

    def menu(self):
        while True:
            print("\n--- Sistema de Gerenciamento ---")
            print("1. Adicionar Tarefa")
            print("2. Adicionar Reunião")
            print("3. Listar Eventos")
            print("4. Salvar e Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                titulo = input("Título da Tarefa: ")
                descricao = input("Descrição: ")
                data_limite = input("Data Limite (AAAA-MM-DD): ")
                tarefa = Tarefa(titulo, descricao, data_limite)
                self.calendario.adicionar_tarefa(tarefa)
            elif opcao == "2":
                titulo = input("Título da Reunião: ")
                data = input("Data (AAAA-MM-DD): ")
                hora = input("Hora (HH:MM): ")
                descricao = input("Descrição: ")
                reuniao = Reuniao(titulo, data, hora, descricao)
                self.calendario.adicionar_reuniao(reuniao)
            elif opcao == "3":
                self.calendario.listar_eventos()
            elif opcao == "4":
                self.calendario.salvar_dados()
                print("Dados salvos. Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema = GerenciadorSistema()
    sistema.menu()
