from stockfish import Stockfish

class Bot:
    def __init__(self, elo) -> None:
        self.stockfish = Stockfish(path="/opt/homebrew/bin/stockfish");
        #initialize board.
        self.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w QKqk - 0 1"
        self.stockfish.set_fen_position(self.fen); 
        
        self.stockfish.set_elo_rating(1350)
    
    def get_best_move(self, fen, time=1000) -> str:
        self.stockfish.set_fen_position(fen); 
        return self.stockfish.get_best_move_time();
