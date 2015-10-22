# A command line blackjack game. 
# Written for PDX Code Guild 2015.
__author__ = "Kevin Saavedra"

import card_objects as c_o
import sys

def hit_me(Player, new_deck):
	"""Adds one card to the hand. The input Player can refer to both the user
	and the dealer.
	"""
	card = new_deck.drawCard()
	Player.hand.addCard(card)
	for item in Player.hand.current_hand:
		index, card_object = item
		print(Player.name, "Card", "is", card_object)
	print("Total hand value is", Player.hand.handValue())
	print("\n")
	if Player.hand.handValue() > 21:
		print("\nBUST! Game Over! :(\n\n\n")
		main()
	else:
		turn(None, Player, new_deck)

def stand(dealer, player, new_deck): 
	"""Completes the game..
	"""
	pass

def turn(dealer, player_, new_deck):
	"""The core turn logic. 
	"""
	decide_input = input("Would you like to hit or stand?\n" \
					   "type 'h' to hit or 's' to stand.\n>> ")
	if decide_input == "h":
		hit_me(player_, new_deck)
	elif decide_input == "s":
		if player_.hand.handValue() > dealer.hand.handValue() and (
			dealer.hand.handValue() < 22):
			print("\n\nYou win!\n\n\n") 
		elif player_.hand.handValue() < dealer.hand.handValue():
			print("You lose!")
	main()
		
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
			print(item.name, "Card", "is", 
					item.current_hand[i][1].__str__())
		print("Total hand value is", item.handValue())
		print("\n")
	turn(dealer, player_, new_deck)

def main():
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
	
if __name__ == "__main__":
	main()