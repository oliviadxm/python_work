class Employee():

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=''):
        if amount:
            self.salary = str(int(amount) + int(self.salary))
        else:
            self.salary = str(5000 + int(self.salary))

