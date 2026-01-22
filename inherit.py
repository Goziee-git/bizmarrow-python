class Thing:
   def __init__(self, price, strength, speed):
      self.price = price
      self.strength = strength
      self.speed = speed
   def printValues(self):
      print("""Price: {0!s}
      Strength: {1!s}
      speed: {2!s}
      """.format(self.price, self.speed, self.strength)
      )

class Weapon(Thing):
   def __init__(self, price, damage):
      super().__init__(self, price, strength, speed)
      self.damage = damage
   def printWeapon(self, **damage):
      print("""
      Price: {3!s}
      Damage: {text}""".format(self.price, damage = "weaponsold"))


class Itenary:
   def __init__(self, price,strength):
      self.price = price
      self.strength = strength

   