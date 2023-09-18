from chess.board import Board
from chess.bot import Bot
from io_utilities.matrix import Matrix
import os
import time

white = Bot(1000)
black = Bot(800)

m = Matrix.new

b = Board(grid=m); 

while True:
     
     wmove = white.get_best_move(b.fen)
     b.move(wmove); 
     
     os.system('cls' if os.name == 'nt' else 'clear')
     
     print(b.stockfish.get_board_visual(True))
     
     time.sleep(2);
     
     bmove = black.get_best_move(b.fen)
     b.move(bmove)
     
     os.system('cls' if os.name == 'nt' else 'clear')
     
     print(b.stockfish.get_board_visual(True))
     
     time.sleep(2);