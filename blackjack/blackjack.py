
from random import randint, shuffle
import sys
import os

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
		self.identity = "p"
	def get_number(self):
		return self.number
	def hit(self, deck):
		if self.number > 21:
			print("BUST")
			exit()
		holder_list = (deck.deal_card(),)
		# if holder_list[0][0] == 'A':
		# 	oneoreleven = str(input(('Do you want the ace to be played as a value of 1 or 11 [1/11]')))
		# 	if oneoreleven == '1':
		# 		self.number += VALUES[holder_list[0][0]]
		# 	else:
		# 		self.number += 11
		print("The card you have been dealt is: ")
		if holder_list[0][0] == 'A':
			val = str(input("Do you want the ace to be worth 1 or 11? "))
			if val == '1':
				self.number += 1
			if val == '11':
				self.number += 11
		else:
			self.number += VALUES[holder_list[0][0]]

		print(holder_list[0])
		if self.number > 21:
			print("BUST")
			exit()
		print("You are currently at a total of " + str(self.number))

class Dealer:
	def __init__(self):
		self.number = 0
		self.numbershowing = 0
		self.identity = "d"
	def get_number(self):
		return self.number + self.numbershowing
	def get_number_showing(self):
		return self.numbershowing
	def hit(self, deck):
		if self.number > 21:
			print("BUST")
			exit()
		holder_list = (deck.deal_card(),)
		self.number += VALUES[holder_list[0][0]]
		print("The card the dealer was dealt is: ")
		print(holder_list[0])
		if self.number > 21:
			print("DEALER BUST, YOU WIN")
			exit()
		print("The dealer is currently at a total of currently at a todal of " + str(self.number))

class Game:
	os.system('clear')
	print("=*="*20)
	print("Welcome to Blackjack")
	print("=*="*20)
	deck = Deck()
	deck.shuffle()
	player = Player()
	dealer = Dealer()
	playerturn = True
	dealerturn = False
	player_starting_cards = (deck.deal_card(), deck.deal_card())
	dealer_starting_cards = (deck.deal_card(), deck.deal_card())
	# print( player_starting_cards)
	# print( dealer_starting_cards)
	if player_starting_cards[0][0] and player_starting_cards[1][0] in VALUES:
		print("Here are your cards: ")
		print(player_starting_cards)
		if player_starting_cards[0][0] == 'A':
			val = str(input("Do you want the ace to be worth 1 or 11? "))
			if val == '1':
				player.number += 1
			if val == '11':
				player.number += 11
			player.number += VALUES[player_starting_cards[1][0]]
		elif player_starting_cards[1][0] == 'A':
			val = str(input("Do you want the ace to be worth 1 or 11? "))
			if val == '1':
				player.number += 1
			if val == '11':
				player.number += 11
			player.number += VALUES[player_starting_cards[0][0]]

		else:
			player.number += VALUES[player_starting_cards[0][0]] + VALUES[player_starting_cards[1][0]]
		print("You are currently at a total of " + str(player.number))
	if dealer_starting_cards[0][0] in VALUES:
		dealer.numbershowing = dealer_starting_cards[0]
		dealer.number += VALUES[dealer_starting_cards[0][0]]
		print("Here is what the dealer has showing: ")
		print(dealer.numbershowing)
	if dealer_starting_cards[1][0] in VALUES:
		dealer.number += VALUES[dealer_starting_cards[1][0]]
	while playerturn == True:
		hit_or_stay = input("Would you like to hit or stay? [h/s]").lower()
		if player.number <= 21:
			if hit_or_stay == 'h':
				player.hit(deck)
			if hit_or_stay == 's':
				playerturn = False
				dealerturn = True
		elif player.number > 21:
			print("BUST")
			exit()
	while dealerturn == True:
		print("\n")
		print("The dealer has flipped the card facing down, revealing the: ")
		print(dealer_starting_cards[1])
		print("The dealers total is: " + str(dealer.number))
		while dealerturn == True:	
			stay_list = [17, 18, 19, 20, 21]
			if dealer.number <= 16:
				print("Dealer has to hit")
				dealer.hit(deck)
			if dealer.number in stay_list:
				dealerturn = False
				print("Dealer stays")
			elif dealer.number > 21:
				print("DEALER BUST, YOU WIN")
				exit()
		if dealer.number >= player.number:
			print("Dealer wins")
			exit()
		else:
			print("You win")


Game()
# betting with chips
# 21 dealt
# gui