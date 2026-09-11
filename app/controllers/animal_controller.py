from app.models.animal import Animal
from app.core.data_utils import Data_Utils
class Animal_Controller:

    def __init__(self, dao,nome_dao , data_nascimento_dao , sexo_dao , peso_dao , cliente_id, especie_id , raca_id, view):
        self.dao = dao
        self.view = view
        self.animal_selecionado = None
        self.nome_dao = nome_dao 
        self.data_nascimento_dao = data_nascimento_dao
        self.sexo_dao = sexo_dao
        self.peso_dao = peso_dao
        self.cliente_id = cliente_id
        self.especie_id = especie_id
        self.raca_id = raca_id

    def new(self):
        self.view.limpar_campos()

    def carregar_clientes(self):
        cliente = self.cliente_dao.get_all()
        self.view.carregar_cliente(cliente)

    def carregar_especie(self):
        especie = self.especie_dao.get_all()
        self.view.carregar_especie(especie)

    def carregar_raca(self):
        raca = self.raca_dao.get_all()
        self.view.carregar_raca(raca)

    def get_all(self):
        animal = self.dao.get_all()
        self.view.exibir_animal(animal)

    def selecionar_animal(self, event):
        try:
            id_animal = self.view.get_id_selecionado()

            self.animal_selecionado = self.dao.get_by_id(
                id_animal
            )

            cliente = self.cliente_dao.get_all()

            especie = self.especie_dao.get_all()

            raca = self.raca_dao.get_all()

            self.view.preencher_campos(
                self.usuario_selecionado,
                cliente, especie, raca
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.animal_selecionado is None:
                self.view.exibir_mensagem(
                    ("Selecione um animal na lista."),
                    False
                )
                return
            nome, data_nascimento, sexo, peso, cliente, especie, raca = (
                self.view.ler_dados_animal()
            )
            self.animal_selecionado.atualizar_dados(
                nome,
                Data_Utils.string_para_data(data_nascimento),
                peso,
                sexo,
                cliente,
                especie,
                raca
            )
            self.dao.update(self.animal_selecionado)
            self.get_all()
            self.view.exibir_mensagem(
                ("Animal atualizado com sucesso!")
            )
        except ValueError as e:
            self.view.exibir_mensagem(
                (("Erro: ")(str(e)), False),
                False
            )
    def delete(self):
        if self.animal_selecionado is None:
            self.view.exibir_mensagem(
                ("Selecione um animal na lista."),
                False
            )
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(
                self.animal_selecionado.id
            )
            if sucesso:
                self.animal_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(
                    ("Animal excluído com sucesso!")
                )
            else:
                self.view.exibir_mensagem(
                    ("Usuário não encontrado."),
                    False
                )
        except Exception:
            self.view.exibir_mensagem(
                ("Problemas ao excluir animal"),
                False
            )