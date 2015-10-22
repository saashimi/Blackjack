# A command line blackjack game. 
# Written for PDX Code Guild 2015.
__author__ = "Kevin Saavedra"

import card_objects as c_o
import sys

def hit_me(dealer_input, player_input):
	"""Adds one card to the hand
	"""
	print("That happened painlessly!")

#def stand(): # Don't know if we actually need a stand function.
#	"""Initiates the next turn.
#	"""
#	pass

def turn(dealer_input, player_input):
	"""The core turn logic. 
	"""
	print("That happened painlessly!")
		
def init_game():
	"""Initializes a dealer, player, and shuffled game deck.
	Output:
	-------
	dealer_hand, player_hand, and new_deck, which are passed to the deal 
	function.
	"""
	dealer_hand = c_o.Hand("Dealer") #TODO: write a for loop to simplify this.
	player_hand = c_o.Hand("Player") # These are all initialization steps.
	dealer = c_o.Player("Dealer", dealer_hand)
	player_ = c_o.Player("Player", player_hand)
	new_deck = c_o.Deck() 
	new_deck.shuffleDeck()
	for item in [dealer_hand, player_hand]: 
		for i in range(2):
			card = new_deck.drawCard()
			item.addCard(card)
			print(item.name, "Card", i + 1, "is", 
					item.current_hand[i][1].__str__())
		print("Total hand value is", item.handValue())
		print("\n")
	decide_input = input("Would you like to hit or stand?\n" \
					   "type 'h' to hit or 's' to stand.\n>> ")
	if decide_input == "h":
		hit_me(dealer, player_)
	elif decide_input == "s":
		turn(dealer_, player)

def init_script():
	"""Allows the player to start or exit the game.
	Input: 
	------
	'start' or 'quit' via user prompt.
	Output:
	-------
	If 'start', initiates game.
	"""
	print("\nWelcome to Blackjack!\n")
	start_text = input("Type 'start' to play or 'quit' to quit.\n>> ")
	if start_text == 'start':
		init_game()
	elif start_text == 'quit':
		sys.exit(0)
	else:
		print("Not a valid command, bozo. We're outta here.")
		sys.exit(0)	

def main():
	"""Main function"""
	init_script()

	
if __name__ == "__main__":
	main()