import tkinter as tk
from tkinter import ttk, messagebox
from logica import Tarefa, Reuniao, Calendario

class GerenciadorGUI:
    def __init__(self, root):
        self.calendario = Calendario()
        self.calendario.carregar_dados()

        self.root = root
        self.root.title("Gerenciador de Tarefas e Reuniões")
        self.root.geometry("800x600")

        self.label_titulo = tk.Label(root, text="Gerenciador de Tarefas e Reuniões", font=("Arial", 18))
        self.label_titulo.pack(pady=10)

        self.frame_form = tk.Frame(root)
        self.frame_form.pack(pady=10)

        tk.Label(self.frame_form, text="Tipo (Tarefa/Reunião):").grid(row=0, column=0, padx=5, pady=5)
        self.tipo_entry = ttk.Combobox(self.frame_form, values=["Tarefa", "Reunião"])
        self.tipo_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_form, text="Título:").grid(row=1, column=0, padx=5, pady=5)
        self.titulo_entry = tk.Entry(self.frame_form)
        self.titulo_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_form, text="Descrição:").grid(row=2, column=0, padx=5, pady=5)
        self.descricao_entry = tk.Entry(self.frame_form)
        self.descricao_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame_form, text="Data (AAAA-MM-DD):").grid(row=3, column=0, padx=5, pady=5)
        self.data_entry = tk.Entry(self.frame_form)
        self.data_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.frame_form, text="Hora (HH:MM):").grid(row=4, column=0, padx=5, pady=5)
        self.hora_entry = tk.Entry(self.frame_form)
        self.hora_entry.grid(row=4, column=1, padx=5, pady=5)

        self.btn_adicionar = tk.Button(self.frame_form, text="Adicionar Evento", command=self.adicionar_evento)
        self.btn_adicionar.grid(row=5, column=0, columnspan=2, pady=10)

        self.tree = ttk.Treeview(root, columns=("Tipo", "Título", "Descrição", "Data", "Hora"), show="headings")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Descrição", text="Descrição")
        self.tree.heading("Data", text="Data")
        self.tree.heading("Hora", text="Hora")
        self.tree.pack(fill="both", expand=True, pady=10)

        self.btn_salvar = tk.Button(root, text="Salvar Dados", command=self.salvar_dados)
        self.btn_salvar.pack(pady=5)

        self.btn_excluir = tk.Button(root, text="Excluir Evento", command=self.excluir_evento)
        self.btn_excluir.pack(pady=5)

        self.atualizar_tabela()

    def adicionar_evento(self):
        tipo = self.tipo_entry.get()
        titulo = self.titulo_entry.get()
        descricao = self.descricao_entry.get()
        data = self.data_entry.get()
        hora = self.hora_entry.get()

        if tipo == "Tarefa":
            evento = Tarefa(titulo, descricao, data)
            self.calendario.adicionar_tarefa(evento)
        elif tipo == "Reunião":
            evento = Reuniao(titulo, data, hora, descricao)
            self.calendario.adicionar_reuniao(evento)
        else:
            messagebox.showerror("Erro", "Selecione um tipo válido.")
            return

        self.atualizar_tabela()
        self.limpar_campos()

    def atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for evento in self.calendario.listar_eventos():
            tipo = "Tarefa" if isinstance(evento, Tarefa) else "Reunião"
            data = evento.data_limite.strftime("%Y-%m-%d") if isinstance(evento, Tarefa) else evento.data.strftime("%Y-%m-%d")
            hora = "" if isinstance(evento, Tarefa) else evento.hora.strftime("%H:%M")
            self.tree.insert("", "end", values=(tipo, evento.titulo, evento.descricao, data, hora))

    def salvar_dados(self):
        self.calendario.salvar_dados()
        messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

    def excluir_evento(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showerror("Erro", "Selecione um evento para excluir.")
            return

        evento_valores = self.tree.item(selecionado, "values")
        tipo, titulo, descricao, data, hora = evento_valores

        if tipo == "Tarefa":
            self.calendario.remover_tarefa(titulo)
        elif tipo == "Reunião":
            self.calendario.remover_reuniao(titulo)

        self.tree.delete(selecionado)
        messagebox.showinfo("Sucesso", "Evento excluído com sucesso!")

    def limpar_campos(self):
        self.tipo_entry.set("")
        self.titulo_entry.delete(0, tk.END)
        self.descricao_entry.delete(0, tk.END)
        self.data_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorGUI(root)
    root.mainloop()
