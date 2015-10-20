from card_objects import *

def constructor_test():
	"""Test Deck object.
	"""
	test_deck = Deck() 
	test_card = Card("Ace", "Clubs")
	alpha = test_deck.constructor()
	bravo = alpha[0][1]
	#assert alpha == test_card
	#for item in temp:
	#	index, value = item
	#print(index, value)
	#	tuple_ = (index, value)
	##assert temp[0] == (0, "Ace of Clubs") # KS: how to check?
	#assert temp[51] == (51, "King of Spades") # ks how to check?
	#assert print(index, value) == "51 King of Spades"
	#print(temp[0][1])
	#print(type(alpha))
	assert len(alpha) == 52
	print("Passed constructor() test!")
	
	"""
	Test draw_card
	"""
	bravo = test_deck.draw_card()
	index, value = bravo
	print(index, value)
	#assert print(index, value) == ("0 Ace of Clubs")




if __name__ == "__main__":
	constructor_test()