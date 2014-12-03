"""Stage 5: Puzzle 5 of 10

Now, for practice, draw a triangle and then a square to draw an envelope.
Hint: delete the 'pass' (which does nothing) with your code.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level28')
a = artist

for count in range(1):
    a.turn_right(60)                                        # ???
    a.move_forward(100)
    a.turn_left(60)
    a.turn_left(60)
    a.move_forward(100)
    a.turn_left(120)
    a.move_forward()
    a.turn_left()
    a.move_forward()
    a.turn_left()
    a.move_forward()
    a.turn_left()
    a.move_forward()
    
    


artist.check()
