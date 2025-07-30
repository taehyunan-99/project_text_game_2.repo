import time

from characters import Warrior, Mage, Rogue
from battle import BattleManager
from choose_character import ChossCharacter

battle = BattleManager()
user = ChossCharacter().choose_character()
enemy = ChossCharacter().enemy_character()


def start():
    battle.coin_toss()
    time.sleep(1)
    print("****전투 시작****")
    time.sleep(1)
    print()
    battle.start_battle(user, enemy)


start()
# user.show_status()