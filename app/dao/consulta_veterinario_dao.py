from app.dao.dao import DAO
from app.models.consulta_veterinario import Consulta_Veterinario


class Consulta_Veterinario_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)

    def save(self, consulta_id, veterinario_id):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:
            sql = """
                INSERT INTO CONSULTA_VETERINARIO
                (ID_CONSULTA, ID_VETERINARIO)
                VALUES (%s, %s)
            """

            cursor.execute(
                sql,
                (consulta_id, veterinario_id)
            )

            conexao.commit()

        except Exception:
            conexao.rollback()
            raise

        finally:
            self._database.desconectar(
                cursor,
                conexao
            )

    def get_all(self):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:
            sql = """
                SELECT ID_CONSULTA, ID_VETERINARIO
                FROM CONSULTA_VETERINARIO
            """

            cursor.execute(sql)

            registros = cursor.fetchall()

            relacionamentos = []

            for registro in registros:
                relacionamentos.append(
                    Consulta_Veterinario(
                        registro[0],
                        registro[1]
                    )
                )

            return relacionamentos

        finally:
            self._database.desconectar(
                cursor,
                conexao
            )

    def get_by_id(self, consulta_id):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:
            sql = """
                SELECT ID_CONSULTA, ID_VETERINARIO
                FROM CONSULTA_VETERINARIO
                WHERE ID_CONSULTA = %s
            """

            cursor.execute(
                sql,
                (consulta_id,)
            )

            registro = cursor.fetchone()

            if registro:
                return Consulta_Veterinario(
                    registro[0],
                    registro[1]
                )

            return None

        finally:
            self._database.desconectar(
                cursor,
                conexao
            )

    def update(self, consulta_veterinario):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:
            sql = """
                UPDATE CONSULTA_VETERINARIO
                SET ID_VETERINARIO = %s
                WHERE ID_CONSULTA = %s
            """

            cursor.execute(
                sql,
                (
                    consulta_veterinario.veterinario_id,
                    consulta_veterinario.consulta_id
                )
            )

            conexao.commit()

        except Exception:
            conexao.rollback()
            raise

        finally:
            self._database.desconectar(
                cursor,
                conexao
            )

    def delete(self, consulta_id):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:
            sql = """
                DELETE FROM CONSULTA_VETERINARIO
                WHERE ID_CONSULTA = %s
            """

            cursor.execute(
                sql,
                (consulta_id,)
            )

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self._database.desconectar(
                cursor,
                conexao
            )