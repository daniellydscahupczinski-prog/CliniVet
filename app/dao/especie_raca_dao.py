from app.models.especie_raca import Especie_Raca
from app.dao.dao import DAO


class Especie_Raca_DAO(DAO):

    def save(self, especie_id, raca_id):

        especie_raca = Especie_Raca(
            especie_id,
            raca_id
        )

        sql = """
            INSERT INTO ESPECIE_RACA
            (ESPECIE_ID, RACA_ID)
            VALUES (%s, %s)
        """

        valores = (
            especie_raca.especie_id,
            especie_raca.raca_id
        )

        self.cursor.execute(sql, valores)
        self.conn.commit()
    def get_all(self):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:
            sql = """
                SELECT ID_ESPECIE, ID_RACA
                FROM ESPECIE_RACA
            """

            cursor.execute(sql)

            registros = cursor.fetchall()

            relacionamentos = []

            for registro in registros:
                relacionamentos.append(
                    Especie_Raca(
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
    def get_by_id(self, especie_id):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:
            sql = """
                SELECT ID_ESPECIE, ID_RACA
                FROM ESPECIE_RACA
                WHERE ID_ESPECIE = %s
            """

            cursor.execute(
                sql,
                (especie_id,)
            )

            registro = cursor.fetchone()

            if registro:
                return Especie_Raca(
                    registro[0],
                    registro[1]
                )

            return None

        finally:
            self._database.desconectar(
                cursor,
                conexao
            )

    def update(self, especie_raca):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:
            sql = """
                UPDATE ESPECIE_RACA
                SET ID_RACA = %s
                WHERE ID_ESPECIE= %s
            """

            cursor.execute(
                sql,
                (
                    especie_raca.raca_id,
                    especie_raca.especie_id
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
    def get_by_especie(self, especie_id):

        sql = """
            SELECT RACA_ID
            FROM ESPECIE_RACA
            WHERE ESPECIE_ID = %s
        """

        self.cursor.execute(sql, (especie_id,))

        return self.cursor.fetchall()

    def delete(self, especie_id, raca_id):

        sql = """
            DELETE FROM ESPECIE_RACA
            WHERE ESPECIE_ID = %s
            AND RACA_ID = %s
        """

        self.cursor.execute(
            sql,
            (especie_id, raca_id)
        )

        self.conn.commit()

        return self.cursor.rowcount > 0