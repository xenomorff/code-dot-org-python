"""Stage 5: Puzzle 3 of 10

Make a square using only 3 lines of code. Hint: replace 'pass', (which does
nothing but lets the code still run), with your code

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level26')
a = artist

for count in range(4):
 a.move_forward(100)
 a.turn_right(90) # ???

artist.check()
