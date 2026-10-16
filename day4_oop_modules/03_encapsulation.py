# Private attribute with validation
class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0

    def set_age(self, age):
        if age < 0:
            print("Invalid age")
        else: 
            self.__age = age
            print("Age set to", age)

    def get_age(self):
        return self.__age

p = Person("Saurabh")
p.set_age(22)
p.set_age(-5)
print(p.get_age())


# Object counter
class Post:
    count = 0

    def __init__(self, caption):
        self.caption = caption
        Post.count += 1

Post("Sunset")
Post("Biryani")
Post("Gym day")
print("Total objects:", Post.count)

