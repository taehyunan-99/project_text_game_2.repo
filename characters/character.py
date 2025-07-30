from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, cls_name, level, hp, max_hp, power, win_count, life_point):
        super().__init__()
        self.name = name
        self.cls_name = cls_name
        self.level = level
        self.hp = hp
        self.max_hp = max_hp
        self.power = power
        self.win_count = win_count
        self.life_point = life_point

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
        print("📜 [ 캐릭터 스텟 ] 📜\n")
        print(f"캐릭터 이름 : {self.name}")
        print(f"직업 : {self.cls_name}")
        print(f"현재 레벨 : {self.level}")
        print(f"현재 체력 : {self.hp}")
        print(f"현재 공격력 : {self.power}")
        print(f"승리 횟수 : {self.win_count}")
        print(f"라이프 포인트 : {self.life_point}\n")

    def reset_hp(self):
        self.hp = self.max_hp

    def level_up(self):
        self.level += 1
        print("🎉 Level Up!! 🎉\n")
        self.max_hp += 25
        print("체력 + 25")
        self.power += 10
        print("공격력 + 10\n")
        self.reset_hp()