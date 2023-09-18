from stockfish import Stockfish

import sys
sys.path.append("../")
from io_utilities.matrix import Matrix

class Board:
    def __init__(self, grid=Matrix()): 
        self.grid = grid
        self.stockfish = Stockfish(path="/opt/homebrew/bin/stockfish");
        #initialize board.
        self.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w QKqk - 0 1"
        self.stockfish.set_fen_position(self.fen); 

    def move(self, mv) -> bool:
        try:
            self.stockfish.make_moves_from_current_position([mv]);
            self.fen = self.stockfish.get_fen_position();
            
            self.grid.matrix=self.fen_to_matrix();
            self.grid.printmatrix(); 
            
        except ValueError:
            return False
        else:
            return True
        
    def fen_to_matrix(self):
        # Create an empty 8x8 chessboard
        board = [['' for _ in range(8)] for _ in range(8)]

        # Split the FEN string into its components
        fen_parts = self.fen.split(' ')
        piece_placement = fen_parts[0]  # Piece placement part of the FEN

        # Initialize variables for tracking the current board position
        rank = 7  # Start from the 8th rank (0-based indexing)
        file = 0   # Start from the a-file (0-based indexing)

        # Iterate through the FEN characters to populate the board
        for char in piece_placement:
            if char == '/':
                rank -= 1  # Move to the next rank
                file = 0   # Reset the file counter
            elif char.isnumeric():
                file += int(char)  # Skip empty squares
            else:
                board[rank][file] = "X"  # Place the piece on the board
                file += 1  # Move to the next file

        return board

if __name__== "__main__":
    brd = Board()
    brd.move("e2e4")
    print(brd.stockfish.get_board_visual(True));