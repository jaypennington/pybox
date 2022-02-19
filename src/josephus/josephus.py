# A group of n prisoners stand in a circle awaiting execution.
# Starting from an arbitrary position(0), the executioner kills
# every kth person until one person remains standing, who is
# then granted freedom (see examples).

# Create a function that takes 2 arguments — the number of
# people to be executed n, and the step size k, and returns
# the original position (index) of the person who survives.

def who_goes_free(num_prisoners, iteration):
    # build the list
    prisoner_list = list(range(num_prisoners))

    start = iteration-1
    while prisoner_list.count("-") != len(prisoner_list) - 1:
        for i in range(start, len(prisoner_list), iteration):
            prisoner_list[i] = "-"
        start = start - len(prisoner_list)%iteration
        prisoner_list = list_remove(prisoner_list, "-")

    for i in prisoner_list:
        if i != "-":
            return i

def list_remove(a_list, item):
    for i in a_list:
        if i == item:
            a_list.remove(i)
    return a_list

def main():
    who_goes_free(9,2)

if __name__ == "__main__":
    main()