# A command line blackjack game. 
# Written for PDX Code Guild 2015.
__author__ = "Kevin Saavedra"

import card_objects as c_o
import sys

def hit_me(dealer, player_, new_deck):
	"""Adds one card to the player's hand. A bust condition will end the game in
	a loss for the player. 

	Input:
	------
	dealer, player_, new_deck objects.

	Output:
	-------
	A bust condition will end the game with a loss. 
	Otherwise, dealer, player_, and new_deck objects are passed to the turn()
	function for futher play.

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

def stand_evaluator(dealer, player_, new_deck):
	"""If the player does not bust, this function evaluates the value of his or
	her hand compared with the dealer's hand. Note that the dealer bust condition 
	was evaluated in turn() function prior to this step.  
	"""
	"""Player wins outright"""
	if player_.hand.handValue() > dealer.hand.handValue() and (
		dealer.hand.handValue() < 22): #player will never have a handValue >21.
	                                   #see hit_me() above for automatic 
	                                   #lose condition in case of this event.
		print("\n\nYou win!\n\n\n") 
	"""Dealer busts"""
	if player_.hand.handValue() < dealer.hand.handValue() and (
		dealer.hand.handValue() > 21):
		print("\n\nYou win!\n\n\n")
	"""Player loses outright"""
	if player_.hand.handValue() < dealer.hand.handValue() and (
		dealer.hand.handValue() < 22):
		print("\n\nYou lose!\n\n\n")
	"""Draw situation"""
	if player_.hand.handValue() == dealer.hand.handValue():
		print("\n\nIt's a draw!\n\n\n")
	main()

def turn(dealer, player_, new_deck):
	"""The core turn logic. Player is asked whether or not to hit or stand. 
	Meanwhile, the dealer evaluates whether or not to draw or stand.  Per common
	casino rules, the dealer will hit if hand value is <= 16 and will stand if 
	the value is > 16 and < 22.
	
	Input:
	------
	dealer, player_, deck objects.
	
	User Input:
	------------
	'h' to hit or 's' to stand.

	Output:
	-------
	If player decides to hit, dealer, player_, and deck obects are passed to the
	hit_me function.

	If player decides to stand, dealer, player_, and deck objects are passed to 
	the stand_evaluator function for scoring. 
	"""
	
	"""Player input prompt"""
	decide_input = input("Would you like to hit or stand?\n" \
				   "type 'h' to hit or 's' to stand.\n>> ")
	"""Dealer's turn"""
	print("\nDealer's Turn!\n") #for program and game flow, the dealer's turn  
	                            #and string outputs are placed here so the user's
	                            #input does not end the function call. 
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
		stand_evaluator(dealer, player_, new_deck)		

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
	
	User Input: 
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