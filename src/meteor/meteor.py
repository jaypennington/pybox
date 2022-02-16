def will_hit(traject, coords):
    traj_data = traject.split(" ")

    m = int(traj_data[2][:-1])
    b = int(traj_data[4])
    
    strike = m*coords[0] + b

    if strike == coords[1]:
        return True
    else:
        return False