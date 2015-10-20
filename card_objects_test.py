from card_objects import *

def master_test():
	"""Tests all classes"""
	"""Test constructor"""
	test_lst = []
	new = Deck() 
	temp = new.constructor()
	for items in temp:
		index, value = items
		test_lst.append((index, value)
	assert temp[0] == (0, "Ace of Clubs")
	assert temp[51] == (51, "King of Spades")
	print("Passed constructor() test!")

if __name__ == "__main__":
	master_test()