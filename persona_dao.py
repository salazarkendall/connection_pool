from cursor import PoolCursor
from persona import Persona


class PersonaDAO:
    _SELECT = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERT = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _UPDATE = 'UPDATE persona SET nombre=%s ,apellido=%s ,email=%s WHERE id_persona=%s'
    _DELETE = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def select(cls):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT)
            data = cursor.fetchall()
            personas = []
            for info in data:
                persona = Persona(info[0], info[1], info[2], info[3])
                personas.append(persona)
            return personas

    @classmethod
    def insert(cls, persona):
        with PoolCursor() as cursor:
            values = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERT, values)
            return cursor.rowcount

    @classmethod
    def update(cls, persona):
        with PoolCursor() as cursor:
            values = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._UPDATE, values)

    @classmethod
    def delete(cls, persona):
        with PoolCursor() as cursor:
            values = (persona.id_persona,)
            cursor.execute(cls._DELETE, values)
            return cursor.rowcount


if __name__ == '__main__':
    # SELECT TEST
    personas = PersonaDAO.select()
    for persona in personas:
        print(persona)

    # INSERT TEST
    # persona_test = Persona(email='gaga@gmail.com', nombre='Gabriel', apellido='Aguilar')
    # print(PersonaDAO.insert(persona_test))

    # UPDATE TEST
    persona_test = Persona(email='gilo@gmail.com', nombre='Alvaro', apellido='Aguilar', id_persona=33)
    PersonaDAO.update(persona_test)

    # DELETE TEST
    print(PersonaDAO.delete(Persona(id_persona=32)))
