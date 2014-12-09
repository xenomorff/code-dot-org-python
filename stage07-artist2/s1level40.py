"""Stage 7: Puzzle 6 of 11

Using only 3 lines of code, can you draw a square with edges of 20 pixels?

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level40')
a = artist
for count in range(4):
    a.move_forward(20)
    a.turn_right(90)

artist.check()
