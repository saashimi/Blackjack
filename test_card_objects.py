import unittest
from card_objects import *


class TestCardObjects(unittest.TestCase):
    __owner__ = 'Kevin Saavedra'

    @classmethod
    def setUpClass(cls):
        cls.test_card = Card("Ace", "Spades")
        cls.test_deck = Deck()
        cls.shuffled_deck = cls.test_deck.shuffleDeck()
        cls.drawn_card = cls.test_deck.drawCard()
        cls.test_hand = Hand('test')
        cls.test_hand.addCard(cls.drawn_card)
        cls.test_player = Player('Player1', cls.test_hand)

    def test_card_rank(self):
        """Make sure rank is correct."""
        self.assertEqual(self.test_card.rank, 'Ace')

    def test_card_suit(self):
        """Make sure suit is correct."""
        self.assertEqual(self.test_card.suit, 'Spades')

    def test_card_value(self):
        """Make sure card value is correct."""
        self.assertEqual(self.test_card.BJValue(), 1)

    def test_string_value(self):
        """Make sure string value is correct."""
        self.assertEqual(self.test_card.__str__(), 'Ace of Spades')

    def test_deck_size(self):
        """Make sure deck size is correct."""
        self.assertEqual(len(self.test_deck.game_deck), 52) # The number of cards in a deck.

    def test_shuffle(self):
        """Make sure shuffled deck differs from standard ordered deck."""
        self.assertNotEqual(sorted(self.test_deck.game_deck),
                            self.test_deck.game_deck)

    def test_draw_card(self):
        """Make sure that drawn card is a tuple."""
        self.assertEqual(len(self.drawn_card), 2) # A single card object is a tuple.

    def test_cards_left(self):
        """Make sure a drawn card subtracts one from the deck."""
        self.assertEqual(self.test_deck.cardsLeft(), 51)
        # Expect one less card every time one is drawn.

    def test_hand_object(self):
        """Make sure hand value is as expected."""
        self.assertEqual(self.test_hand.handValue(), 11)
        self.assertEqual(self.test_hand.current_hand[0][1].__str__(), 'Ace of Clubs')
        #return test_hand #Pass this onto player_object_test to make sure the Player
        #object inherits its characteristics

    def player_object_tests(self):
        """Test value in player hand."""
        test_player = Player("Player1", hand)
        self.assertEqual(test_player.hand.current_hand[0][1].__str__(), 'Ace of Clubs')

"""
def mergeSort_test():
    
    test_deck = Deck()
    test_deck1 = Deck()
    test_deck.shuffleDeck()
    assert sorted(test_deck.game_deck) != test_deck.game_deck #Check that it's
    #been shuffled.
    merge_sorted_deck = test_deck.mergeSort()
    assert merge_sorted_deck == sorted(merge_sorted_deck)	 #Check that it's been
    # sorted.
    print("Passed mergeSort_test!")
"""

if __name__ == "__main__":
    unittest.main(verbosity=2)