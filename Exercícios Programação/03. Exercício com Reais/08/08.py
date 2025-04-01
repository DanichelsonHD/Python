class Student:
    def __init__ (self, grades: list[int]):
        self.grades = grades
        self.approved: bool = False

students: list[Student] = [
    Student([8, 7, 9]),
    Student([5, 3, 1]),
    Student([3, 5, 7]),
    Student([6, 1, 7]),
    Student([5, 7, 6]),
    Student([4, 8, 10])
]

def average_of_grades (student: object) -> int:
    average: int = 0
    
    for grade in student.grades:
        average += grade
    
    average /= 3
    
    return average

def verify_students (students: list[Student]):
    aproved: list[Student] = []
    failed: list[Student] = []
    average: float = 0.0
    
    for i in students:
        if average_of_grades(i) >= 5:
            i.approved = True
            aproved.append(i)
        else:
            failed.append(i)
        average += average_of_grades(i)
    
    average /= len(students)
    
    print(f'Aprovados: {len(aproved)}\nReprovados: {len(failed)}\nMédia da turma: {average:.2f}')

verify_students(students)            