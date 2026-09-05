class Raca:

    def __init__(
            self,
            id,
            nome,
            especie_id
    ):
        self._id = id
        self._nome = nome
        self._especie_id = especie_id

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def nome(self):
        return self.nome.upper()
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def especie_id(self):
        return self.especie_id
    
    @especie_id.setter
    def especie_id(self, nova_especie_id):
        self.especie_id = nova_especie_id

    def atualizar_dados(
            self,
            novo_nome,
            nova_especie_id
    ):
        self._nome = novo_nome
        self._especie_id = nova_especie_id
        