import unittest
from unittest.mock import patch
from io import StringIO
from blackjack import BlackjackGame

class BlackjackGameTests(unittest.TestCase):
    def setUp(self):
        self.game = BlackjackGame()

    def tearDown(self):
        pass

    @patch('builtins.input', side_effect=['John', '100'])
    def test_setup_game(self, mock_input):
        self.game.setup_game()
        self.assertEqual(self.game.player.name, 'John')
        self.assertEqual(self.game.player.money, 100)

    @patch('builtins.input', return_value='50')
    def test_get_bet_valid(self, mock_input):
        bet = self.game.get_bet()
        self.assertEqual(bet, 50)

    @patch('builtins.input', side_effect=['5', '15'])
    def test_get_bet_below_minimum(self, mock_input):
        bet = self.game.get_bet()
        self.assertEqual(bet, 15)

    @patch('builtins.input', return_value='200')
    def test_get_bet_exceeds_money(self, mock_input):
        self.game.player.money = 150
        bet = self.game.get_bet()
        self.assertEqual(bet, 150)

    @patch('builtins.input', return_value='invalid')
    def test_get_bet_invalid_input(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            bet = self.game.get_bet()
            self.assertEqual(fake_output.getvalue().strip(), 'Invalid bet. Please enter a valid amount.')

    def test_evaluate_round_player_busted(self):
        self.game.player.hand = MockHand([10, 10, 5])
        self.game.dealer.hand = MockHand([10, 5])
        self.game.evaluate_round(50)
        self.assertEqual(self.game.player.money, 50)

    def test_evaluate_round_dealer_busted(self):
        self.game.player.hand = MockHand([10, 5])
        self.game.dealer.hand = MockHand([10, 10, 5])
        self.game.evaluate_round(50)
        self.assertEqual(self.game.player.money, 150)

    def test_evaluate_round_tie(self):
        self.game.player.hand = MockHand([10, 5])
        self.game.dealer.hand = MockHand([10, 5])
        self.game.evaluate_round(50)
        self.assertEqual(self.game.player.money, 100)

    def test_evaluate_round_player_wins(self):
        self.game.player.hand = MockHand([10, 8])
        self.game.dealer.hand = MockHand([10, 5])
        self.game.evaluate_round(50)
        self.assertEqual(self.game.player.money, 150)

    def test_evaluate_round_dealer_wins(self):
        self.game.player.hand = MockHand([10, 5])
        self.game.dealer.hand = MockHand([10, 8])
        self.game.evaluate_round(50)
        self.assertEqual(self.game.player.money, 50)

class MockHand:
    def __init__(self, values):
        self.values = values

    def get_value(self):
        return sum(self.values)

if __name__ == '__main__':
    unittest.main()
