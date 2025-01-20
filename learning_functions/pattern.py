# 1. Create a square of side 'n'.
# Example.
# n = 4
# ****
# ****
# ****
# ****
def pattern_unified(shape="square", length=4, breadth=None, hollow=False):
    if shape == "square":
        breadth = length  # If it's a square, breadth is the same as length
    for i in range(breadth):
        if hollow and i != 0 and i != breadth - 1:
            row = '*' + " " * (length - 2) + '*'
        else:
            row = '*' * length
        print(row)

pattern_unified(shape="square", length=4)

# 2. Create a hollow Square of side 'n'.
# Example.
# n = 4
# ****
# *  *
# *  *
# ****
pattern_unified(shape="square", length=5, hollow=True)


# 3. Create a rectangle of side 'n'.
# Example.
# l = 4, b = 3
# ****
# ****
# ****
def pattern_rectangle(length,breadth):
    for i in range(breadth):
        row = '*' * length
        print(row)

pattern_rectangle(4,3)


# 4. Create a Hollow Rectangle of side 'n'.
# Example.
# l=4, b=3
# ****
# *  *
# ****
def pattern_hollow_rectangle(l, b):
    for i in range(b):
        if i == 0 or i == b - 1:
            row = '*' * l
            print(row)
        else:
            row = '*' + " " * (l - 2) + '*'
            print(row)
pattern_hollow_rectangle(4,3)


# 5. Create a pyramid of row 'n'.
# Example.
# row = 3
#   *
#  ***
# *****
def pyramid(row):
    def progression():
         return 1 + (row - 1) * 2

    asterics = 1
    highest_count = progression()
    for i in range(row):
        spaces = (highest_count - asterics) // 2
        print (' ' * spaces + '*' * asterics)
        asterics = asterics + 2

pyramid(5)




