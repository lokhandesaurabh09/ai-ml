# Variables and data types
age = 21                                #int
height = 5.9                            #float
name = "Saurabh"                        #string
is_Student = True                       #boolean
skills = ["Python", "Git"]              #list
coordinates = (18.5, 73.8)              #tuple
profile = {"name": name, "age": age}    #dict
unique_ids = {1, 2, 3, 3}               #set 

print(age, type(age))
print(height, type(height))
print(name, type(name))
print(is_Student, type(is_Student))
print(skills, type(skills))
print(coordinates, type(coordinates))
print(profile, type(profile))
print(unique_ids, type(unique_ids))

# Type conversion
print(int("5") + 10)
print(str(10) + " apples")
print(float(3))
print(int(7.9))

# Taking input (always comes as a string)
city = input("Enter your city: ")
print("Hello from", city)