"""Stage 5: Puzzle 8 of 10

Ok, try to figure out what happens when you run this code.
Then, repeat it enough times to complete the drawing. The
colors will be different every time.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level31')
a = artist

artist.color = artist.random_color()
artist.move_forward(100)
artist.move_backward(100)
artist.turn_right(45)
artist.color = artist.random_color()
artist.move_forward(100)
artist.move_backward(100)
artist.turn_right(45)
artist.color = artist.random_color()
artist.move_forward(100)
artist.move_backward(100)
artist.turn_right(45)
artist.color = artist.random_color()
artist.move_forward(100)
artist.move_backward(100)
artist.turn_right(45)
artist.color = artist.random_color()
artist.move_forward(100)
artist.move_backward(100)
artist.turn_right(45)
artist.color = artist.random_color()
artist.move_forward(100)
artist.move_backward(100)
artist.turn_right(45)
artist.color = artist.random_color()
artist.move_forward(100)
artist.move_backward(100)
artist.turn_right(45)
artist.color = artist.random_color()
artist.move_forward(100)
artist.move_backward(100)
artist.turn_right(45)

artist.check()
