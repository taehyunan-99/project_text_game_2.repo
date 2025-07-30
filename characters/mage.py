import time

from .character import Character

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, cls_name="🪄 마법사", level=1, hp=100, max_hp=100, power=20, win_count=0, life_point=3)

    def attack(self, target):
        target.take_damage(self.power)
    
    def special_attack(self, target):
        target.take_damage(self.power * 2)
        if target.hp > 0:
            time.sleep(1)
            print("⏰ 시간 조작 마법을 사용하여 한 턴 더 플레이합니다. ⏰\n")
