print("Beginning of code")
name = "Jasper"
def Enter_name(name):
    name = input("Enter your name: ")
    print(name)

Enter_name(name)
print(name)
print("End of code")  

#Functions with parameters
#Bio Data Function

def Bio_data(name, age, sex):
    name = input("Enter your name: ")
    age = int(input("Enter your age:"))
    sex = input("Enter your sex: ")

    print(name, age, sex)

Bio_data("Caxton",22 , "Male")
