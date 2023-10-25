def greet(name="User"):
    """
    This function greets the user by name.
    """
    print("Hello, " + name + "!")
    
greet()  # Output: Hello, User!
greet("Alice")  # Output: Hello, Alice!


def get_name_and_age():
    """
    This function returns a tuple containing name and age.
    """
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

name, age = get_name_and_age()
print("Name:", name)
print("Age:", age)
