from characters import Warrior, Mage, Rogue
from monsters import Slime, Goblin, Dragon
import time

class ChossCharacter:
    def choose_character(self):
        user_name = input("이름을 입력해주세요 :")
        print()
        time.sleep(1)
        print("🔽 나의 직업 선택 🔽\n")
        print("1. 🛡️ 전사\n2. 🪄 마법사\n3. 🎲 도적\n")
        select_num = input("캐릭터를 선택해주세요(ex: 1) :")
        print()
        if select_num == "1":
            time.sleep(1)
            print("✅ '전사'을/를 선택하셨습니다!")
            print()
            return Warrior(user_name)
        elif select_num == "2":
            time.sleep(1)
            print("✅ '마법사'을/를 선택하셨습니다!")
            print()
            return Mage(user_name)
        elif select_num == "3":
            time.sleep(1)
            print("✅ '도적'을/를 선택하셨습니다!")
            print()
            return Rogue(user_name)
        else:
            print("잘못된 입력입니다.")
            print()
        time.sleep(1)

    def enemy_character(self):
        time.sleep(1)
        print("🔽 상대 몬스터 선택 🔽\n")
        print("1. 🟢 슬라임 Lv 1\n2. 👺 고블린 Lv 2\n3. 🐲 드래곤 Lv 3\n")
        select_num = input("상대 몬스터를 선택해주세요(ex: 1) :")
        print()
        if select_num == "1":
            time.sleep(1)
            print("✅ 상대로 '슬라임'을/를 선택하셨습니다!")
            print()
            return Slime()
        elif select_num == "2":
            time.sleep(1)
            print("✅ 상대로 '고블린'을/를 선택하셨습니다!")
            print()
            return Goblin()
        elif select_num == "3":
            time.sleep(1)
            print("✅ 상대로 '드래곤'을/를 선택하셨습니다!")
            print()
            return Dragon()
        else:
            print("잘못된 입력입니다.")
            print()