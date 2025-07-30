import time

from characters import Warrior, Mage, Rogue
from monsters import Slime, Goblin, Dragon
from battle import BattleManager
from choose_character import ChossCharacter

battle = BattleManager()

def info():
    time.sleep(1)
    check_info = input("💡 캐릭터 설명을 보시겠습니까? 💡\n(1 = 예 / 아무키나 입력시 나가기)\n")
    if check_info == "1":
        while True:
            time.sleep(1)
            print("1. 🛡️ 전사\n2. 🪄 마법사\n3. 🎲 도적\n")
            time.sleep(1)
            select_info = input("🔔 캐릭터를 선택해주세요(ex: 1) 🔔\n아무키나 입력시 나가기\n")
            time.sleep(1)
            if select_info == "1":
                print("🛡️ 전사 🛡️\n")
                time.sleep(1)
                print("기본 체급이 높으며 특수 능력으로 체력이 적을 때, 큰 피해를 입히고 체력을 흡수합니다.\n")
            elif select_info == "2":
                print("🪄 마법사 🪄\n")
                time.sleep(1)
                print("특수 능력으로 시간을 조작하여 한 턴 더 플레이합니다.\n")
            elif select_info == "3":
                print("🎲 도적 🎲\n")
                time.sleep(1)
                print("기본 체급은 가장 낮지만 모든 공격시 주사위를 굴려 추가 피해를 입힙니다.\n")
            else:
                break

def start():
    time.sleep(1)
    print("🎉 환영합니다!! 🎉\n")
    info()
    user = ChossCharacter().choose_character()
    while user.win_count < 3 and user.life_point > 0:
        win_check = user.win_count
        time.sleep(1)
        user.show_status()
        enemy = ChossCharacter().enemy_character()
        time.sleep(1)
        ready = input("⚔️ 전투를 시작하겠습니까? ⚔️\n(1 = 시작 / 아무키나 입력시 종료) \n").lower()

        if ready == "1":
            battle.coin_toss()
            time.sleep(1)
            print("⚔️ ****전투 시작**** ⚔️")
            time.sleep(1)
            print()
            battle.start_battle(user, enemy)
        else:
            print("🎮 게임을 종료합니다.")
            exit()
        
        if user.win_count > win_check and user.win_count < 3:
            time.sleep(1)
            user.level_up()

    # 승리 문구
    if user.win_count == 3:
        time.sleep(1)
        print("🎉 클리어를 축하드립니다!! 🎉\n")
        time.sleep(1)
        print("📜 [ 최종 스텟 ] 📜\n")
        time.sleep(1)
        print(f"캐릭터 이름 : {user.name}")
        time.sleep(0.5)
        print(f"직업 : {user.cls_name}")
        time.sleep(0.5)
        print(f"최종 레벨 : {user.level}")
        time.sleep(0.5)
        print(f"최종 체력 : {user.hp}")
        time.sleep(0.5)
        print(f"최종 공격력 : {user.power}")
        time.sleep(0.5)
        print(f"최종 승리 횟수 : {user.win_count}")
        time.sleep(0.5)
        print(f"남은 라이프 포인트 : {user.life_point}")
        print()
        time.sleep(1)
        print("✨ 감사합니다!! ✨")
    # 패배 문구
    else:
        time.sleep(1)
        print("라이프 포인트를 모두 소진하였습니다.\n")
        time.sleep(1)
        print("⚰️ Game Over ⚰️")

# 게임 실행
start()