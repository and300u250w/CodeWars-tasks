# Create a function that returns the name of the winner in a fight between two fighters.

# Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

# Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

# Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

# Example:
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__ = __str__


def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here

    while True:
        if first_attacker in fighter1.name and fighter1.health > 0:
            fighter2.health - = fighter1.damage_per_attack
            if fighter2.health > 0:
                fighter1.health - = fighter2.damage_per_attack
            elif fighter2.health < 0:
                print (fighter1.name + " Won this game")
                break
            elif fighter1.health < 0:
              print (fighter2.name + " Won this game")
              break
        else:
            fighter1.health - = fighter2.damage_per_attack
            if fighter1.health > 0:
                fighter2.health - = fighter1.damage_per_attack
            elif fighter2.health < 0:
                print (fighter1.name + " Won this game")
                break
            elif fighter1.health < 0:
                print (fighter2.name + " Won this game")
                break


declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew")
# , "Lew")

declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Harry")
# ,"Harry")



# def declare_winner(fighter1, fighter2, first_attacker):
#     cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
#     while cur.health > 0:
#         opp.health -= cur.damage_per_attack
#         cur, opp = opp, cur
#     return opp.name