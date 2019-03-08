#This is a simple file

print('Hello python')


for i in range(30):
    print('This is line: ', i+1)

class player:
    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.num = num

kobe = player('Kobe', 30, 24)

print(kobe.name)

print(kobe.age)

print(kobe.num)



