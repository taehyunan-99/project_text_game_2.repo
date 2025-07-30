import time

from characters.character import Character

class Slime(Character):
    def __init__(self):
        super().__init__(name="슬라임", cls_name="몬스터", level=1, hp=70, max_hp=70, power=6, win_count=0, life_point=1)

    def attack(self, target):
        target.take_damage(self.power)
    
    def special_attack(self, target):
        time.sleep(1)
        target.take_damage(self.power + 4)
        self.hp += 5
        print("🟢 '슬라임'이 체력을 흡수하였습니다. 🟢\n")
