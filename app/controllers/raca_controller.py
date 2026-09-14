from app.models.raca import Raca

class Raca_Controller:

    def __init__(
        self,
        dao,
        view
    ):
        self.dao = dao
        self.view = view

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome = self.view.ler_dados_cliente()
            cliente = Raca(
                None,
                nome,
                
            )
            self.dao.save(cliente)
            self.get_all()
            self.view.exibir_mensagem((("Raça cadastrada com sucesso!")))
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def get_all(self):
        raca = self.dao.get_all()
        self.view.exibir_raca(raca)

    def selecionar_raca(self, event):
        try:
            id_raca = self.view.get_id_selecionado()
            self.raca_selecionada = self.dao.get_by_id(
                id_raca
            )
            
            self.view.preencher_campos(
                self.raca_selecionado,
                Raca
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.cliente_selecionado is None:
                self.view.exibir_mensagem((("Selecione uma raça da lista", False)))
                return
            nome = self.view.ler_dados_cliente()
            self.raca_selecionada.atualizar_dados(
                nome
               
            )
            self.dao.update(self.cliente_selecionado)
            self.get_all()
            self.view.exibir_mensagem((("Raça atualizada")))
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.cliente_selecionado is None:
            self.view.exibir_mensagem((("Selecione uma raça na lista", False)))
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.cliente_selecionado.id)
            if sucesso:
                self.cliente_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem((("Raça excluida com sucesso")))
            else:
                self.view.exibir_mensagem((("Raça nao encontrada", False)))
        except Exception as e:
            self.view.exibir_mensagem((("Problemas ao excluir raça", False)))
        