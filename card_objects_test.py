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
	test_hand = Hand("test")
	test_hand.addCard(returned)
	assert test_hand.handValue() == 11 
	assert(test_hand.current_hand[0][1].__str__()) == "Ace of Clubs"
	print("Passed hand object tests!")
	return test_hand #Pass this onto player_object_test to make sure the Player
					 #object inherits its characteristics

def mergeSort_test():
	"""Tests the mergeSort function."""
	test_deck = Deck()
	test_deck1 = Deck()
	test_deck.shuffleDeck()
	assert sorted(test_deck.game_deck) != test_deck.game_deck #Check that it's 
															  #been shuffled.
	merge_sorted_deck = test_deck.mergeSort()
	assert merge_sorted_deck == sorted(merge_sorted_deck)	 #Check that it's been
	                                                   # sorted.
	print("Passed mergeSort_test!") 

def player_object_tests(hand):
	"""Test Player objects.
	"""
	test_player = Player("Player1", hand)
	assert(test_player.hand.current_hand[0][1].__str__()) == "Ace of Clubs"
	print("Passed player object tests!")
	print("!!!!!!!!!! All tests passed !!!!!!!!!!")

if __name__ == "__main__":
	card_object_tests()
	deck_object_tests()
	output = hand_object_tests()
	mergeSort_test()
	player_object_tests(output)
