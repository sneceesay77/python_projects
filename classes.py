
class Tutorial:
    """Modelling a Tutorial class""" #a docstring, mainly printed in documentation
    
    #constructor
    def __init__(self, module_name, max_students):
        self.module_name = module_name
        self.max_students = max_students
    
    def display_max_stud(self):
        print(f"Maximum number of students in this {self.module_name.title()} is {self.max_students}")
    
    def display_module_name(self):
        print(f"The name of this module is {self.module_name}")

    def get_name(self):
        return self.module_name
    

my_tutorial = Tutorial("Programming Data", 7)
print(f"The name of the module is: {my_tutorial.module_name}")
print(f"The max number of students is: {my_tutorial.max_students}")
print("==========================================================")

my_tutorial.display_max_stud()
my_tutorial.display_module_name()
print(f"Tutorial name is: {my_tutorial.get_name()}")

        