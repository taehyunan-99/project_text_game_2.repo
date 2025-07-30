from characters import Warrior, Mage, Rogue
import random
import time

class BattleManager:
    def __init__(self):
        self.start = False

    def coin_toss(self):
        time.sleep(2)
        coin = ["앞", "뒤"]
        print("코인 토스로 선공을 정합니다.")
        time.sleep(1)
        print()
        while True:
            user_coin = input("동전의 (앞/뒤)중 하나를 입력해주세요 :").strip()
            print()
            time.sleep(1)
            if user_coin in coin:
                if user_coin == random.choice(coin):
                    print("코인 토스에 승리하여 선공으로 시작합니다!")
                    self.start = True
                    print()
                    break
                else:
                    print("코인 토스에 패배하여 후공으로 시작합니다!")
                    self.start = False
                    print()
                    break
            else:
                print("잘못된 입력입니다!")
                print()

    def start_battle(self, user, enemy):
        while user.hp > 0 and enemy.hp > 0:
            random_num = random.randint(1,100)
            if self.start:
                if random_num > 30:
                    print("공격에 성공했습니다!")
                    user.attack(enemy)
                    print(f"상대 남은 체력 : {enemy.hp}")
                    print()
                    time.sleep(1)
                else:
                    print("특수 공격에 성공해 큰 피해를 입혔습니다!")
                    user.special_attack(enemy)
                    print()
                    print(f"상대 남은 체력 : {enemy.hp}")
                    print()
                    time.sleep(1)
                self.start = not self.start
            else:
                if random_num > 30:
                    print("상대의 공격에 당했습니다!")
                    enemy.attack(user)
                    print(f"현재 남은 체력 : {user.hp}")
                    print()
                    time.sleep(1)
                else:
                    print("상대의 특수 공격에 당해 큰 피해를 입었습니다!")
                    enemy.special_attack(user)
                    print(f"현재 남은 체력 : {user.hp}")
                    print()
                    time.sleep(1)
                self.start = not self.start
        print("[전투 결과]")
        print()
        if user.hp > 0:
            print("승리")
        else:
            print("패배")




