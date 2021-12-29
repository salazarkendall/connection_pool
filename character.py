class Character:
    def __init__(self, character_name, character_power):
        self._character_name = character_name
        self._character_power = character_power

    def __str__(self):
        return f'{self._character_name}: {self._character_power}'

    @property
    def character_name(self):
        return self._character_name

    @character_name.setter
    def character_name(self, value):
        self.character_name = value

    @property
    def character_power(self):
        return self._character_power

    @character_power.setter
    def character_power(self, value):
        self.character_power = value


if __name__ == '__main__':
    my_character = Character(character_name='Osvaldo', character_power='Teach')
    print(my_character)