# Excercise: https://www.hackinscience.org/exercises/student-class
#
#
# Solution:

class Student:
    def __init__(self, name: str | None = None) -> None:
        self.name = name
        self.grade: list[float] = []

    def __str__(self) -> str:
        return f"[{self.name}, {self.grade}]"

    def add_exam(self, grade) -> None:
        self.grade.append(float(grade))

    def get_mean(self) -> float:
        return sum(self.grade) / len(self.grade)



class School:
    def __init__(self, name: str | None = None) -> None:
        self.name = name
        self.students: list[Student] = []

    def __str__(self) -> str:
        return f"[{self.name}, total {len(self.students)} students]"

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def get_mean(self) -> float:
        total = 0
        for student in self.students:
            total += student.get_mean()
        return total / len(self.students)
    
    def get_best_student(self) -> Student:
        best = {"student" : None, "mean": 0}
        for i in self.students:
            if i.get_mean() > best["mean"]:
                best["student"], best["mean"] = i, i.get_mean()
        return best["student"]


class City:
    def __init__(self, name: str | None = None) -> None:
        self.name = name
        self.schools: list[School] = []

    def add_school(self, school: School) -> None:
        self.schools.append(school)

    def get_mean(self) -> float:
        total = 0
        for school in self.schools:
            total += school.get_mean()
        return total / len(self.schools)
    
    def get_best_school(self) -> School:
        best = {"school": None, "mean": 0}
        for school in self.schools:
            if school.get_mean() > best["mean"]:
                best["school"], best["mean"] = school, school.get_mean()
        return best["school"]
    
    def get_best_student(self) -> Student:
        best = {"student": None, "mean": 0}
        for school in self.schools:
            for student in school.students:
                if student.get_mean() > best["mean"]:
                    best["student"], best["mean"] = student, student.get_mean()
        return best["student"]




        

#################################################################################

for name in ("Bob", "Alice", "John"):
    globals()[f"{name}"] = Student(name)

for i in range(0, 15, 3):
    Bob.add_exam(i)  # type: ignore
    Alice.add_exam(i+2)  # type: ignore
    John.add_exam(i-1)  # type: ignore

print(Bob, Alice, John) # type: ignore

scl = School("Paddy's")

for stud in (Bob, Alice, John): # type: ignore
    scl.add_student(stud)

print(scl.name, scl.get_mean(), scl.get_best_student())

ct = City("Orlando")
ct.add_school(scl)

print(ct.name, ct.get_mean(), ct.get_best_school(), ct.get_best_student())