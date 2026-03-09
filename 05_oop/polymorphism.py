# Basic Polymorphism
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meow")

animals = [Dog(), Cat()]

for a in animals:
      a.speak()
      
      

# Employee System
class Employee:
    def get_salary(self):
        return 50000
    
class Manager(Employee):
    def get_salary(self):
        return 100000
    
class Intern(Employee):
    def get_salary(self):
        return 2000
    
employees = [Employee(), Manager(), Intern()]
for b in employees:
   print(b.get_salary())
   
   


# AI Model
class AIModel:
    def predict(self):
        print("Genric Prediction")

class MLModel(AIModel):
    def predict(self):
        print("Machine Learning Prediction")

class DLModel(AIModel):
    def predict(self):
        print("Deep Learnign Model")

models = [MLModel(), DLModel(), AIModel()]

for m in models:
    m.predict()
    
    


# Function Ploymorphism
def add(a, b, c=0):
    return a + b + c

print(add(2, 3))
print(add(2, 3, 4))



# Shape area
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 10 * 5
    
class Circle(Shape):
    def area(self):
        return 3.14 * 7 * 7
    
shapes = [Rectangle(), Circle()]
for s in shapes:
    print(s.area())

    

