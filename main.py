import random

mylist = ["グー", "チョキ", "パー"]


class RPS_AI:
    def __init__(self) -> None:
        pass

    def get_ai_choice(self):
        return random.choice(mylist)

    def play_game(self):
        playerscore = 0
        AIscore = 0

        for _ in range(10):
            player_choice = input("グー、チョキ、パーのいずれかを入力してください：")
            ai_choice = self.get_ai_choice()

            if player_choice == ai_choice:
                print("あいこ")

            elif (
                (player_choice == "グー" and ai_choice == "チョキ")
                or (player_choice == "チョキ" and ai_choice == "パー")
                or (player_choice == "パー" and ai_choice == "グー")
            ):
                print("プレイヤーの勝ちです")
                playerscore += 1

            else:
                print("AIの勝ちです")
                AIscore += 1

        print(f"\n最終スコア - プレイヤー: {playerscore}, AI: {AIscore}")


def main():
    ai = RPS_AI()
    ai.play_game()


if __name__ == "__main__":
    main()
