class Person:
    def __init__(self, name, last_name, birth_year=0):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def get_full_name(self):
        print(self.name, self.last_name)

    def calculate_age(self):
        if self.birth_year == 0:
            raise Exception('You must provide a birth year')
        print('The age is', 2019-self.birth_year)



if __name__ == '__main__':
    p = Person('Aquiles', 'Carattino', 1986)
    p2 = Person('John', 'Doe', 1980)

    p.get_full_name()
    p2.get_full_name()
    print(p.birth_year)

    p.calculate_age()
    p2.calculate_age()