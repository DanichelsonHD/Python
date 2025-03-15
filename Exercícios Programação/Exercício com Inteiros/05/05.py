import math as m

sells: list[int] = [ 1, 5, 2, 7, 9, 3, 8, 4, 6 ]

def find_major_sell (s: list[int]):
    major: int = 0
    for i in sells:
        if i > major:
            major = i
    return major

print(find_major_sell(sells))