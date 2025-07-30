from .character import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, cls_name="🛡️ 전사", level=1, hp=110, max_hp=100, power=10, win_count=0, life_point=3)

    def attack(self, target):
        target.take_damage(self.power)
    
    def special_attack(self, target):
        if self.hp < 40:
            target.take_damage(self.power * 3)
            self.hp += 10
            print(f"🛡️ 체력 10 흡수 🛡️\n현재 체력 : {self.hp}\n")
        else:
            target.take_damage(self.power * 2)