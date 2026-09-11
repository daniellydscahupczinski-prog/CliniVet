from app.dao.dao import DAO 
from app.models.consulta_veterinario import Consulta_Veterinario

class Consulta_Veterinario_DAO(DAO):
    def __init__(self,database):
        super().__init__(database)

    def save(self, consulta_veterinario):
        conexao, cursor = self.conectar()
        cursor.execute(
            """ INSERT INTO CONSULTA_VETERINARIO
            (FK_CONSULTA_ID, FK_VETERINARIO_ID)
            VALUES(%s,%s)
""", (
    consulta_veterinario.consulta_id, 
    consulta_veterinario.veterinario_id
)
        )