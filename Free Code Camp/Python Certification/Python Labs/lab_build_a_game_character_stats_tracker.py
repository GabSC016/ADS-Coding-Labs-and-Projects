# Lab: Build a Game Character Stats Tracker
# In this lab, you'll build a game character stats tracker. The program will allow you to create a character with specific attributes, update those attributes, and retrieve the current stats of the character.

class GameCharacter:
    def __init__ (self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1
    
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self._health = 0
        if new_health >= 0 and new_health <= 100:
            self._health = new_health
    
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0:
            self._mana = 0
        if 0 <= new_mana <= 50:
            self._mana = new_mana
    
    @property
    def level(self):
        return self._level
    
    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self._name} leveled up to {self._level}!")
    
    def __str__(self):
        character_stats = ''
        character_stats += f'Name: {self._name}\n'
        character_stats += f'Level: {self._level}\n'
        character_stats += f'Health: {self._health}\n'
        character_stats += f'Mana: {self._mana}'

        return character_stats