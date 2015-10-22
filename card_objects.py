# Card and Deck objects for blackjack.py
# This objects are intended to be reusable for future card games.
__author__ = "Kevin Saavedra"

import random

class Card(object):
	"""
	A class for generating standard attributes for playing cards. Class 
	definitions inspired by John Zelle's "Python Programming" 2nd ed.
	"""
	def __init__(self, rank, suit):
		"""Return a Card object with rank and suit value.
		"""
		self.rank = rank
		self.suit = suit
		
	def getRank(self):
		"""Returns the rank of the card.
		"""
		return self.rank

	def getSuit(self):
		"""Returns the suit of the card.
		"""
		return self.suit

	def BJValue(self):
		"""Returns the blackjack value of the card as an integer. 
		Example:
		-------
		2 == 2; King == 10
		Note: An ace is given the default value of 1 here.  The alternative
		value of 11 is assigned in blackjack.py.
		"""
		if self.rank == 'Ace':
			return 1 
		elif self.rank == 'Jack' or self.rank == 'Queen' or self.rank == 'King':
			return 10
		else:
			return int(self.rank)

	def __str__(self):
		"""Returns values of cards in a natural-sounding format.
		Example:
		--------
		Two of Spades, Queen of Hearts
		"""
		return('{0} of {1}'.format(self.rank, self.suit))

class Deck(object):
	"""A class for generating a deck of cards.
	"""
	def __init__(self):
		"""Constructs a deck of 52 cards. This function will create a deck
		using the traditional French suits with the suit order Clubs, Diamonds,
		Hearts, and Spades. 
		Output:
		-------
		An enumerated list of Card objects.
		"""
		self.game_deck = []
		for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
			for num in ['Ace','2', '3', '4', '5', '6', '7', '8', '9', '10',
							'Jack', 'Queen', 'King']:		
				self.game_deck.append(Card(num, suit))
		self.game_deck = list(enumerate(self.game_deck)) #Enumerate for easy
														 #sorting later.

	def shuffleDeck(self):
		"""Shuffles a deck of cards.
		"""
		return random.shuffle(self.game_deck)

	def drawCard(self):
		"""Returns the value of the top card and subtracts that value from 
		the deck.
		"""
		top_card = self.game_deck[0]
		self.game_deck.pop(0)
		return top_card

	def cardsLeft(self):
		return len(self.game_deck)

	def sort(self):
		"""Sorts the remaining cards back into standard order. Thunder suggested
		merge sort (that magnificent bastard!)
		"""
		pass # Write me!!!! Bite me!!!!


class Hand(object):
	"""a class for storing the draw_card objects.
	"""
	def __init__(self, name):
		"""An empty list"""
		self.current_hand = []
		self.name = name

	def addCard(self, card):
		"""Adds a card to current_hand.
		"""
		return self.current_hand.append(card)
		
	def subtractCard(self, card):
		"""Removes a card from current_hand.
		"""
		return self.current_hand.remove(card)

	def handValue(self):
		"""The total value of a hand !!!!!NOT YET TESTED IN TEST FILE!!!!!!
		"""
		total = []
		for item in self.current_hand: 
			index, card_obj = item
			total.append(card_obj.BJValue())
		total_ace = []
		for item in total:
			if item == 1:
				if sum(total) - 1 + 11 <= 21: #Checks to see if 11 would be a
											  #better value for Ace.
					total_ace.append(11)
					continue
				else:
					total_ace.append(1)
			else:
				total_ace.append(item)
		return sum(total_ace)

class Player(object):
	"""A class that plays a hand of cards.
	"""
	def __init__(self, name, hand):
		"""Returns a Player object whose name is 'name' and contains a hand
		"""
		self.name = name
		self.hand = hand

if __name__ == '__main__':
	test_hand = Hand("test")
	player = Player(Player, test_hand)
	test_deck = Deck()
	"""for item in test_deck.game_deck:
		index, card_object = item
		print(index, card_object.__str__())"""
	card1 = test_deck.game_deck.pop(0) #Ace of Clubs
	print(card1[1])
	card2 = test_deck.game_deck.pop(12) #7 of Clubs (index is two less)
	print(card2[1])
	test_hand.addCard(card1)
	test_hand.addCard(card2)
	print(test_hand.handValue())
