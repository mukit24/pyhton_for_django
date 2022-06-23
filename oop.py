class Dog:
    species = 'Canis Familaries'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def speak(self,sound):
        return f"{self.name} says {sound}"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

leo = Dog('leo',5)
print(leo.age)
print(leo.speak('woof woof'))
print(leo)
print(isinstance(leo,Dog))

class GoldenRetrive(Dog):
    def speak(self, sound='yooo'):
        return super().speak(sound)

brad = GoldenRetrive('brad',12)
print(brad.speak())