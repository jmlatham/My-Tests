class parentClass:
  lastName="Latham"
  def __init__(self, name):
    self.name = name
  def printName(self):
    print(self.name,self.lastName)