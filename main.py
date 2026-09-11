from colorama import init
from app.core.database import Database

# Componentes de Raca
from app.dao.raca_dao import Raca_DAO
from app.views.raca_view import Raca_View
from app.controllers.raca_controller import Raca_Controller

# Componentes de Cliente
from app.dao.cliente_dao import Cliente_DAO
from app.views.cliente_view import Cliente_View
from app.controllers import cliente_controller

# Componentes de Agendamento
from app.dao.agendamento_dao import Agendamento_DAO
from app.views.agendamento_view import Agendamento_View
from app.controllers.agendamento_controller import Agendamento_Controller

import tkinter as tk

class ErpApplication:

    def __init__(self):

        init(autoreset=True)

        self._database = Database()

        self._root = tk.Tk()

        self._usuario_logado = None

        self._janela_raca= None
        self._janela_agendamento = None
        self._janela_cliente = None

        # ================================
        # RACA
        # ================================

        self._dao_raca  = Raca_DAO(
            self._database
        )

        self._ctrl_raca = Raca_Controller(
            dao = self._dao_raca,
            view = None
        )

        # ==================================
        # CLIENTE
        # =================================
        
        self._dao_cliente = Cliente_DAO(
            self._database
        )

        self._ctrl_cliente = cliente_controller(
            dao=self._dao_cliente,
            view=None
        )

        # ==================================
        # AGENDAMENTO
        # ==================================

        self._dao_agendamento = Agendamento_DAO(
            self._database
        )
        
        self._ctrl_agendamento = Agendamento_Controller(
            dao=self._dao_agendamento,
            view=None
        )

    def _configurar_janela(self):
        titulo = "Sistema Corporativo ERP"
        if self._usuario_logado is not None:
            titulo = f"{titulo} — {self._usuario_logado.nome} ({self._usuario_logado.perfil.nome})"
        self._root.title(titulo)
        self._root.state("zoomed")

    def _criar_menu(self):

        menu_principal = tk.Menu(self._root)

        menu_cadastros_basicos = tk.Menu(menu_principal, tearoff=0)
        menu_cadastros_basicos.add_command(
            label=("Menu de raca"),
            command=self._abrir_raca
        )
        menu_cadastros_basicos.add_command(
            label=("Menu de cliente"),
            command=self._abrir_cliente
        )
        menu_principal.add_cascade(
            label=("Menu de agendamento"),
            menu=menu_cadastros_basicos
        )


    def _abrir_janela(
        self,
        atributo_janela,
        classe_view,
        controller
    ):   

        janela_existente = getattr(
            self,
            atributo_janela
        )

        if (
            janela_existente is not None
            and janela_existente.winfo_exists()
        ):
            janela_existente.lift()
            janela_existente.focus_force()
            return

        janela = tk.Toplevel(
            self._root
        )

        setattr(
            self,
            atributo_janela,
            janela
        )

        controller.view = classe_view(
            janela,
            controller
        )

        controller.view.iniciar()

    def _abrir_raca(self):
        self._abrir_raca(
            "_janela_raca",
            Raca_View,
            self._ctrl_raca
        )
    
    def _abrir_cliente(self):
        self._abrir_cliente(
            "_janela_cliente",
            Cliente_View,
            self._ctrl_cliente
        )

    def _abrir_agendamento(self):
        self._abrir_agendamento(
            "janela_agendamento",
            Agendamento_View,
            self._ctrl_agendamento
        )
    
    def run(self):
        self._root.mainloop()


if __name__ == "__main__":

    app = ErpApplication()

    app.run()
    
