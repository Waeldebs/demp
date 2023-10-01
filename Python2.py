class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greeting(self):
        return f"hello my name is {self.name}"

    Person1 = Person("Mark", 2)
    Person2 = Person("Harry", 5)

    
    greeting(Person2)




class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(10, 20)
v2 = Vector(5, 6)
v3 = Vector(9, 6)




def multiplicator(B):
    return C == B*2


def outerfunction(X, Z, B):
    Prix_call = X * Z
    Results = Prix_call / B 
    return Results
    
outerfunction(1, 2, multiplicator(B))
      


def outer_function(x):
    # This is the outer function
    def inner_function(y):
        # This is the inner function
        return y * 2
    
    result = x + inner_function(6)
    return result

# Calling the outer function
result = outer_function(5)
print(result)  # Output: 15
