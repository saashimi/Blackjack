from card_objects import *

def card_object_tests():
	"""Test card objects.
	"""
	test_card = Card("Ace", "Spades")
	assert test_card.rank == "Ace"
	assert test_card.suit == "Spades"
	assert test_card.BJValue() == 1
	assert test_card.__str__() == "Ace of Spades"
	print("Passed card object tests!")

def deck_object_tests():
	"""Test Deck object.
	"""
	test_deck = Deck() 
	assert len(test_deck.game_deck) == 52 #The number of cards in a deck.
	print("Passed __init__ test!")
	
	""" Test shuffle_deck method.
	"""
	test_deck.shuffleDeck()
	assert sorted(test_deck.game_deck) != test_deck.game_deck
	print("Passed shuffle_deck test!")

	"""Test draw_card method.
	"""
	returned = test_deck.drawCard()
	#print(returned)
	assert(len(returned)) == 2 #A single card object is a tuple.  
	print("Passed draw_card test!")

	"""Test cards_left method.
	"""
	assert test_deck.cardsLeft() == 51 #Expect one less card every time one is
									   #drawn.
	print("Passed cards_left test!")

def hand_object_tests():
	"""Test Hand objects.
	"""
	test_deck = Deck()
	returned = test_deck.drawCard()
	test_hand = Hand()
	test_hand.addCard(returned)
	assert(test_hand.current_hand[0][1].__str__()) == "Ace of Clubs"
	Print("Passed hand object tests!")

if __name__ == "__main__":
	card_object_tests()
	deck_object_tests()
	hand_object_tests()