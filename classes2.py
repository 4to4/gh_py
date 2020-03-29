class Student:
    common_name = None
    name = None
    id = None

    def st(self, name="None", id=0):
        self.name = name
        self.id = id
        print(f"Name {self.name} and Id {self.id} and common_name{self.common_name}")

    def __init__(self, cn=" None "):
        self.common_name=cn

    def get_full_name(self):
        print (self.name, self.common_name)

co = Student("Common name")
co.st(name="Nm1", id=12)
co.get_full_name()
print("------------------")
co2 = Student()
co2.st(name="Nm22", id=14)
co.get_full_name()

common_name, name and id are treated as static variables.

Here

class Student:
    common_name = None
#    name = None
#    id = None

    def st(self, name="None", id=0):
        self.name = name    # 1
        self.id = id # 2
        print(f"Name {self.name} and Id {self.id} and common_name{self.common_name}")

    def __init__(self, cn=" None "):
        self.common_name=cn

    def get_full_name(self):
        print (self.name, self.common_name)

co = Student("Common name")
co.st(name="Nm1", id=12)
co.get_full_name()
print("------------------")
co2 = Student()
co2.st(name="Nm22", id=14)
co.get_full_name()

Even though name and id are getting declared implicitly they are not static variables.
Basically you can keep declaring the variable with self. in class method bodies and keep using them.
But if you declare them explicitly in class body then they are treated as static vars and can be accessed directly with class object



# super() method is used to called parent class methods