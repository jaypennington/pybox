def tallest_skyscraper(skyline):
    sky_height = len(skyline)

    for i in range(sky_height):
        for item in skyline[i]:
            if item == 1:
                return sky_height - i