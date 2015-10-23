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
		value of 11 is evaluated and assigned in handValue below.
		"""
		if self.rank == 'Ace':
			return 1 
		elif self.rank == 'Jack' or self.rank == 'Queen' or self.rank == 'King':
			return 10
		else:
			return int(self.rank)

	def __str__(self):
		"""Returns values of cards in a pretty print format.
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
		An enumerated list of Card objects. Useful for implementing the mergeSort
		function below.
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

	def mergeSort(self):
		"""Sorts the remaining cards back into standard order. 
		"""
		def mergeSortInt(list_): #internal function to avoid complications with
								 #recursively calling deck object. 
			result = []
			if len(list_) < 2:
				return list_
			mid = len(list_) // 2
			left_list = mergeSortInt(list_[:mid]) # recursive call
			right_list = mergeSortInt(list_[mid:])# recursive call
			i = 0
			j = 0
			while i < len(left_list) and j < len(right_list):
				if left_list[i] > right_list[j]:
					result.append(right_list[j])
					j += 1
				else:
					result.append(left_list[i])
					i += 1
			result += left_list[i:]
			result += right_list[j:]
			return result

		game_deck = self.game_deck
		sorted_ = mergeSortInt(game_deck)
		return sorted_

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
		"""The total value of a hand.  This function handles aces in a nested
		function, ace_eval(). See below for additional information.

		Output:
		--------
		List of black card values, which are passed to ace_eval for further 
		processing of aces.
		"""
		total = []
		for item in self.current_hand: 
			index, card_obj = item
			total.append(card_obj.BJValue())
		
		def ace_eval(total):
			"""Checks for aces in the hand and recusively updates values to 11
			if advantageous to the total score. 

			Example:
			--------
			Ace of Hearts, 8 of Clubs --> 19
			Ace of Hearts, 8 of Clubs, 2 of Diamonds --> 11

			Output:
			-------
			The total integer value of all cards in a hand, after assigning values
			to Aces. 
			"""
			for item in total:
				if item == 1: # Checks for any aces.
					if sum(total) -1 + 11 <= 21: #Checks to see if 11 would be 
					                             #a better value for Ace and 
					                             #adds it to a new list.
						total.remove(1)
						total.append(11)
						ace_eval(total) 
					else:
						continue
			return sum(total)
		
		total_ace = ace_eval(total)
		return total_ace		

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
	"""
	test_deck.shuffleDeck()
	print(test_deck.game_deck)
	a = test_deck.mergeSort()
	print(a)
	"""
	card1 = test_deck.game_deck.pop(0) #Ace of Clubs
	print(card1[1])
	card2 = test_deck.game_deck.pop(12) #7 of Clubs (index is two less)
	print(card2[1])
	test_hand.addCard(card1)
	test_hand.addCard(card2)
	print(test_hand.handValue())
	card3 = test_deck.game_deck.pop(13)
	test_hand.addCard(card3)
	print(card3[1])
	print(test_hand.handValue())
