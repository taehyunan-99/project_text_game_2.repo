import random
import time

from .character import Character

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name,cls_name="🎲 도적", level=1, hp=100, max_hp=100, power=5, win_count=0, life_point=3)
    
    def attack(self, target):
        time.sleep(1)
        random_dice = random.randint(1,6)
        print(f"🎲 주사위를 굴려 {random_dice}의 추가 피해를 입혔습니다. 🎲\n")
        target.take_damage(self.power + random_dice)
    
    def special_attack(self, target):
        random_dice = random.randint(1,6)
        time.sleep(1)
        if random_dice == 6:
            target.take_damage(self.power * 4)
            print(f"🎲 주사위를 굴려 4배의 추가 피해를 입혔습니다. 🎲\n")
        elif random_dice > 3:
            target.take_damage(self.power * 3)
            print(f"🎲 주사위를 굴려 3배의 추가 피해를 입혔습니다. 🎲\n")
        else:
            target.take_damage(self.power * 2)
            print(f"🎲 주사위를 굴려 2배의 추가 피해를 입혔습니다. 🎲\n")