import math as m

grades: list[int] = [52, 67, 100, 89, 75, 65, 92, 81, 76, 56]

def find_major_and_minor_grades (g: list[int]):
    major: int = 0
    minor: int = 100
    for i in grades:
        if i > major:
            major = i
        if i < minor:
            minor = i
    return 'Maior nota é: ' + str(major), 'Menor nota é: ' + str(minor)

print(find_major_and_minor_grades(grades))