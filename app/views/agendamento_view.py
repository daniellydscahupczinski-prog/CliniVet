
from app.models.agendamento import Agendamento
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Agendamento_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._estados = []
        self._cidades = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title((("Crud de agendamentos")))
        self.root.geometry("900x600")
        self.root.resizable(False, False)


    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = (("Cadastro de agendamento")),
            font = ("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            columnspan = 4,
            padx = 5,
            pady = 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text = (("Dados do agendamento"))
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan=4,
            padx = 10,
            pady = 5,
            sticky = "ew"
        )
        self.frm_dados.grid_columnconfigure(0, weight=0)
        self.frm_dados.grid_columnconfigure(1, weight=1)
        self.frm_dados.grid_columnconfigure(2, weight=0)
        self.frm_dados.grid_columnconfigure(3, weight=1)
        self.lbl_id = tk.Label(
            self.frm_dados,
            text = "ID:"
        )
        self.lbl_id.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width = 10,
            state = "readonly"
        )
        self.txt_id.grid(
            row = 0,
            column= 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_servico_agendamento = tk.Label(
            self.frm_dados,
            text = "SERVICOS"
        )
        self.lbl_servico_agendamento.grid(
            row = 1,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_servico_agendamento = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_servico_agendamento.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_horario_agendamento = tk.Label(
            self.frm_dados,
            text = "Horarios"
        )
        self.lbl_horario_agendamento.grid(
            row = 1,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_horario_agendamento = tk.Entry(
            self.frm_dados,
            width = 20,
            state = "readonly"
        )
        self.txt_horario_agendamento.grid(
            row = 1,
            column= 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_data_agendamento = tk.Label(
            self.frm_dados,
            text = "Data do agendamento"
        )
        self.lbl_id.grid(
            row = 2,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width = 20,
            state = "readonly"
        )
        self.txt_id.grid(
            row = 2,
            column= 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_status_agendamento = tk.Label(
            self.frm_dados,
            text = ("Status:")
        )
        self.lbl_status_agendamento.grid(
            row = 2,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.cmb_status_agendamento = ttk.Combobox(
            self.frm_dados,
            width = 37,
            state = "readonly"
        )
        self.cmb_status_agendamento.grid(
            row = 2,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border = 2,
            relief = "groove"
        )
        self.frm_botoes.grid(
            row = 4,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 4,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text = (("novo")),
            width = 15
        )
        self.btn_novo.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text = (("salvar")),
            width = 15
        )
        self.btn_salvar.grid(
            row = 0,
            column = 1,
            padx = 5,
            pady = 5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text = (("alterar")),
            width = 15
        )
        self.btn_alterar.grid(
            row = 0,
            column = 2,
            padx = 5,
            pady = 5
        )
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text = (("excluir")),
            width = 15
        )
        self.btn_excluir.grid(
            row = 0,
            column = 3,
            padx = 5,
            pady = 5
        )
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text = (("fechar")),
            width = 15
        )
        self.btn_fechar.grid(
            row = 0,
            column = 4,
            padx = 5,
            pady = 5
        )
        self.tbl_agendamento = ttk.Treeview(
            self.root,
            height = 10
        )
        self.tbl_agendamento.grid(
            row = 5,
            column = 0,
            columnspan = 4,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )
    def configurar_treeview(self):
        self.tbl_clientes["columns"] = (
            "id",
            "servico_agendamento",
            "horario_agendamento",
            "data_agendamento",
            "status_agendamento"
        )
        self.tbl_agendamento.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_agendamento.column(
            "id",
            width = 10,
            anchor = "center"
        )
        self.tbl_agendamento.column(
            "servico_agendamento",
            width = 40
        )
        self.tbl_agendamento.column(
            "horario_agendamento",
            width = 20,
            anchor = "center"
        )
        self.tbl_agendamento.column(
            "data_agendamento",
            width = 15,
            anchor = "center"
        )
        self.tbl_agendamento.column(
            "limite",
            width = 20,
            anchor = "e"
        )
        self.tbl_agendamento.column(
            "status_agendamento",
            width = 30
        )
        self.tbl_agendamento.heading(
            "id",
            text = "ID"
        )
        self.tbl_agendamento.heading(
            "servicos",
            text = "Servicos"
        )
        self.tbl_agendamento.heading(
            "horario_agendamento",
            text = "Horario"
        )
        self.tbl_agendamento.heading(
            "Data",
            text = "Data"
        )
        self.tbl_agendamento.heading(
            "status",
            text = "Status do agendamento"
        )
    def configurar_eventos(self):
        self.btn_novo.config(
            command = self.controller.new
        )
        self.btn_salvar.config(
            command = self.controller.save
        )
        self.btn_alterar.config(
            command = self.controller.update
        )
        self.btn_excluir.config(
            command = self.controller.delete
        )
        self.btn_fechar.config(
            command = self.fechar
        )
        self.tbl_agendamento.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_agendamento
        )
    def preencher_campos(self, agendamento):

        self.limpar_campos()

        self.txt_id.config(state="normal")
        self.txt_id.insert(
        0,
        str(agendamento.id)
        )
        self.txt_id.config(state="readonly")

        self.txt_servico.insert(
        0,
        agendamento.servico_agendamento
        )

        self.txt_horario.insert(
        0,
        agendamento.horario_agendamento
        )

        self.txt_data.insert(
        0,
        agendamento.data_agendamento
        )

        self.cmb_status.set(
        agendamento.status_agendamento
        )
    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state="readonly")

        self.txt_servico.delete(0, tk.END)
        self.txt_horario.delete(0, tk.END)
        self.txt_data.delete(0, tk.END)

        self.cmb_status.set("")

        self.txt_servico.focus()   

    def limpar_treeview(self):
        for item in self.tbl_agendamento.get_children():
            self.tbl_agendamento.delete(item)   

    def get_id_selecionado(self):

        item = self.tbl_agendamento.selection()[0]

        return self.tbl_agendamento.item(item)["values"][0]
    
    def confirmar_exclusao(self):

        return messagebox.askyesno(
            (("Confirmaçao")),
            (("Deseja realmente excluir este agendamento?")),
            parent=self.root
        )

    def ler_dados_agendamento(self):
        servico_agendamento = self.txt_servico.get()
        horario_agendamento = self.txt_horario.get()
        data_agendamento = self.txt_data.get()
        status_agendamento = self.cmb_status.get()

        return servico_agendamento, horario_agendamento, data_agendamento, status_agendamento
    
    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(
                "Mini ERP",
                mensagem,
                parent=self.root
            )
        else:
            messagebox.showerror(
                "Mini ERP",
                mensagem,
                parent=self.root
            )

    def exibir_agendamento(self, agendamento):

        self.limpar_treeview()

        for agendamento in agendamento:

            self.tbl_clientes.insert(
                "",
                tk.END,
                values=(
                    agendamento.id,
                    agendamento.servico_agendamento,
                    agendamento.horario_agendamento,
                    agendamento.data_agendamento,
                    agendamento.status_agendamento
                )
            )
    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()
