import random


class RPS_AI:
    CHOICE_LIST = ["グー", "チョキ", "パー"]

    def get_ai_choice(self) -> str:
        return random.choice(self.CHOICE_LIST)

    def game(self) -> Bool:
        playerscore = 0
        AIscore = 0

        player_choice = input(
            "グー、チョキ、パー(終了する場合はqと入力してください)のいずれかを入力してください："
        )
        ai_choice = self.get_ai_choice()

        if player_choice == "q":
            print("終了します")
            return False

        elif player_choice == ai_choice:
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

    def play_game(self) -> None:
        for _ in range(10):
            if not self.game():
                break


def main():
    ai = RPS_AI()
    ai.play_game()


if __name__ == "__main__":
    main()
