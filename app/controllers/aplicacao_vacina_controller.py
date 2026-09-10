from app.models.aplicacao_vacina import Aplicacao_Vacina
from app.core.data_utils import Data_Utils
class Usuario_Controller:

    def __init__(self, dao, tipo_servico_dao, data_vacina_dao, horario_vacina_dao, status_vacina_dao, animal_id, vacina_id, view):
        self.dao = dao
        self.view = view
        self.aplicacao_vacina_selecionada = None
        self.tipo_servico_dao = tipo_servico_dao
        self.data_vacina_dao = data_vacina_dao
        self.horario_vacina_dao = horario_vacina_dao
        self.status_vacina_dao = status_vacina_dao
        self.animaL_id = animal_id
        self.vacina_id = vacina_id

    def new(self):
        self.view.limpar_campos()

    def carregar_animal(self):
        animal = self.animal_dao.get_all()
        self.view.carregar_animal(animal)

    def carregar_perfis(self):
        vacina = self.vacina_dao.get_all()
        self.view.carregar_vacina(vacina)

    def save(self):
        try:
            tipo_servico, data_vacina, horario_vacina, status_vacina, animal, vacina = (
                self.view.ler_dados_aplicacao_vacina()
            )
            aplicacao_vacina = Aplicacao_Vacina(
                None, tipo_servico, data_vacina, horario_vacina, status_vacina, animal, vacina
            )
            self.dao.save(aplicacao_vacina)
            self.get_all()
            self.view.exibir_mensagem("Aplicação da vacina cadastrada com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem("Erro: "(str(e)), False)

    def get_all(self):
        aplicacao_vacina = self.dao.get_all()
        self.view.exibir_usuarios(aplicacao_vacina)

    def selecionar_aplicacao_vacina(self, event):
        try:
            id_aplicacao_vacina = self.view.get_id_selecionado()

            self.aplicacao_vacina_selecionada = self.dao.get_by_id(
                id_aplicacao_vacina
            )

            animal = self.animal_dao.get_all()

            vacina = self.vacina_dao.get_all()

            self.view.preencher_campos(
                self.aplicacao_vacina_selecionada,
                animal,
                vacina
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.aplicacao_vacina_selecionada is None:
                self.view.exibir_mensagem(
                    ("Selecione uma aplicação da vacina na lista."),
                    False
                )
                return
            tipo_servico, data_vacina, horario_vacina, status_vacina, animal_id, vacina_id = (
                self.view.ler_dados_aplicacao_vacina()
            )
            self.aplicacao_vacina_selecionada.atualizar_dados(
               tipo_servico,
               data_vacina,
               horario_vacina,
               status_vacina,
               animal_id,
               vacina_id
            )
            self.dao.update(self.aplicacao_vacina_selecionada)
            self.get_all()
            self.view.exibir_mensagem(
                ("Aplicação da vacina atualizada com sucesso!")
            )
        except ValueError as e:
            self.view.exibir_mensagem(
                ("Erro: "(str(e)), False),
                False
            )
    def delete(self):
        if self.aplicacao_vacina_selecionada is None:
            self.view.exibir_mensagem(
                ("Selecione uma aplicação da vacina na lista."),
                False
            )
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(
                self.aplicacao_vacina_selecionada.id
            )
            if sucesso:
                self.aplicacao_vacina_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(
                    ("Usuário excluído com sucesso!")
                )
            else:
                self.view.exibir_mensagem(
                    ("Aplicação da vacina não encontrado"),
                    False
                )
        except Exception:
            self.view.exibir_mensagem(
                ("Problemas ao excluir a aplicação da vacina."),
                False
            )