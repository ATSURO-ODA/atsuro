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


class RpsAi:
    CHOICE_LIST = [Hand.ROCK, Hand.SCISSORS, Hand.PAPER]

    def __init__(self) -> None:
        self.player_score = 0
        self.ai_score = 0

    def get_ai_choice(self) -> Hand:
        return random.choice(self.CHOICE_LIST)

    def get_player_choice(self) -> Hand:
        player_choice = input(
            "グー、チョキ、パー(終了する場合はqと入力してください)のいずれかを入力してください："
        )
        if player_choice == "q":
            print("終了します")
            quit()

        player_hand = hand_from_str(player_choice)

        return player_hand

    def game(self) -> None:
        player_hand = self.get_player_choice()

        ai_hand = self.get_ai_choice()

        if player_hand == ai_hand:
            print("あいこ")

        elif player_hand.is_winning(ai_hand):
            print("プレイヤーの勝ちです")
            self.player_score += 1

        else:
            print("AIの勝ちです")
            self.ai_score += 1

    def play_game(self) -> None:
        for _ in range(10):
            if not self.game():
                break
        print(f"\n最終スコア - プレイヤー: {self.player_score}, AI: {self.ai_score}")


def main():
    ai = RpsAi()
    ai.play_game()


if __name__ == "__main__":
    main()
