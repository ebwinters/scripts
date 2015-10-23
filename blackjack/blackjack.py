
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

	def shuffle(self):
		shuffle(self.deck)
		return(self.deck)
	def deal_card(self):
		dealt = self.deck.pop()
		return([dealt.value, dealt.suit])
	

class Player:
	def __init__(self):
		self.number = 0
	def get_number(self):
		return self.number
class Dealer:
	def __init__(self):
		self.number = 0
		self.numbershowing = 0
	def get_number(self):
		return self.number + self.numbershowing
	def get_number_showing(self):
		return self.numbershowing

class Game:
	deck = Deck()
	deck.shuffle()
	player = Player()
	dealer = Dealer()
	player_starting_cards = (deck.deal_card(), deck.deal_card())
	dealer_starting_cards = (deck.deal_card(), deck.deal_card())
	print( player_starting_cards)
	print( dealer_starting_cards)
	if player_starting_cards[0][0] and player_starting_cards[1][0] in VALUES:
		print(VALUES[player_starting_cards[0][0]])
		print(VALUES[player_starting_cards[1][0]])
		player.number += VALUES[player_starting_cards[0][0]] + VALUES[player_starting_cards[1][0]]
		print(player.number)
	if dealer_starting_cards[0][0] in VALUES:
		dealer.numbershowing = dealer_starting_cards[0][0]
		dealer.number += VALUES[dealer_starting_cards[0][0]]
		print(dealer.numbershowing)
	if dealer_starting_cards[1][0] in VALUES:
		dealer.number += VALUES[dealer_starting_cards[1][0]]
		print(dealer.number)
	




	def hit(self, player):
		pass
	def stay(self, player):
		pass

	
	#create dealer and player
	#deal player, dealer
	#ask for hit or not 
Game()
