"""
Warrior unit.
"""

from .base import Base


class Warrior(Base):
    def __init__(self, health = 10, strength = 10, stamina = 10, agility = 10):
        super().__init__(health, strength, stamina, agility)

        self.range = 1

        pass

