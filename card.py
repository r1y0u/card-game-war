
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
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    # The case, c2 is smaller.
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        r = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return r

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(0, 4):
                self.cards.append(i, j)
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.Name = name

class Game:
    def __init__(self):
        player1 = input("プレイヤー１の名前： ")
        player2 = input("プレイヤー２の名前： ")
        self.deck = Deck()
        self.p1 = Player(player1)
        self.p2 = Player(player2)

    def wins(self, winner):
        w = "今回のこのゲームは{}が勝ちました!"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} は｛｝を引き、{} は {}を引きました。"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("それではゲームを始めます。")
        while len(cards) >= 2:
            msg = "ゲームを終了したい場合は [q] を押します。" \
                  "それ以外でゲーム続行です。"
            res = input(msg)
            if res == q:
                break

            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)

            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

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