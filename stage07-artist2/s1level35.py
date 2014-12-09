"""Stage 7: Puzzle 1 of 11

Can you draw a triangle (with edges of 100 pixels) with only 3
lines of code? Hint: use a repeat (for) loop.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level35')
a = artist

a.move_forward(100)
a.turn_right(120)
a.move_forward(100)
a.turn_right(120)
a.move_forward(100)

artist.check()
