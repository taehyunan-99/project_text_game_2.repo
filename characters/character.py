from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, level, hp, max_hp, power):
        super().__init__()
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = max_hp
        self.power = power

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def special_attack(self, target):
        pass

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def alive(self):
        if self.hp <= 0:
            return False
        
    def show_status(self):
        print(f"캐릭터 이름 : {self.name}")
        print(f"현재 레벨 : {self.level}")
        print(f"현재 체력 : {self.hp}")
        print(f"현재 공격력 : {self.power}")

    def reset_hp(self):
        self.hp = self.max_hp