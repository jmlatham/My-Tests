from .childClass import childClass

class grandchildClass(childClass):
  lastName="Smith"
  def __init__(self, name):
    self.name = name