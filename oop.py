# Use of object oriented programming in python
class Car:
    def __init__(self,name="",engine=""):
        self.name = name
        self.engine = engine
# self refers to an individual object
car1=Car("Subaru","EJ20")
car2=Car("Supra","2JZ-GTE")
car3=Car("Skyline GTR","RB26DETT")

print("The spec for car 1 are: " + car1.name + " " +car1.engine )
print("The spec for car 2 are: " + car2.name + " " + car2.engine)
print("The spec for car 3 are: " + car3.name + " " + car3.engine)
