from app.dao.dao import DAO
from app.models.especie import Especie 

class Especie_DAO(DAO):
    def __init__(self, database, raca_dao):
        super().__init__(database)
        self._raca_dao = raca_dao

    def save(self,especie):
        conexao,cursor = self.conectar()
        try: 
            sql = """     INSERT INTO ESPECIE 
            (NOME,ID_RACA) VALUES ( %s, %s )
            """
            cursor.execute(
                sql, (
                    especie.nome,
                    especie.raca.id
                )
            )
            conexao.commit()
            especie.id = cursor.lastrwid
            return especie
        except Exception: 
            conexao.rollback()
            raise
        finally: 
            self.desconectar(cursor,conexao)


 



    def get_all(self):
        conexao, cursor = self.conectar()
        try: 
            sql = """
                    SELECT ID, NOME
                    FROM ESPECIE 
                    ORDER BY NOME
                """
            cursor.execute(sql)
            registros = cursor.fetchall()
            especies = []
            for registro in registros: 
                raca = self._raca_dao.get_by_id(
                    registros[2]
                )
                especies.append(
                    Especie( 
                        registro [0],
                        registro[1],
                        raca
                    )

                )
            return especies 

        finally: 
            self.desconectar(cursor,conexao)

    def get_by_id_raca(self, raca_id):
        conexao, cursor = self.conectar()
        try: 
            sql = """
                SELECT ID, NOME, RACA_ID
                FROM ESPECIE 
                WHERE RACA_ID = %s
                ORDER BY NOME
            """
            cursor.execute(
                sql,(raca_id,)
            )
            registros = cursor.fetchall()
            especies = []
            for registro in registros: 
                raca = self._raca_dao.get_by_id(
                    registro[2]
                )
                especies.append(
                    Especie(
                        registro[0],
                        registro[1],
                        raca
                    )
                )
                return especies
        finally: 
            self.desconectar(cursor,conexao)

    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try: 
            sql = """ 
                    SELECT ID, NOME, RACA_ID
                    FROM ESPECIE 
                    WHERE ID = %s
                """
            cursor.execute(sql,(id,))
            registro = cursor.fetchone()

            if registro is None: 
                return None
            raca = self._raca_dao.get_by_id(
                registro[2]
            )
            return Especie(
                registro[0],
                registro[1],
                raca
            )
        finally: 
            self.desconectar(cursor,conexao)

    def update(self,especie):
        conexao, cursor = self.conectar()
        try: 
            sql = """
                UPDATE ESPECIE SET 
                NOME = %s
                RACA_ID = %s
                WHERE 
                ID = %s

            """
            cursor.execute(
                sql,(
                    especie.nome, 
                    especie.raca_id,
                    especie.id
                )
            )
            conexao.commit()
            return cursor.rowcount > 0
        except Exception:
            conexao.rollback()
            raise
        finally: 
            self.desconectar(cursor, conexao)
    def delete(self, id):
        conexao, cursor = self.conectar()

        try:

            sql = """
                    DELETE
                    FROM ESPECIE
                    WHERE ID = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:

            conexao.rollback()
            raise

        finally:

            self.desconectar(cursor, conexao)