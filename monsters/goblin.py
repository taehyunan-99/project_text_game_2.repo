import time

from characters.character import Character

class Goblin(Character):
    def __init__(self):
        super().__init__(name="고블린", cls_name="몬스터", level=2, hp=100, max_hp=100, power=10, win_count=0, life_point=1)

    def attack(self, target):
        target.take_damage(self.power)
    
    def special_attack(self, target):
        time.sleep(1)
        target.take_damage(self.power * 2.5)
        print("👺 '고블린'이 찌르기 공격을 시전하였습니다. 👺\n")
