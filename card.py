class Card:

    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [ None, None,
               "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    def __init__(self, s, v):
        self.suit = s
        self.value = v

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
            if self.suit > c2.value:
                return True
            else:
                return False
        return False

    def __repr__(self):
        r = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return r






