# Card and Deck objects for gamescript.py
# This objects are intended to be reusable for future card games.

class Card(object):
	"""
	A class for generating standard attributes for playing cards.
	"""
	def __init__(self, rank, suit):
		"""Return a Card object with rank and suit value."""
		self.rank = rank
		self.suit = suit
		
	def getrank(self):
		"""Returns the rank of the card."""
		return self.rank

	def getSuit(self):
		"""Returns the suit of the card."""
		return self.suit

	def BJValue(self):
		"""Returns the blackjack value of the card. 
		Example:
		-------
		2 == 2; King == 10
		Note: An ace is given the default value of 1 here.  Its alternative
		value of 11 is assigned in blackjack.py.
		"""
		if self.rank == 'Ace':
			return 1 
		elif self.rank == 'Jack' or self.rank == 'Queen' or self.rank == 'King':
			return 10
		else:
			return int(self.rank)

	def __str__(self):
		return('{0} of {1}'.format(self.rank, self.suit))

class Deck(object):
	"""A class for generating a deck of cards.
	"""
	def __init__(self):
		"""Initializes the deck, which is an empty list.
		"""
		self.game_deck = []
	
	def constructor(self):
		"""Constructs a deck of 52 cards. This function will create a deck
		using the traditional French suits with the suit order Clubs, Diamonds,
		Hearts, and Spades.
		"""
		for num in ['Ace','2', '3', '4', '5', '6', '7', '8', '9', '10',
						'Jack', 'Queen', 'King']:
			for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
				self.game_deck.append(Card(num, suit))
		self.game_deck = enumerate(self.game_deck)
		return self.game_deck

if __name__ == '__main__':
	pass


