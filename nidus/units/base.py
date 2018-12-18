"""
Base class for units.
"""


class Base(object):
    def __init__(self, owner_id, health, strength, stamina, agility):

        self.owner_id = owner_id
        self.health = health
        self.strength = strength
        self.stamina = stamina
        self.agility = agility

        self.experience = 0
        self.alive = True

        pass

    def is_alive(self):

        if self.health <= 0:
            self.alive = False

        return self.alive

    def take_damage(self, damage):
        self.health -= damage
        return
