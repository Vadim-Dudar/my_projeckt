class name():
   str = 'name'
class Human(name):
   def __init__(self, name, surename):
     self.name = name
     self.surename = surename

dudar = Human('Vadim', 'Dudar')
print(dudar.name)