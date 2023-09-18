import unittest
import sys
sys.path.append("../")
from chess.board import Board
from stockfish import Stockfish

class TestBoard(unittest.TestCase):
    def test_move(self):
        # tests the moving functionality of the board.
        brd = Board(); 
        brd.move("e2e4");
        
        expected_fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"
        
        self.assertEqual(brd.fen, expected_fen);
    
    def test_legal_move_false(self):
        brd = Board();
        legality = brd.move("e2e5");
        self.assertFalse(legality); 
        
    def test_legal_move_true(self):
        brd = Board(); 
        legality = brd.move("e2e4");
        self.assertTrue(legality);
        
    def test_fen_to_matrix(self):
        brd = Board(); 
        # fen = rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1
        matrix = brd.fen_to_matrix(); 
        
        expected_matrix = [
			["X","X","X","X","X","X","X","X"],
			["X","X","X","X","X","X","X","X"],
			["","","","","","","",""],
			["","","","","","","",""],
			["","","","","","","",""],
			["","","","","","","",""],
			["X","X","X","X","X","X","X","X"],
			["X","X","X","X","X","X","X","X"],
		]; 
        
        self.assertEqual(matrix,expected_matrix); 
