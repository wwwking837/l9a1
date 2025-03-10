class Employee:

    def __init__(self):
        print('Employee created.')
        
    def _del_(self):
        print('Destructor called, Employee deleted')

obj = Employee()
del obj

class student:
    def __init__(self):
        print('Student created')
    def _del_(self):
        print('Destructor called, Student deleted')
obj = student()
del obj