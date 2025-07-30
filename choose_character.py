from characters import Warrior, Mage, Rogue
import time

class ChossCharacter:
    def choose_character(self):
        user_name = input("이름을 입력해주세요 :")
        print()
        time.sleep(1)
        print("[ 1. 전사 / 2. 마법사 / 3. 도적 ]")
        select_num = input("캐릭터를 선택해주세요(ex: 1) :")
        print()
        if select_num == "1":
            time.sleep(1)
            print("'전사'를 선택하셨습니다!")
            print()
            return Warrior(user_name)
        elif select_num == "2":
            time.sleep(1)
            print("'마법사'를 선택하셨습니다!")
            print()
            return Mage(user_name)
        elif select_num == "3":
            time.sleep(1)
            print("'도적'를 선택하셨습니다!")
            print()
            return Rogue(user_name)
        else:
            print("잘못된 입력입니다.")
            print()
        

    def enemy_character(self):
        time.sleep(1)
        print("[ 1. 전사 / 2. 마법사 / 3. 도적 ]")
        select_num = input("상대 캐릭터를 선택해주세요(ex: 1) :")
        print()
        if select_num == "1":
            time.sleep(1)
            print("상대로 '전사'를 선택하셨습니다!")
            print()
            return Warrior("enemy")
        elif select_num == "2":
            time.sleep(1)
            print("상대로 '마법사'를 선택하셨습니다!")
            print()
            return Mage("enemy")
        elif select_num == "3":
            time.sleep(1)
            print("상대로 '도적'를 선택하셨습니다!")
            print()
            return Rogue("enemy")
        else:
            print("잘못된 입력입니다.")
            print()