from app.dao.dao import DAO
from app.models.cliente import Cliente
from app.dao.animal_dao import Animal_DAO

class Cliente_DAO(DAO):
    def __init__(self, database, animal_dao):
        super().__init__(database)
        self._animal_dao = animal_dao

    def save(self, cliente):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    INSERT INTO CLIENTE
                    (
                        NOME,
                        TELEFONE,
                        CPF,
                        ANIMAL_ID
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
                    cliente.nome,
                    cliente.telefone,
                    cliente.cpf,
                    cliente.animal.id
                )
            )

            conexao.commit()

            cliente.id = cursor.lastrowid

            return cliente
        
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
                        NOME,
                        TELEFONE,
                        CPF,
                        ANIMAL_ID
                    FROM
                        CLIENTE
                    ORDER BY
                        NOME
                    """
            cursor.execute(sql)
            
            registros = cursor.fetchall()
            cliente = []
            for registro in registros:
                animal = self._animal_dao.get_by_id(
                    registro[4]
                )
                cliente.append(
                    Cliente(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        animal
                    )
                )

            return cliente
            
        finally:

            self.desconectar(cursor, conexao)

    def get_by_animal(self, id_animal):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    SELECT
                        ID,
                        NOME,
                        TELEFONE,
                        CPF,
                        ANIMAL_ID
                    FROM
                        CLIENTE
                    WHERE
                        ANIMAL_ID = %s
                    ORDER BY
                        NOME
                    """
            cursor.execute(
                sql,
                (id_animal,)
            )
            registros = cursor.fetchall()
            cliente = []
            for registro in registros:
                animal = self._animal_dao.get_by_id(
                    registro[4]
                )
                cliente.append(
                    Cliente(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3],
                        animal
                    )
                )

            return cliente

        finally:

            self.desconectar(cursor, conexao)

    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    SELECT
                        ID,
                        NOME,
                        TELEFONE,
                        CPF,
                        ANIMAL_ID
                    FROM
                        CLIENTE
                    WHERE
                        ID = %s
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()

            if registro is None:
                return None
            
            animal = self._animal_dao.get_by_id(
                registro[4]
            )
            return Cliente(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                animal
            )

        finally:

            self.desconectar(cursor, conexao)

    def update(self, cliente):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    UPDATE CLIENTE
                    SET
                        NOME = %s,
                        TELEFONE = %s,
                        CPF = %s,
                        ANIMAL_ID = %s
                    WHERE
                        ID = %s
                    """
            
            cursor.execute(
                sql,
                (
                    cliente.nome,
                    cliente.telefone,
                    cliente.cpf,
                    cliente.animal.id,
                    cliente.id
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
                    FROM CLIENTE
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
            
        
