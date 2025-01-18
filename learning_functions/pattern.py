"""
create a saquare of 'n'
create a hollow square of side 'n'
create of rectangle of side 'n'
create a hollow rectangle of side 'n'
create a pyramid of row 'n'
can you fuse 1,2,3,4

"""

# def pattern_square(size):
#     for i in range(size):
#         row = '*' * size
#         print(row)
#
# pattern_square(4)


def pattern_hollow_square(size):
    for i in range(size):
        if i == 0 or i ==  4:
            row = '*' * size
        else:
            row = '*' + " " * 3 + '*'

        print(row)

pattern_hollow_square(5)





