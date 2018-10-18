# project 5 ITS 5900 by Collins Ojo.  ===> uses python 3.5
import math
import sys
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Logarithm base e")
print("6.Log base 10")
print("7.Log base 2")
print("8.sum of no. and ln")
print("9.sum of no. and log10")
print("10.sum of no. and log2")
print("11.diff of no. and ln")
print("12.diff of no. and log10")
print("13.diff of no. and log2")
print("Type 'quit' to exit")

choice = input("Enter choice(between 1 to 13) or 'quit' to exit:")

#function for basic calculator
def basicCalc(x, y):
    if choice == '1':
        return x + y
    elif choice == '2':
        return x - y
    elif choice == '3':
        return x * y
    elif choice == '4':
        return x / y
#function for log of a single number        
def logCalc(x):
    if choice == '5':
        return math.log(x)
    elif choice == '6':
        return math.log10(x)
    elif choice == '7':
        return math.log2(x)
#compound expression implementation 
def logCalc2(x, y):
    if choice == '8':
        return (y + math.log(x))
    elif choice == '9':
        return (y + math.log10(x))
    elif choice == '10':
        return (y + math.log2(x))
    elif choice == '11':
        return (y - math.log(x))
    elif choice == '12':
        return (y - math.log10(x))
    elif choice == '13':    
        return (y - math.log2(x))

while choice == '1':     
        try:
            x = round(float(input("Enter first number: ")), 4)
            y = round(float(input("Enter second number: ")), 4)
            print(x,"+",y,"=", basicCalc(x,y))
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")  
while choice == '2':
        try:
            x = round(float(input("Enter first number: ")), 4)
            y = round(float(input("Enter second number: ")), 4)
            print(x,"-",y,"=", basicCalc(x,y))
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")
while choice == '3':
        try:
            x = round(float(input("Enter first number: ")), 4)
            y = round(float(input("Enter second number: ")), 4)
            print(x,"*",y,"=", basicCalc(x,y))
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")
while choice == '4':
        try:
            x = round(float(input("Enter first number: ")), 4)
            y = round(float(input("Enter second number: ")), 4)
            print(x,"/",y,"=", basicCalc(x,y))
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")
while choice == '5':
        
        try:
            x = round(float(input("Enter number to get the natural log: ")), 4)
            print(logCalc(x))
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")
while choice == '6':
        try:
            x = round(float(input("Enter number to get the log to base 10: ")), 4)
            print(logCalc(x))
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")
while choice == '7':
        try:
            x = round(float(input("Enter number to get the log to base 2: ")), 4)
            print(logCalc(x))
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")
while choice == '8':
        try:
            x = round(float(input("Enter first number: ")), 4)
            y = round(float(input("Enter second number: ")), 4)
            print(logCalc2(x, y))
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")
while choice == '9':
        try:
            x = round(float(input("Enter first number: ")), 4)
            y = round(float(input("Enter second number: ")), 4)
            print(logCalc2(x, y))
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")  
while choice == '10':
        try:
            x = round(float(input("Enter first number: ")), 4)
            y = round(float(input("Enter second number: ")), 4)
            print(logCalc2(x, y))
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")
while choice == '11':
        try:
            x = round(float(input("Enter first number: ")), 4)
            y = round(float(input("Enter second number: ")), 4)
            print(logCalc2(x, y))
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")
while choice == '12':
        try:
            x = round(float(input("Enter first number: ")), 4)
            y = round(float(input("Enter second number: ")), 4)
            print(logCalc2(x, y)) 
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")
while choice == '13':
        try:
            x = round(float(input("Enter first number: ")), 4)
            y = round(float(input("Enter second number: ")), 4)
            print(logCalc2(x, y))
        except ValueError:
            z = input("do you want to exit? if yes, type 'quit' to exit: ")
            if z == 'quit':
                sys.exit()
            else:
                print("please enter a number to continue")
else:
    print("Invalid input")    