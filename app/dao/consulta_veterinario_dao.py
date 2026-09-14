from app.dao.dao import DAO 
from app.models.consulta_veterinario import Consulta_Veterinario

class Consulta_Veterinario_DAO(DAO):
    def __init__(self,database):
        super().__init__(database)

    def save(self,  consulta) :
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        try: 
            sql = """
                    SELECT 
                    C.ID,
                    C.DATA_CONSULTA,
                    C.HORA_CONSULTA,
                    C.OBSERVACOES
                    FROM CONSULTA C
                    INNER JOIN 
                        CONSULTA_VETERINARIO CV
                        ON CV.VETERINARIO_ID = V.ID
                    WHERE 
                        CV.ID_CONSULTA = %s
                    ORDER BY 
                        C.DATA_CONSULTA 
                    """
            cursor.execute(sql,(consulta.id,))
            resgitros = cursor.fetchall
            veterinarios = []
            for registro in resgitros:
                veterinarios.append(
                    Veterinario(
                        registro[0],
                        registro[1]
                    )
                )
                return veterinarios
        finally: 
            self._database.desconectar(cursor, conexao)

    def substituir_veterinario_da_consulta(self, consulta, veterinarios):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        try: 
            cursor.execute(
                """
                    DELETE FROM CONSULTA_VETERINARIO
                    WHERE ID_CONSULTA = %s

                """,(
                    consulta.id
                )
            )
            for veterinario in veterinarios: 
                cursor.execute(
                    """
                    INSERT INTO CONSULTA_VETERINARIO
                    (ID_CONSULTA, ID_VETERINARIO)
                    VALUES (%s, %s)
                    """, (
                        consulta.id, veterinario.id
                    )
                )
                conexao.commit()
        except Exception: 
            conexao.rollback()
            raise
        finally: 
            self._database.desconectar(cursor, conexao)
