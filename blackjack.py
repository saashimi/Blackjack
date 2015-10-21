# A command line blackjack game. 
# Written for PDX Code Guild 2015.

import card_objects as c_o
import sys

def hit_me():
	"""Adds one card to the hand"""
	pass

def stand():
	"""Initiates the next turn."""
	pass

def deal():
	"""Deals the two cards into the hand at the start of the game.
	"""
	pass
	
def init_game():
	"""Initializes a dealer, player, and game deck"""
	dealer = c_o.Player("Dealer")
	player_ = c_o.Player("Player")
	new_deck = c_o.Deck() 

def main():
	"""Main function"""
	print("\nWelcome to Blackjack!\n")
	start_text = input("Type 'start' to play or 'quit' to quit.")
	if start_text == 'start':
		init_game()
	elif start_text == 'quit':
		sys.exit(0)
	else:
		print("Not a valid command, bozo. We're outta here.")
		sys.exit(0)




if __name__ == "__main__":
	main()