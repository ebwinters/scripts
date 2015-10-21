
from random import randint, shuffle

SUITS = ['C', 'S', 'D', 'H']
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
VALUES = {
	'A' : 1,
	'2' : 2,
	'3' : 3,
	'4' : 4,
	'5' : 5,
	'6' : 6,
	'7' : 7,
	'8' : 8,
	'9' : 9,
	'10' : 10,
	'J' : 10,
	'Q' : 10,
	'K' : 10,
}

class Card:
	def __init__(self, value, suit):
		if (suit in SUITS) and (value in RANKS):
			self.suit = suit
			self.value = value
	def get_suit(self):
		return self.suit
	def get_rank(self):
		return self.value

class Deck:
	def __init__(self):
		self.deck = []
		counter = 0
		suit = 0
		rank = 0
		for suit in SUITS:
			for rank in RANKS:
				self.deck.append(Card(rank, suit))
		while counter < len(self.deck):
			counter += 1

	def shuffle(self, card_list):
		shuffle(card_list)
		return( card_list)
	def deal_card(self, card_list):
		dealt = card_list.pop()
		return(dealt.value, dealt.suit)
		
deck = Deck()
deck.shuffle(deck.deck)
deck.deal_card(deck.deck)