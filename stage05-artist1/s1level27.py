"""Stage 5: Puzzle 4 of 10

Draw a triangle whose sides are all in different colors. Hint:
you'll have to figure out how far to turn by testing different
values for the `turn_right(degrees)` function. Note: we've added
`artist.random_color()` as well. Use it instead of a color to get
random colors. (`artist.random_colour()`,`artist.colour_random()`, and
`artist.color_random()` will also work.)

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level27')
a = artist

for count in range(3):
    artist.color = artist.random_color()
    a.move_forward(100)
    a.turn_right(120)
    # ???
    
artist.check()
