"""Stage 15: Puzzle 4 of 10

See if you can figure out how to use `draw_square()` and `draw_triangle()`
(and some other code) to draw a house around the lion.

"""
import sys
sys.path.append('..')
import codestudio
z = codestudio.load('s1level85')

def draw_square():
    for count in range(4):
        z.move_forward(100)
        z.turn_right(90)

def draw_triangle():
    for count in range(3):
        z.move_forward(100)
        z.turn_right(120)

draw_square()
z.move_forward()
z.turn_right()
z.move_forward()
z.turn_left()
z.turn_left()
draw_triangle()


z.check()
