class Employee():

    def __init__(self, name, surname, annual_salary, adding=''):
        self.name = name
        self.surname = surname
        self.annual_salary = annual_salary
        self.adding = adding

    def give_raise(self):
        if self.adding:
            annSal = self.annual_salary + int(self.adding)
            print(annSal)
        else:
            print(self.annual_salary + 5000)

my_employee = Employee("Иван", "Иванов", 8000, 8000)
my_employee.give_raise()