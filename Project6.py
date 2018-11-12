
#Basic Calculator script
import math
print("1 for sum; 2 for subtraction; 3 for division; 4 for multiplication; 5 for ln(x); 6 for log10; 7 for log2; 8 for add log10")
choice = input("Your task: ")
def basicCalc():
    while True:
        try:
            if choice == '1':
                a, b, = input("enter your values in this format 'x + y': ").split('+')
                a1 = float(a)
                b1 = float(b)
                Sum = a1+b1
                print(Sum)
                continue
            elif choice == '2':
                a, b, = input("enter your values in this format 'x - y': ").split('-')
                a1 = float(a)
                b1 = float(b)
                Minux  = a1 - b1
                print(Minux)
                continue
            elif choice == '3':
                a, b, = input("enter your values in this format 'x / y': ").split('/')
                a1 = float(a)
                b1 = float(b)
                Divide = a1/b1
                print(Divide)
                continue
            elif choice == '4':
                a, b, = input("enter your values in this format 'x * y': ").split('*')
                a1 = float(a)
                b1 = float(b)
                Multiply = a1*b1
                print(Multiply)
                continue
            elif choice == '5':
                b, a = input("enter your value in this format 'ln x': ").split('ln')
                a1 = float(a)
                print(math.log(a1))
                continue
            elif choice == '6':
                b, a = input("enter your values in this format 'log x': ").split('log')
                a1 = float(a)
                print(math.log10(a1))
                continue
            elif choice == '7':
                b, a = input("enter your value in this format 'log2 x': ").split('log2')
                a1 = float(a)
                print(math.log2(a1))
                continue
            elif choice == '8':
                a, b, = input("enter your values in this format 'x + log y' : ").split('+ log')
                a1 = float(a)
                b1 = float(math.log10(float(b)))
                Sum = a1 + b1
                print(Sum)
                continue
            else:
                print("invalid value")
        except ValueError:
            print("read instructions")
            
basicCalc()

