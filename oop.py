class name():
   str = 'name'
class Human(name):
   def __init__(self, name, surename):
     self.name = name
     self.surename = surename

   def do(self):
      def q():
         print(123)
      q()

dudar = Human('Vadim', 'Dudar')
dudar.do()