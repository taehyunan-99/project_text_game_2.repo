import time

from characters.character import Character

class Dragon(Character):
    def __init__(self):
        super().__init__(name="드래곤", cls_name="몬스터", level=3, hp=150, max_hp=150, power=15, win_count=0, life_point=1)

    def attack(self, target):
        target.take_damage(self.power)
    
    def special_attack(self, target):
        time.sleep(1)
        if target.hp > 30:
            target.hp = target.hp // 2
        else:
            target.hp = 0
        print("🐲 '드래곤'이 브레스를 뿜었습니다. 🐲\n")