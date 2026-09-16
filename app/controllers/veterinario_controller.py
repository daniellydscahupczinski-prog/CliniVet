from app.models.veterinario import Veterinario 

class Veterinario_Controller:

    def __init__(self,dao, view ):
        self.dao = dao
        self.view = view
        self.veterinario_selecionado = None

def new(self):
    self.view.limpar_campos()

def save(self):
    try: 
        nome = self.view.ler_dados_veterinario()
        veterinario = Veterinario(
            None,
            nome
        )
        self.dao.save(veterinario)
        self.get_all()
        self.view.exibir_mensagem("Veterinario Cadastrado com sucesso!")
    except ValueError as e: 
        self.view.exibir_mensagem("Erro: Tente Novamente.")

def get_all(self):
    veterinarios = self.dao.get_all()
    self.view.exibir_veterinarios(veterinarios)

def selecionar_veterinario(self, event):
    try: 
        veterinario_id = self.view.get_id_selecionado()
        self.veterinario_selecionado = self.dao.get_by_id(
            veterinario_id
        )
        self.view.preencher_campos(
            self.veterinario_selecionado
        )
    except IndexError: 
        pass
def update(self):
    try: 
        if self.veterinario_selecionado is None: 
            self.view.exibir_mensagem("Selecione um veterinario da lista: ")
            return 
        nome,telefone,especialidade = self.view.ler_dados_veterinario()
        self.veterinario_selecionado.atualizar_dados(nome,telefone, especialidade)
        self.dao.update(self.veterinario_selecionado)
        self.get_all()
        self.view.exibir_mensagem("Veterinario atualizado com sucesso!")
    except ValueError as e: 
        self.view.exibir_mensagem("Erro. ")

def delete(self):
    if self.veterinario_selecionado is None: 
        self.view.exibir_mensagem("Selecione um veterinario da lista: ")
        return 
    if not self.view.confirmar_exclusão():
        return 
    try: 
        sucesso = self.dao.delete(self.veterinario_selecionado.id)
        if sucesso: 
            self.veterinario_selecionado = None
            self.view.limpar_campos()
            self.get_all()
            self.view.exibir_mensagem("Veterinario excluído com sucesso!")
        else: 
            self.view.exibir_mensagem("Veterinario não encontrado!")
    except Exception as e: 
        self.view.exibir_mensagem("Erro ao excluir o Veterinário")