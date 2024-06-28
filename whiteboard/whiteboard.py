# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of 
# pair of gloves you can constitute from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can constitute, 
# assuming that only gloves of the same color can form pairs.

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)

# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)

def solution(s):
    color_count = {}
    for color in (s):
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    pairs = 0
    for color in color_count:
            pairs += color_count[color] //2
    return pairs