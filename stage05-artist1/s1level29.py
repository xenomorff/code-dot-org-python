"""Stage 5: Puzzle 6 of 10

Can you figure out how draw this triangle and square? Hint: Do the
triangle first, then figure out how much to turn before drawing the
square.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level29')
a = artist

for count in range(1):
    a.move_forward()        # ???
    a.turn_right(120)
    a.move_forward()
    a.turn_right(120)
    a.move_forward()
    a.turn_left(60)
    a.move_forward()
    a.turn_right()
    a.move_forward()
    a.turn_right()
    a.move_forward()
    a.turn_right()
    a.move_forward()

artist.check()
