from classes.firstClass import FirstClass
from classes.printTest import PrintTests
from classes.exampleClass import ExampleClass
from classes.grandchildClass import grandchildClass
from classes.childClass import childClass
from classes.parentClass import parentClass

def printMenu():
  moduleList={"1":"Slices","2":"Indexing Ord & Chr", "3":"Try/Except", "4":"FirstClass","5":"PrintTests","6":"ExampleClass", "7":"FamilyClasses","8":"Bitwise Logical Operators","9":"Bitwise Shift Operators","10":"Modules"}
  for key in moduleList:
    print(key, moduleList[key], sep=". ")

def runBitwiseLogicalOperators():
  print("biwise logical operators")
  print("------------------------")
  i=0
  j=0
  k=(i and j)
  l=(i or j)
  print("i=",i)
  print("j=",j)
  print("k=",k)
  print("l=",l)
  print("\n")

  k=(i & j)
  l=(i | j)
  m=(i ^ j)
  n=~i
  print("i=",i)
  print("j=",j)
  print("k=",k)
  print("l=",l)
  print("m=",m)
  print("n=",n)
  print("\n")

def runBitwiseShiftOperators():
  print("bitwise shift operators")
  print("-----------------------")
  var = 17
  varRight = var >> 1
  varLeft = var << 2
  print("var=",var, "varRight=",varRight, "varLeft=",varLeft)
  print("var", "R", "L", sep="\t")
  print(var, varRight, varLeft, sep="\t")
  print(var, var/2, var*4, sep="\t")
  print("\n")

def runFirstClass():
  print("FirstClass class tests")
  print("----------------------")
  fClass = FirstClass()
  fClass.speak()
  print(fClass.color)
  print("\n"*2)

def runPrintTests():
  print("PrintTests class tests")
  print("----------------------")
  pClass = PrintTests()
  #pClass.printTest1()
  pClass.printTest2()
  pClass.printTest3()
  pClass.printTest4()
  pClass.printTest5()
  pClass.printTest6()
  pClass.printTest7()
  pClass.printTest8()
  pClass.printTest9()
  #pClass.printTest0()
  print("\n"*2)

def runExampleClass():
  print("ExampleClass class tests")
  print("------------------------")
  eClass = ExampleClass("instanceA", 1)
  print("eClass values:",eClass.name, eClass.description, eClass.getNumber(), sep=" - ")
  print(eClass.exampleMethod())
  print("eClass print method results:")
  eClass.printMethod(256)
  eClass.printMethod("WORD")
  print("eClass values A:",eClass.instanceA)
  print("eClass values A:",eClass.getInstanceA())
  print("eClass values B:",eClass.instanceB)
  print("eClass values B:",eClass.getInstanceB())
  fClass = ExampleClass("instanceB", 2)
  print("fClass values:",fClass.name, fClass.description, fClass.getNumber(), sep=" - ")
  print("fClass values:",fClass.instanceA)
  print("fClass values:",fClass.getInstanceA())
  print("fClass values B:",fClass.instanceB)
  print("fClass values B:",fClass.getInstanceB())
  # finish testing the instance variables!!!!
  print("changing eClass values")
  eClass.name = "new eClass Name"
  eClass.description = "new eClass Description"
  eClass.number = 79
  ExampleClass.name = "Example Class new Name"
  ExampleClass.number = 456
  eClass.instanceA = "new eClass Instance A"
  eClass.setInstanceB("new eClass Instance B")
  print("eClass values:",eClass.name, eClass.description, eClass.number, sep=" - ")
  print(eClass.exampleMethod())
  print("eClass print method results:")
  eClass.printMethod(256)
  eClass.printMethod("WORD")
  print("eClass values A:",eClass.instanceA)
  print("eClass values A:",eClass.getInstanceA())
  print("eClass values B:",eClass.instanceB)
  print("eClass values B:",eClass.getInstanceB())
  #fClass = ExampleClass()
  print("fClass values:",fClass.name, fClass.description, fClass.number, sep=" - ")
  print("fClass values A:",fClass.instanceA)
  print("fClass values A:",fClass.getInstanceA())
  print("fClass values B:",fClass.instanceB)
  print("fClass values B:",fClass.getInstanceB())
  eClass.setInstanceC("wow")
  print("eClass InstanceC:", eClass.getInstanceC())
  #print("fClass InstanceC:", fClass.instanceC)
  fClass.setInstanceC("WOW")
  print("fClass InstanceC:", fClass.getInstanceC())
  print("eClass InstanceC:", eClass.getInstanceC())
  print("fClass InstanceC:", fClass.instanceC)
  print("eClass InstanceC:", eClass.instanceC)
  eClass.dog = "Jasmine"
  print(eClass.dog)
  #print(fClass.dog)
  print("\n"*2)

def runFamilyClasses():
  print("Family Classes class tests")
  print("--------------------------")
  pClass = parentClass("Marshall")
  cClass = childClass("Jonathan")
  gChild = grandchildClass("Joe")
    
  print(type(pClass).__name__, end=": ")
  pClass.printName()
  print(type(cClass).__name__, end=": ")
  cClass.printName()
  print(type(gChild).__name__, end=": ")
  gChild.printName()
  print("\n"*2)

def runModules():
  # from 5.1.3.3
  #import module

  # from 5.1.3.4
  # main.py

  from module import suml, prodl

  zeroes = [0 for i in range(5)]
  ones = [1 for i in range(5)]
  count1 = [i+1 for i in range(5)]
  count2 = [i*2 for i in range(5)]
  print(suml(zeroes))
  print(prodl(ones))
  print(count1)
  print(suml(count1))
  print(count2)
  print(prodl(count2))

def runSlices():
  print("Slices #5.1.8.7")
  print("\n" * 3)

  # Slices

  alpha = "abcdefghijklmnopqrstuvwxyz"

  print("1",alpha[1:3])
  print("2",alpha[3:])
  print("3",alpha[:3])
  print("4",alpha[3:-2])
  print("5",alpha[-3:4])
  print("6",alpha[::2])
  print("7",alpha[1::2])

def runTryExcept():
  # 5.1.4.9
  print("5.1.4.9")
  try:
      x = int(input("Enter a number: "))
      y = 1 / x
      print(y)
  except ZeroDivisionError:
      print("You cannot divide by zero, sorry.")
  except ValueError:
      print("You must enter an integer value.")
  except:
      print("Oh dear, something went wrong...")

  print("THE END.")

def runIndexingOrdChr():
  # Indexing strings

  exampleString = 'silly walks'

  for ix in range(len(exampleString)):
      print(exampleString[ix], end=' ')
  print()
  ords = []
  for ix in range(len(exampleString)):
      num = ord(exampleString[ix])
      ords.append(num)
      print(num, end=' ')
  print()
  for ix in range(len(exampleString)):
      print(chr(ords[ix]), end=" ")
  #print(ords)
  print()



# Refactor this program to ask what part I want to execute and then execute that part
# Write the code so that the options are in a list, so I only have to add the item to the list and add the code to file.
# Build the menu from the list

while True:
  printMenu()
  
  modToRun = input("Enter your choice: ")

  if modToRun == "1":
    runSlices()
  elif modToRun == "2":
    runIndexingOrdChr()
  elif modToRun == "3":
    runTryExcept()
  elif modToRun == "4":
    runFirstClass()
  elif modToRun == "5":
    runPrintTests()
  elif modToRun == "6":
    runExampleClass()
  elif modToRun == "7":
    runFamilyClasses()
  elif modToRun == "8":
    runBitwiseLogicalOperators()
  elif modToRun == "9":
    runBitwiseShiftOperators()
  elif modToRun == "10":
    runModules()

  runProgram = input("Do you want to run this program again? ")
  if runProgram != "y" and runProgram != 'y' and runProgram != "Yes" and runProgram != "yes":
    break