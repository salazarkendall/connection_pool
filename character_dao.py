from character import Character
from cursor import PoolCursor


class CharacterDAO:
    _SELECT_CHARACTER = 'SELECT * FROM characters WHERE character_id=%s'
    _SELECT_ALL = 'SELECT * FROM characters'
    _INSERT = 'INSERT INTO characters(character_name, character_power) VALUES (%s,%s)'
    _UPDATE = 'UPDATE characters SET character_name =%s, character_power = %s WHERE character_id=%s'
    _UPDATE_NAME = 'UPDATE characters SET character_name =%s WHERE character_id=%s'
    _UPDATE_POWER = 'UPDATE characters SET character_power = %s WHERE character_id=%s'
    _DELETE = 'DELETE FROM characters WHERE character_id=%s'

    @classmethod
    def select_character(cls, character_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_CHARACTER, (character_id,))
            main_character = cursor.fetchone()
            return Character(main_character[1], main_character[2])

    @classmethod
    def select_all(cls):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT_ALL)
            data = cursor.fetchall()
            characters = []
            for character in data:
                new_character = Character(character[1], character[2])
                characters.append(new_character)
            return characters

    @classmethod
    def insert(cls, character):
        with PoolCursor() as cursor:
            cursor.execute(cls._INSERT, (character.character_name, character.character_power))
            return cursor.rowcount

    @classmethod
    def update_name(cls, character_name, character_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._UPDATE_NAME, (character_name, character_id))
            return cursor.rowcount

    @classmethod
    def update_power(cls, character_power, character_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._UPDATE_POWER, (character_power, character_id))
            return cursor.rowcount

    @classmethod
    def update_character(cls, character_name, character_power, character_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._UPDATE, (character_name, character_power, character_id))
            return cursor.rowcount

    @classmethod
    def delete(cls, character_id):
        with PoolCursor() as cursor:
            cursor.execute(cls._DELETE, (character_id,))
            return cursor.rowcount


if __name__ == '__main__':
    # data = CharacterDAO.select_all()
    # for character in data:
    #     print(f'{character} -----')
    #     print(type(character))
    #
    # my_character = CharacterDAO.select_character(1)
    # print(my_character)
    # print(type(my_character))

    print(CharacterDAO.delete(4))

    # print(naruto)
    # print(CharacterDAO.insert(naruto))
