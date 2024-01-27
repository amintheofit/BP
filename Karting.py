import random

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.score = 0

    def play_round(self, opponent, card_a, card_b, card_c):
        cards = [card_a, card_b, card_c]

        self.play_card(cards, opponent)
        opponent.play_card(cards, self)

    def play_card(self, cards, opponent):
        chosen_card = random.choice(cards)

        if chosen_card == 'A':
            damage = cards['A']
        elif chosen_card == 'B':
            damage = cards['B']
        else:
            damage = cards['C']

        if damage > opponent.play_opponent_card(cards):
            self.score += 1

    def play_opponent_card(self, cards):
        chosen_card = random.choice(list(cards.keys()))
        return cards[chosen_card]

    def take_damage(self, damage):
        self.health -= damage

if __name__ == "__main__":
    try:
        names = input().split()
        healths = list(map(int, input().split()))
        damages = dict(zip(['A', 'B', 'C'], map(int, input().split())))

        player1 = Player(names[0], healths[0])
        player2 = Player(names[1], healths[1])

        for _ in range(3):
            player1.play_round(player2, damages)
        
        with open("result.txt", "w") as f:
            f.write(f"{player1.name} -> Score: {player1.score}, Health: {player1.health}\n")
            f.write(f"{player2.name} -> Score: {player2.score}, Health: {player2.health}\n")

    except ValueError:
        print("Invalid Command.")
