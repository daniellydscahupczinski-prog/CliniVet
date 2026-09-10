from app.models.consulta import Consulta

class Consulta_Controller:
    def __init__(self,dao,consulta_dao,view):
        self.dao = dao
        self.consulta_dao = consulta_dao
        self.view = view

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try: 
            data_consulta, horario_consulta, observacoes = self.view.ler_dados_consulta
            consulta = Consulta(
                None, 
                data_consulta, 
                horario_consulta, 
                observacoes
             )
            self.dao.save(consulta)
            self.get_all()
            self.view.exibir_mensagem("Agendamento de Consultas")
        except ValueError:
            self.view.exibir_mensagem("Erro!")

    def get_all(self):
        consultas = self.dao.get_all()
        self.view.exibir_consultas(consultas)

    def selecionar_consultas(self,event):
        try: 
            id_consulta = self.view.get_id_selecionado()
            self.consulta_selecionada = self.dao.get_by_id(
                id_consulta
            )
            self.view.preencher_campos(
                self.consulta_selecionada
            )
        except IndexError:
            pass
    def update(self):
        try: 
            if self.consulta_selecionada is None: 
                self.view.exibir_mensagem("Selecione uma consulta da lista: ")
                return
            data_consulta, horario_consulta, observacoes = self.view.ler_dados_consulta
            self.consulta_selecionada.atualizar_dados(data_consulta,horario_consulta,observacoes)
            self.dao.update(self.consulta_selecionada)
            self.get_all()
            self.view.exibir_mensagem("Consulta Atualizada com Sucesso!")
        except ValueError as e: 
            self.view.exibir_mensagem (f"Erro:", False)

    def delete(self):
        if self.consulta_selecionada is None: 
            self.view.exibir_mensagem("Seleciona uma consulta da lista: ")
            return 
        if not self.view.confirmar_exclusao():
            return
        try: 
            sucesso = self.dao.delete(self.consulta_selecionada.id)
            if sucesso: 
                self.consulta_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Consulta Atualizada com sucesso!")
            else: 
                self.view.exibir_mensagem("Consulta não encontrada!")
        except Exception as e: 
            self.view.exibir_mensagem("Erro ao exclur Consulta")

    
