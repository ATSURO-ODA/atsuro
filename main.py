from __future__ import annotations
import random
from enum import Enum


class Hand(Enum):
    ROCK = 0
    SCISSORS = 1
    PAPER = 2

    def is_winning(self, other_hand: Hand) -> bool:
        return (
            self.value < other_hand.value
            or self == Hand.PAPER
            and other_hand == Hand.ROCK
        )


def hand_from_str(hand_str: str) -> Hand:
    if hand_str == "グー":
        return Hand.ROCK

    if hand_str == "チョキ":
        return Hand.SCISSORS

    if hand_str == "パー":
        return Hand.PAPER

    raise ValueError("グー、チョキ、パー以外の値は入力できません")


class Rps_Ai:
    CHOICE_LIST = [Hand.ROCK, Hand.SCISSORS, Hand.PAPER]

    def get_ai_choice(self) -> Hand:
        return random.choice(self.CHOICE_LIST)

    def game(self) -> bool:
        player_score = 0
        ai_score = 0

        player_choice = input(
            "グー、チョキ、パー(終了する場合はqと入力してください)のいずれかを入力してください："
        )
        player_hand = hand_from_str(player_choice)

        ai_hand = self.get_ai_choice()

        if player_choice == "q":
            print("終了します")
            return False

        elif player_choice == ai_hand:
            print("あいこ")

        elif player_hand.is_winning(ai_hand):
            print("プレイヤーの勝ちです")
            player_score += 1

        else:
            print("AIの勝ちです")
            ai_score += 1

        print(f"\n最終スコア - プレイヤー: {player_score}, AI: {ai_score}")

    def play_game(self) -> None:
        for _ in range(10):
            if not self.game():
                break


def main():
    ai = Rps_Ai()
    ai.play_game()


if __name__ == "__main__":
    main()
