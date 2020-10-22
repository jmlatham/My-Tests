class PrintTests:
  def printTest1(self):
    print("Hello!")
    print("Welcome to Python Essentials!")
    print("THIS IS SANDBOX MODE.")
    # Click the Run button
    print("WELCOME TO PYTHON ESSENTIALS!")
    print("Hello, World!")
    print("Hello, Python!")
    print("Jonathan1")
  
    #print(Jonathan2)
    #Traceback (most recent call last):
    #  File "main.py", line 3, in <module>
    #    print(Jonathan2)
    #NameError: name 'Jonathan2' is not defined
  
    #print Jonathan3
    #  File "main.py", line 4
    #    print Jonathan3
    #                  ^
    #SyntaxError: Missing parentheses in call to 'print'. Did you mean print(Jonathan3)?
  
    #print "Jonathan4"
    #  File "main.py", line 9
    #    print "Jonathan4"
    #                    ^
    #SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Jonathan4")?
  
    #print 'Jonathan5'
    #  File "main.py", line 14
    #    print 'Jonathan5'
    #                    ^
    #SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Jonathan5')?
  
    print('Jonathan6')
  
    #print('Jonathan7')print("Jonathan8")
    #  File "main.py", line 20
    #    print('Jonathan7')print("Jonathan8")
    #                          ^
    #SyntaxError: invalid syntax
    
    print() # blank line
    print("Jonathan""Marshall""Latham") # concatenates
    print("Jonathan", "Marshall", "Latham") # separated by a space
    print(0, "this is an integer - decimal")
    #print(01)
    #  File "main.py", line 46
    #    print(01)
    #           ^
    #SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
    print(0o5, "this is an octal 5")
    #print(0o8)
    #  File "main.py", line 46
    #    print(01)
    #           ^
    #SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
    print(0o17, "this is an octal 17") # prints 15 - this is octal
    print(0.1)
    print(0b1, "this is a binary 1")
    #print(0b2)
    #  File "main.py", line 46
    #    print(01)
    #           ^
    #SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
    print(0b11, "this is a binary 11") # prints 3
    print(0b100, "this is a binary 100") # prints 4 - this is binary
    print(0xa, "this is a hexadecimal a") # prints 10 - this is hexadecimal
    print()
    print("a \a","a")
    print("b \b","b")
    print("c \c","c")
    print("d \d","d")
    print("e \e","e")
    print("f \f","f")
    print("g \g","g")
    print("h \h","h")
    print("i \i","i")
    print("j \j","j")
    print("k \k","k")
    print("l \l","l")
    print("m \m","m")
    print("n \n","n")
    print("o \o","o")
    print("p \p","p")
    print("q \q","q")
    print("r \r","r")
    print("s \s","s")
    print("t \t","t")
    #print("u \u")
    #  File "main.py", line 89
    #    print("u \u")
    #          ^
    #SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
    print("u-> u4561 \u4561","u")
    print("v \v","v")
    print("w \w","w")
    #print("x \x")
    #  File "main.py", line 97
    #    print("x \x")
    #          ^
    #SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \xXX escape
    print("x->x27 \x27","x")
    print("y \y","y")
    print("z \z","z")
    print("1 \1","1")
    print("2 \2","2")
    print("3 \3","3")
    print("4 \4","4")
    print("5 \5","5")
    print("6 \6","6")
    print("7 \7","7")
    print("8 \8","8")
    print("9 \9","9")
    print("0 \0","0")
    print("\\ \\","\\")
    print("\" \"","\"")
    print("' \'","'")
    print(". \.",".")
    print(", \,",",")
    print("/ \/","/")
    print("[ \[","[")
    print("{ \{","{")
    print("] \]","]")
    print("} \}","}")
    print("| \|","|")
    print("< \<","<")
    print("> \>",">")
    print("? \?","?")
    print("` \`","`")
    print("~ \~","~")
    print("! \!","!")
    print("@ \@","@")
    print("# \#","#")
    print("$ \$","$")
    print("% \%","%")
    print("^ \^","^")
    print("& \&","&")
    print("* \*","*")
    print("( \(","(")
    print(") \)",")")
    print("- \-","-")
    print("_ \_","_")
    print("+ \+","+")
    print("= \=","=")
    print("; \;",";")
    print(": \:",":")

  #2.1.1.19 LAB: Formatting the output
  def printTest2(self):
    print("2.1.1.19 LAB: Formatting the output")
    print("My", "name", "is", "Monty", "Python.", sep="-", end=" ")

    print("What is your name?")
    print("My", "name", "is", sep="_", end="*")
    print("Monty", "Python.", sep="*", end="*\n")
    print("Programming","Essentials","in", sep="***", end="...")
    print("Python")
  
  
  #2.1.1.20 LAB: Formatting the output
  def printTest3(self):
    print("2.1.1.20 LAB: Formatting the output")
    print("Original")
    print("    *")
    print("   * *")
    print("  *   *")
    print(" *     *")
    print("***   ***")
    print("  *   *")
    print("  *   *")
    print("  *****")
    print("1. minimize by using \\n")
    print("    *","   * *","  *   *"," *     *","***   ***","  *   *","  *   *","  *****", sep="\n")
    print("2. make arrow twice as large (but keep the proportions)")
    print("        **")
    print("        **")
    print("      **  **")
    print("      **  **")
    print("    **      **")
    print("    **      **")
    print("  **          **")
    print("  **          **")
    print("******      ******")
    print("******      ******")
    print("    **      **")
    print("    **      **")
    print("    **      **")
    print("    **      **")
    print("    **********")
    print("    **********")
    print("3. duplicate the arrow side by side")
    print("    *    " * 2)
    print("   * *   " * 2)
    print("  *   *  " * 2)
    print(" *     * " * 2)
    print("***   ***" * 2)
    print("  *   *  " * 2)
    print("  *   *  " * 2)
    print("  *****  " * 2)
    print()

  # 2.1.2.2 Python literals
  def printTest4(self):
    print("Original")
    print("2")
    print(2)
    print("Test 1")
    print("2" * 2)
    print(2 * 2)
    print("Test 2")
    #print("2" * "2")
    #Traceback (most recent call last):
    #  File "main.py", line 9, in <module>
    #    print("2" * "2")
    #TypeError: can't multiply sequence by non-int of type 'str'
    print(11111111)
    print(11_111_111) # the underscores are removed automatically
    print(-11111111)
    print(-11_111_111) # the underscores are removed automatically
    print("   11111111",11111111, sep=" = ")
    print(" 11_111_111",11_111_111, sep=" = ")
    print("  -11111111",-11111111, sep=" = ")
    print("-11_111_111",-11_111_111, sep=" = ")
    print(" 11111111   +   2222222",11111111 + 2222222, sep=" = ")
    print(" 11_111_111 + 2_222_222",11_111_111 + 2_222_222, sep=" = ")
    print("-11111111   +   2222222",-11111111 + 2222222, sep=" = ")
    print("-11_111_111 + 2_222_222",-11_111_111 + 2_222_222, sep=" = ")
  
  # 2.1.2.4 Python Literals
  def printTest5(self):
    print("2.1.2.4 Python Literals")
    print("0o123",0o123, sep=" = ")
    print("0O123",0O123, sep=" = ")
    print("0x123",0x123, sep=" = ")
    print("0X123",0X123, sep=" = ")
  # 2.1.2.5 Python Literals
  def printTest6(self):
    print("2.1.2.5 Python Literals")
    print("0.4",0.4, sep=" = ")
    print(".4 ", .4, sep=" = ")
    print("4.0",4.0, sep=" = ")
    print("4. ", 4., sep=" = ")
    print("0.4*2",0.4*2, sep=" = ")
    print(".4*2 ", .4*2, sep=" = ")
    print("4.0*2",4.0*2, sep=" = ")
    print("4.*2 ", 4.*2, sep=" = ")

  # 2.1.2.6 Python Literals
  def printTest7(self):
    print("2.1.2.6 Python Literals")
    print("300000000", 3E8, sep=" = ")
    print(" 1E1",1E1, sep=" = ")
    print(".1E1", .1E1, sep=" = ")
    print("127E10 * 127E10", 127E10*127E10, sep=" = ")
    print(" 2E10 * 2E10 ", 2E10*2E10, sep=" = ")
    print("2E-10 * 2E-10", 2E-10 * 2E-10, sep=" = ")

  # 2.1.2.10 Python Literals
  def printTest8(self):
    print("2.1.2.10 Python Literals")
    print("True > False", True > False, sep=" = ")
    print("True < False", True < False, sep=" = ")

  # 2.1.2.11 LAB: Python Literals - strings
  def printTest9(self):
    print("2.1.2.11 LAB: Python Literals - strings")
    print("\"I'm\"",'""learning""','"""Python"""', sep="\n")

  # 2.1.3.1 Operators - data manipulation tools
  def printTest0(self):
    print("2+3     ",2+3, sep=" = ")
    print("2-3     ",2-3, sep=" = ")
    print("2*3     ",2*3, sep=" = ")
    print("2/3     ",2/3, sep=" = ")
    print("2.0+3   ",2.0+3, sep=" = ")
    print("2.0-3   ",2.0-3, sep=" = ")
    print("2.0*3   ",2.0*3, sep=" = ")
    print("2.0/3   ",2.0/3, sep=" = ")
    print("2+3.0   ",2+3.0, sep=" = ")
    print("2-3.0   ",2-3.0, sep=" = ")
    print("2*3.0   ",2*3.0, sep=" = ")
    print("2/3.0   ",2/3.0, sep=" = ")
    print("2.0+3.0 ",2.0+3.0, sep=" = ")
    print("2.0-3.0 ",2.0-3.0, sep=" = ")
    print("2.0*3.0 ",2.0*3.0, sep=" = ")
    print("2.0/3.0 ",2.0/3.0, sep=" = ")
    print("-------------------------")
    print("2//3    ",2//3, sep=" = ")   # Integer Division (integer value to the left of the quotient decimal point)
    print("2%3     ",2%3, sep=" = ")    # Modulo (remainder of 2/3)
    print("2**3    ",2**3, sep=" = ")   # Exponent 2^3
    print("2.0//3  ",2.0//3, sep=" = ")
    print("2.0%3   ",2.0%3, sep=" = ")
    print("2.0**3  ",2.0**3, sep=" = ")
    print("2//3.0  ",2//3.0, sep=" = ")
    print("2%3.0   ",2%3.0, sep=" = ")
    print("2**3.0  ",2**3.0, sep=" = ")
    print("2.0//3.0",2.0//3.0, sep=" = ")
    print("2.0%3.0 ",2.0%3.0, sep=" = ")
    print("2.0**3.0",2.0**3.0, sep=" = ")
    print("8//3    ",8//3, sep=" = ")
    print("8.0//3  ",8.0//3, sep=" = ")
    print("8//3.0  ",8//3.0, sep=" = ")
    print("8.0//3.0",8.0//3.0, sep=" = ")