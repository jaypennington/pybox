# A city skyline can be represented as a 2-D list with 1s representing buildings.
# In the example below, the height of the tallest building is 4 (second-most right column).
#   [[0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 1, 0],
#    [0, 0, 1, 0, 1, 0],
#    [0, 1, 1, 1, 1, 0],
#    [1, 1, 1, 1, 1, 1]]
# Create a function that takes a skyline (2-D list of 0's and 1's)
# and returns the height of the tallest skyscraper.


def tallest_skyscraper(skyline):
    sky_height = len(skyline)

    for i in range(sky_height):
        for item in skyline[i]:
            if item == 1:
                return sky_height - i