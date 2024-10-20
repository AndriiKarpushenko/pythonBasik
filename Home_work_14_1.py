# Home work 14.1

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"gender = {self.gender}, age = {self.age}, first_name={self.first_name}, last_name={self.last_name}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        Human.__init__(self, gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"gender = {self.gender}, age = {self.age}, first_name={self.first_name}, last_name={self.last_name}, record_book={self.record_book}"

class GroupFullException(Exception):
    def __init__(self, message="Додано більше 10-ти студентів"):
        self.message = message
        Exception.__init__(self, self.message)

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullException()
        self.group.add(student)

    def delete_student(self, last_name):
        student_delete_from_group = self.find_student(last_name)
        new_group = set()
        for student in self.group:
            if student != student_delete_from_group:
                new_group.add(student)
        self.group = new_group

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            student_info = str(student) + "\n"
            all_students += student_info

        return f'Number:{self.number}\n{all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

students_to_add = [
    Student('Male', 30, 'Ernest', 'Hemingway', 'AN142'),
    Student('Male', 25, 'Ken', 'Kesey', 'AN145'),
    Student('Male', 22, 'Mark', 'Twain', 'AN11'),
    Student('Female', 23, 'Emily', 'Dickinson', 'AN12'),
    Student('Male', 24, 'F. Scott', 'Fitzgerald', 'AN13'),
    Student('Male', 21, 'J.D.', 'Salinger', 'AN14'),
    Student('Male', 26, 'Stephen', 'King', 'AN15'),
    Student('Male', 27, 'O.', 'Henry', 'AN16'),
    Student('Male', 28, 'Charles', 'Dickens', 'AN17'),
    Student('Female', 29, 'Flannery', 'O’Connor', 'AN18'),
    Student('Male', 20, 'Jack', 'Kerouac', 'AN19')  # 11-й студент
]

gr = Group('PD1')

for student in students_to_add:
    try:
        gr.add_student(student)
        print(f"Студент {student.first_name} {student.last_name} успішно доданий.")
    except GroupFullException as e:
        print(f"Виняток при додаванні студента {student.first_name} {student.last_name}: {e}")

print(gr)


