import math as m

sequence: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

other_sequence: list[int] = []

def calc_squares (n: int):
    return int(m.pow(n, 2))


def write_squares_in_new_list (s: list[int]):
    for i in s:
        if (i != 0):
            other_sequence.append(calc_squares(i))
        else:
            break
    return other_sequence

def print_squares (s: list[int]):
    new_s = write_squares_in_new_list(s)
    for i in new_s:
        print(i)

print_squares(sequence)