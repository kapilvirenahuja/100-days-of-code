import math

def paint_calc(height, width, coverage):
    area = height * width
    num_of_cans = area / coverage

    # return num_of_cans and round to the top
    return math.ceil(num_of_cans)


height = int(input ("Enter the height of the wall: "))
width = int(input ("Enter the width of the wall: "))

coverage = 5
number_of_cans = paint_calc(height=height, width=width, coverage=coverage)
print (f"number of cans needed: {number_of_cans}")
