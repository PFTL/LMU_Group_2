from person import Person


class Student(Person):
    def __init__(self, name, last_name, course):
        super().__init__(name, last_name)
        self.course = course




if __name__ == '__main__':
    s = Student('Aquiles', 'Carattino', 'Physics')
    s.get_full_name()
