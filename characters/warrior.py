from .character import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, level=1, hp=100, max_hp=100, power=10)

    def attack(self, target):
        target.take_damage(self.power)
    
    def special_attack(self, target):
        if self.hp < 30:
            target.take_damage(self.power * 3)
            self.hp += 30
            print(f"체력 20 흡수\n현재 체력 : {self.hp} ")

    def show_status(self):
        super().show_status()
        print("특수 공격 : 현재 체력이 30 미만인 경우 3배의 데미지로 공격하고 hp 20을 흡수한다.")
        print()
    



