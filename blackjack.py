# A command line blackjack game. 
# Written for PDX Code Guild 2015.
__author__ = "Kevin Saavedra"

import card_objects as c_o
import sys

def hit_me(dealer, player_, new_deck):
	"""Adds one card to the hand.
	"""
	card = new_deck.drawCard()
	player_.hand.addCard(card)
	for item in player_.hand.current_hand:
		index, card_object = item
		print(player_.name, "Card", "is", card_object)
	print("Total hand value is", player_.hand.handValue())
	print("\n")
	if player_.hand.handValue() > 21:
		print("\nBUST! Game Over! :(\n\n\n") 
		main()
	else:
		turn(dealer, player_, new_deck)

def turn(dealer, player_, new_deck):
	"""The core turn logic. 
	"""
	"""Player input prompt"""
	decide_input = input("Would you like to hit or stand?\n" \
				   "type 'h' to hit or 's' to stand.\n>> ")
	"""Dealer's turn"""
	print("\nDealer's Turn!\n")
	if dealer.hand.handValue() <= 16:
		card = new_deck.drawCard()
		dealer.hand.addCard(card)
		print("\nDealer draws a card!")
	else:
		print("Dealer stands!")
	for item in dealer.hand.current_hand:
		index, card_object = item
		print(dealer.name, "Card", "is", card_object)
	print("Total hand value is", dealer.hand.handValue(), "\n")
	if dealer.hand.handValue() > 21:
		print("\nDealer BUSTS!\n")
	"""Player decision script"""
	if decide_input == "h":
		hit_me(dealer, player_, new_deck)
	elif decide_input == "s":
		if player_.hand.handValue() > dealer.hand.handValue() and (
			dealer.hand.handValue() < 22):
			print("\n\nYou win!\n\n\n") 
		if player_.hand.handValue() < dealer.hand.handValue() and (
			dealer.hand.handValue() > 22):
			print("\n\nYou win!\n\n\n") # dealer busts
		elif player_.hand.handValue() < dealer.hand.handValue() and (
			dealer.hand.handValue() < 22):
			print("\n\nYou lose!\n\n\n")
		elif player_.hand.handValue() == dealer.hand.handValue():
			print("\n\nIt's a draw!\n\n\n")
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