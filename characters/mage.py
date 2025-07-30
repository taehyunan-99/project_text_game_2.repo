from .character import Character

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, level=1, hp=100, max_hp=100, power=10)

    def attack(self, target):
        target.take_damage(self.power)
    
    def special_attack(self, target):
        target.take_damage(self.power * 2)
    
    def show_status(self):
        super().show_status()
        print("특수 공격 : ")
        print()