import sys 
import math
#These were imported to help with the math calculations and to stop the code from running.
try:
 print("Welcome to the Python™ calculator by [redacted]. (Version 2.0.1 'Final Release')")
 print("Please select an operation. For addition, type a, for subtraction, type s, for multiplication, type m,")
 print("for division, type d, for exponenting, type e, and for square rooting, type sq.")
 operation=input(" You can also get the percentage of a number by typing %. If you want to use sin, cos, or tan, type sct:  ") 
 if operation=="a":
#All operations put a large amount of code in a variable to help make this code simpler and allow for repetition with while loops.
    x = float(input("Insert the base number:  "))
    y = float(input("Insert the number to be additor:  "))
    z=(x+y)
    print("Your answer is", z)
    c=input("Continue? Press Y/N:  ")
    while c=="y":
#While loops were added to allow people to continue a problem, and not just have two step equations be added.
      x = float(input("Insert the additor:  "))
      z=(x+z)
      print(z)
      c=input("Continue? Press Y/N:  ")

 elif operation=="s":
    x = float(input("Insert the minuend:  "))
    y = float(input("Insert the subtrahend:  "))
    z=(x-y)
    print("Your answer is", z)
    c=input("Continue? Press Y/N:  ")
    while c=="y":
      x = float(input("Insert the subtractor:  "))
      z=(z-x)
      print(z)
      c=input("Continue? Press Y/N:  ")

 elif operation=="m":
    x = float(input("Insert the base number:  "))
    y = float(input("Insert the multiplyer:  "))
    z=(x*y)
    print("Your answer is", z)
    c=input("Continue? Press Y/N:  ")
    while c=="y":
      x = float(input("Insert the multiplyer:  "))
      z=(z*x)
      print(z)
      c=input("Continue? Press Y/N:  ")

 elif operation=="d":
    x = float(input("Insert the base number:  "))
    y = float(input("Insert the divisor:  "))
    if y == 0:
      sys.exit("You cannot divide by zero. The whole calculator will implode if attempted. The calculator has been shut down as a result.")
    z=(x/y)
    print("Your answer is", z)
    c=input("Continue? Press Y/N:  ")
    while c=="y":
      x = float(input("Insert the divider:  "))
      if x == 0:
        sys.exit("You cannot divide by zero. The whole calculator will implode if attempted. The calculator has been shut down as a result.")
      z=(z/x)
      print(z)
      c=input("Continue? Press Y/N:  ")

 elif operation=="e":
    x = float(input("Insert the base number:  "))
    y = float(input("Insert the exponenter:  "))
    if x == 0:
      if y== 0:
        sys.exit("It is unknown in the science and math community if 0 exponented by 0 = 0 or 1 right now. To prevent confusion, no answer will be given and the program will be shut down.")
    z=(x**y)
    print("Your answer is", z)
    c=input("Continue? Press Y/N:  ")
    while c=="y":
      x = float(input("Insert the exponenter:  "))
      if x == 0:
        if z == 0:
          sys.exit("It is unknown in the science and math community if 0 exponented by 0 = 0 or 1 right now. To prevent confusion, no answer will be given and the program will be shut down.")
      z=(z**x)
      print(z)
      c=input("Continue? Press Y/N:  ")
      
 elif operation=="sq":
    x = float(input("Insert the base number to be squared:  "))
    z=(math.sqrt(x)) 
#The math import is used here as it is easier than making a square rooting formula.
    print("Your answer is", z)
    c=input("Do you want to square root the answer? Press Y/N:  ")
    while c=="y":
      z=(math.sqrt(x))
      print(z)
      c=input("Do you want to square root the answer? Press Y/N:  ")
    
 elif operation=="%":
    x = float(input("Insert the base number to be percentaged:  "))
    z=(x/100)
    print(z,"%")
  
 elif operation=="sct":
    
    sct=input("sin, con, or tan? (Type only the abreviation):  ")
    if sct=="sin":
      x = float(input("Insert Sine:  "))
      z=(math.sin(x))
      print(z)
    elif sct=="cos":
      x = float(input("Insert Cosine:  "))
      z=(math.cos(x))
      print(z)
    elif sct=="tan":
      x = float(input("Insert tangent:  "))
      z=(math.tan(x))
      print(z)

 else:
    sys.exit("Something went wrong, and the code has been terminated to prevent damage to the computer.")
except ValueError:
  sys.exit("Something went wrong, and the code has been terminated to prevent damage to the computer.")
except OverflowError:
  sys.exit("Something went wrong, and the code has been terminated to prevent damage to the computer.")
except ZeroDivisionError:
  sys.exit("Something went wrong, and the code has been terminated to prevent damage to the computer.")
except KeyboardInterrupt:
   sys.exit("Something went wrong, and the code has been terminated to prevent damage to the computer.") 
