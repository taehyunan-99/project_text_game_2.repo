import random

from .character import Character

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, level=1, hp=100, max_hp=100, power=7)
    
    def attack(self, target):
        random_dice = random.randint(1,6)
        print(f"주사위를 굴려 {random_dice}의 추가 피해를 입혔습니다.")
        target.take_damage(self.power + random_dice)
    
    def special_attack(self, target):
        target.take_damage(self.power * 2)
        
    def show_status(self):
        super().show_status()
        print("특수 공격 : ")
        print()