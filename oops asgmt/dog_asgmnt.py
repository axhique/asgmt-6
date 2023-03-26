class dog():
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        return f'Name of dog : {self.name}\nAge of dog : {self.age}'

    def get_info(self):
        return f'Color of {self.name}\'s coat : {self.coat_color}'


class jackrusselterrier(dog):
    def __init__(self,name,age,coat_color,food):
        super().__init__(name,age,coat_color)
        self.food = food

    def run(self):
        return f'{self.name} can run 1000m at a strech'

    def eats(self):
        return f'{self.name} eats {self.food} daily'

class bulldog(dog):
    def __init__(self,name,age,coat_color,color):
        super().__init__(name,age,coat_color)
        self.color = color

    def jump(self):
        return f'{self.name} can jump 3m high'

    def colr(self):
        return f'{self.name} is {self.color} in colour'
 

jk=jackrusselterrier('roxy',3,'red','pedgree')

print(jk.description())
print(jk.get_info())
print(jk.run())
print(jk.eats())

bd=bulldog('ruby',5,'blue','white')

print(bd.description())
print(bd.get_info())
print(bd.jump())
print(bd.colr())


