import time
import random
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas

class Matrix:
	def __init__(self): 
		# Define the SPI interface
		self.serial = spi(port=0, device=0, gpio=noop())

		# Initialize the MAX7219 device
		self.device = max7219(self.serial, cascaded=1, block_orientation=0, rotate=0)

		# Clear the display
		self.device.clear()

		self.matrix = [
			["X","X","X","X","X","X","X","X"],
			["X","X","X","X","X","X","X","X"],
			["","","","","","","",""],
			["","","","","","","",""],
			["","","","X","","","",""],
			["","","","","","","",""],
			["X","X","X","","X","X","X","X"],
			["X","X","X","X","X","X","X","X"],
		]; 

	def __str__(self):
		return f"{self.matrix}"

	def printmatrix(self):
		self.rst()
		with canvas(self.device) as draw:
			for row_idx,row in enumerate(self.matrix):
				for col_idx,col in enumerate(row):
					if col == "X":
						self.printpoint(col_idx,row_idx,draw);

	def rst(self):
		self.device.clear(); 

	def scatter(self): 
		for r in range(0,7):
			for c in range (0,7):
				ridx = random.randint(1,2);
				if ridx == 1:
					self.matrix[r][c]="X";
				else:
					self.matrix[r][c]=""

			

	def printpoint(self,x,y,draw):
		try:
			draw.point((x, y), fill="white")
		except:
			print("FATAL!"); 
			self.rst(); 

if __name__=="__main__":
	grid = Matrix()
	try:
		while True:
			grid.scatter();
			grid.printmatrix();
			time.sleep(0.1); 
	finally: 
		grid.rst();