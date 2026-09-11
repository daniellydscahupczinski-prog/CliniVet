from app.dao.dao import DAO
from app.models.aplicacao_vacina import Aplicacao_Vacina

class Aplicacao_Vacina_DAO(DAO):
    def init(self, database):
        super().init(database)

def save(self, aplicacao_vacina):
    conexao, cursor = self.conectar()
    try:
        sql = """
                INSERT INTO APLICACAO_VACINA
                (TIPO_SERVICO, DATA_VACINA, HORARIO_VACINA, STATUS_VACINA, ANIMAL_ID, VACINA_ID)
                VALUES(%s, %s, %s, %s, %s, %s)
                """
        cursor.execute(sql, (
            aplicacao_vacina.tipo_servico,
            aplicacao_vacina.data_vacina,
            aplicacao_vacina.horario_vacina,
            aplicacao_vacina.status_vacina,
            aplicacao_vacina.animal_id,
            aplicacao_vacina.vacina_id,
        ))
        conexao.commit()
        aplicacao_vacina.id = cursor.lastrowid
        return aplicacao_vacina
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
                ID, TIPO_SERVICO, DATA_VACINA, HORARIO_VACINA,
                STATUS_VACINA, ANIMAL_ID, VACINA_ID
            FROM
                APLICACAO_VACINA
            ORDER BY
                DATA_VACINA
              """
        cursor.execute(sql)
        registro = cursor.fetchone()

        if registro is None:
            return None

        animal = self._animal_dao.get_by_id
        vacina = self.vacina_dao.get_by_Id(
            registro[5]
        )

        return Aplicacao_Vacina(
            registro[0],
            registro[1],
            registro[2],
            registro[3],
            registro[4],
            animal, 
            vacina
        
        )
        return aplicacoes_vacina
    finally:
        self.desconectar(cursor, conexao)
def get_by_id(self, id):
    conexao, cursor = self.conectar()
    try:
        sql = """
            SELECT 
                ID, TIPO_SERVICO, DATA_VACINA, HORARIO_VACINA,
                STATUS_VACINA, ANIMAL_ID, VACINA_ID
            FROM 
                APLICACAO_VACINA
            WHERE
                ID = %s
              """
        cursor.execute(sql, (id,))
        registro = cursor.fetchone()
        if registro is None:
            return None
        
        animal = self._animal_dao.get_by_id
        vacina = self._vacina_dao.get_by_id(
                registro[5]
            )
        return Aplicacao_Vacina(
            registro[0],
            registro[1],
            registro[2],
            registro[3],
            registro[4],
            animal,
            vacina
        )
    finally:
        self.desconectar(cursor, conexao)
def update(self, aplicacao_vacina):
    conexao, cursor = self.conectar()
    try:
        sql = """
            UPDATE APLICACAO_VACINA SET 
                TIPO_SERVICO = %s,
                DATA_VACINA = %s,
                HORARIO_VACINA = %s,
                STATUS_VACINA = %s,
                ANIMAL_ID = %s,
                VACINA_ID = %s
            WHERE 
                ID = %s
              """
        cursor.execute(sql, (
            aplicacao_vacina.tipo_servico,
            aplicacao_vacina.data_vacina,
            aplicacao_vacina.horario_vacina,
            aplicacao_vacina.status_vacina,
            aplicacao_vacina.animal_id,
            aplicacao_vacina.vacina_id,
            aplicacao_vacina.id
        ))
        conexao.commit()
        sucesso = cursor.rowcount > 0
        return sucesso
    except Exception:
        conexao.rollback()
        raise
    finally:
        self.desconectar(cursor, conexao)
def delete(self, id):
    conexao, cursor = self.conectar()
    try:
        sql = """
                    DELETE FROM APLICACAO_VACINA  
                    WHERE ID = %s
                """
        cursor.execute(sql, (id,))
        conexao.commit()
        sucesso = cursor.rowcount > 0
        return sucesso
    except Exception:
        conexao.rollback()
        raise
    finally:
        self.desconectar(cursor, conexao)