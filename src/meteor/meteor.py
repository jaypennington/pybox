# In a video game, a meteor will fall toward the main character's home planet.
# Given the meteor's trajectory as a string in the form y = mx + b and the
# character's position as a tuple of (x, y), return True if the meteor will
# hit the character and False if it will not.


def will_hit(traject, coords):
    traj_data = traject.split(" ")

    m = int(traj_data[2][:-1])
    b = int(traj_data[4])
    
    strike = m*coords[0] + b

    if strike == coords[1]:
        return True
    else:
        return False