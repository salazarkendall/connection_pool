from connection import Connection
from persona import Persona


class PersonaDAO:
    _SELECT = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERT = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _UPDATE = 'UPDATE persona SET nombre=%s ,apellido=%s ,email=%s WHERE id_persona=%s'
    _DELETE = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def select(cls):
        with Connection.get_curs() as cursor:
            cursor.execute(cls._SELECT)
            data = cursor.fetchall()
            personas = []
            for info in data:
                persona = Persona(info[0], info[1], info[2], info[3])
                personas.append(persona)
            return personas

    @classmethod
    def insert(cls, persona):
        with Connection.get_conn():
            with Connection.get_curs() as cursor:
                values = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERT, values)
                return cursor.rowcount

    @classmethod
    def update(cls, persona):
        with Connection.get_conn():
            with Connection.get_curs() as cursor:
                values = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._UPDATE, values)

    @classmethod
    def delete(cls, persona):
        with Connection.get_conn():
            with Connection.get_curs() as cursor:
                values = (persona.id_persona,)
                cursor.execute(cls._DELETE, values)
                return cursor.rowcount


if __name__ == '__main__':
    # INSERT TEST
    # persona_test = Persona(
    #     email='tchami@gmail.com', nombre='Tobias', apellido='Casa'
    # )
    # PersonaDAO.insert(persona_test)

    # SELECT TEST
    # datos = PersonaDAO.select()
    # for persona in datos:
    #     log.info(persona)

    # UPDATE TEST
    # persona_test = Persona(
    #     email='jloria.com', nombre='Jefferson', apellido='Loria', id_persona=9
    # )
    # PersonaDAO.update(persona_test)

    # DELETE TEST
    PersonaDAO.delete(Persona(id_persona=3))
