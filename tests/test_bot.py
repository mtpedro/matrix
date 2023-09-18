import unittest
import sys
sys.path.append("../")
from chess.bot import Bot
from stockfish import Stockfish

class TestBoard(unittest.TestCase):
    def test_get_best_move(self):
        b = Bot(3000); 
        
        # reverse arrow head opening (instant checkmate)
        mv = b.get_best_move("rnbqkbnr/pppp1ppp/8/4p3/6P1/5P2/PPPPP2P/RNBQKBNR b KQkq g3 0 2", time=10); 
        
        self.assertEqual(mv, "d8h4"); 
        
        # scholars mate (instant checkmate)
        mv = b.get_best_move("r1bqkbnr/pppp1p1p/2n3p1/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 0 4", time=10);
        
        self.assertEqual(mv, "f3f7"); 