from characters import Warrior, Mage, Rogue
import random
import time

class BattleManager:
    def __init__(self):
        self.coin = False

    # 선후공 정하기 코인 토스
    def coin_toss(self):
        time.sleep(1)
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
                    print("코인 토스에 승리하여 선공으로 시작합니다!\n")
                    self.coin = True
                    break
                else:
                    print("코인 토스에 패배하여 후공으로 시작합니다!\n")
                    self.coin = False
                    break
            else:
                print("잘못된 입력입니다!\n")

    # 배틀 페이지
    def start_battle(self, user, enemy):
        while user.hp > 0 and enemy.hp > 0:
            random_num = random.randint(1,100)
            if self.coin:
                print("🟦 User Turn\n")
                if random_num > 30:
                    # 유저 일반 공격
                    time.sleep(1)
                    print("🗡️")
                    print("공격에 성공했습니다!\n")
                    user.attack(enemy)
                    time.sleep(1)
                    print(f"✅ 상대 남은 체력 : {enemy.hp}\n")
                    time.sleep(1)
                else:
                    # 유저 특수 공격
                    time.sleep(1)
                    print("💥")
                    print("특수 공격에 성공해 큰 피해를 입혔습니다!\n")
                    user.special_attack(enemy)
                    time.sleep(1)
                    print(f"✅ 상대 남은 체력 : {enemy.hp}\n")
                    if user.cls_name == "🪄 마법사":
                        self.coin = not self.coin
                    time.sleep(1)
                self.coin = not self.coin
            else:
                print("🟥 Enemy Turn\n")
                if random_num > 20:
                    # 상대 일반 공격
                    time.sleep(1)
                    print("🗡️")
                    print("상대의 공격에 당했습니다!\n")
                    enemy.attack(user)
                    time.sleep(1)
                    print(f"✅ 현재 남은 체력 : {user.hp}\n")
                    time.sleep(1)
                else:
                    # 상대 특수 공격
                    time.sleep(1)
                    print("💥")
                    print("상대의 특수 공격에 당해 큰 피해를 입었습니다!\n")
                    enemy.special_attack(user)
                    time.sleep(1)
                    print(f"✅ 현재 남은 체력 : {user.hp}\n")
                    time.sleep(1)
                self.coin = not self.coin
        print("📜 [ 전투 결과 ] 📜\n")
        if user.hp > 0:
            print("🏆 승리 🏆\n")
            user.win_count += 1
            user.reset_hp()
        else:
            print("💀 패배 💀\n")
            user.life_point -= 1
            user.reset_hp()




