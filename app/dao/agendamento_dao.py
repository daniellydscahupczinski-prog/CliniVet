from app.models.agendamento import Agendamento
from app   .dao.dao import DAO

class Agendamento_DAO(DAO):

    def __init__(self, database ):
        super().__init__(database)

    def save(self, agendamento):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    INSERT INTO AGENDAMENTO
                    (
                        SERVICO_AGENDAMENTO
                        HORARIO_AGENDAMENTO
                        DATA_AGENDAMENTO
                        STATUS_AGENDAMENTO
                    )
                    VALUES
                    (
                        %s,
                        %s,
                        %s,
                        %s
                    )
                  """

            cursor.execute(
                sql,
                (
                    agendamento.servico_agendamento,
                    agendamento.horario_agendamento,
                    agendamento.data_agendamento,
                    agendamento.status_agendamento
                )
            )

            conexao.commit()

            agendamento.id = cursor.lastrowid

            return agendamento

        except Exception:

            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)

    def get_all(self):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    SELECT
                        ID,
                        SERVICO_AGENDAMENTO
                        HORARIO_AGENDAMENTO,
                        DATA_AGENDAMENTO,
                        STATUS_AGENDAMENTO
                    FROM
                        AGENDAMENTO
                    ORDER BY
                        DATA_AGENDAMENTO
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            agendamento = []

            for registro in registros:

               

                agendamento.append(

                    Agendamento(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        registro[4]
                    )

                )

            return agendamento 

        finally:

            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    SELECT
                        ID,
                        SERVICO_AGENDAMENTO,
                        HORARIO_AGENDAMENTO,
                        DATA_AGENDAMENTO,
                        STATUS_AGENDAMENTO
                    FROM
                        AGENDAMENTO
                    WHERE
                        ID = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            agendamento = self._agendamento_dao.get_by_id(
                registro[4]
            )

            return Agendamento(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                agendamento
            )

        finally:

            self.desconectar(cursor, conexao)

    def update(self, agendamento):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    UPDATE AGENDAMENTO
                    SET
                        SERVICO_AGENDAMENTO = %s,
                        HORARIO_AGENDAMENTO = %s,
                        DATA_AGENDAMENTO = %s,
                        STATUS_AGENDAMENTO = %s
                    WHERE
                        ID = %s
                  """

            cursor.execute(
                sql,
                (
                    agendamento.servico_agendamento,
                    agendamento.horario_agendamento,
                    agendamento.data_agendamento,
                    agendamento.status_agendamento,
                    Agendamento.id
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
                    FROM AGENDAMENTO
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
