
from random import shuffle

class Card:

    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,
               "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    # The case, c2 is greater.
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
        return False

    # The case, c2 is smaller.
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
        return False

    def __repr__(self):
        r = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return r

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        player1 = input("プレイヤー１の名前： ")
        player2 = input("プレイヤー２の名前： ")
        self.deck = Deck()
        self.p1 = Player(player1)
        self.p2 = Player(player2)

    def print_wins(self, winner):
        w = "今回のこのゲームは {} が勝ちました!"
        print(w.format(winner.name))

    def print_draw(self, p1, p2):
        d = "{} は {} を引き、{} は {}を引きました。"
        print(d.format(p1.name, p1.card, p2.name, p2.card))

    def play_game(self):
        cards = self.deck.cards
        print("それではゲームを始めます。")
        while len(cards) >= 2:
            msg = "ゲームを終了したい場合は [q] を押します。" \
                  "それ以外でゲーム続行です。\n"
            answer = input(msg)
            if answer == 'q':
                break

            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_wins(self.p1)
            else:
                self.p2.wins += 1
                self.print_wins(self.p2)

        win = self.winner(self.p1, self.p2)
        print("ゲーム終了！このゲームは {} の勝利です！".format(win))

    def winner(self, p1 , p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name

        return "このゲームは引き分けです！"



game = Game()
game.play_game()