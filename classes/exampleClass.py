class ExampleClass:
  name="Example Class" # class variable
  description="This is an example class." # class variable
  __number=179 # class variable

  def __init__(self, instA, instB):
    self.instanceA = instA
    self.instanceB = instB
    
  def getNumber(self):
    return self.__number

  def exampleMethod(self):
    return "This is an example method"

  def printMethod(self, value):
    print("This is the value you passed: ", value)

  def setInstanceA(self, value):
    self.instanceA = value
  
  def setInstanceB(self, value):
    self.instanceB = value
  
  def getInstanceA(self):
    return self.instanceA
  
  def getInstanceB(self):
    return self.instanceB

  def setInstanceC(self, value):
    self.instanceC = value

  def getInstanceC(self):
    return self.instanceC
