from Horner1 import horner
import math
import sympy
#TODO użyj sympy

def derivative(func, x, h=1e-6):
    return (func(x + h) - func(x)) / h

def second_derivative(func, x, h=1e-6):
    return (derivative(func, x + h, h) - derivative(func, x, h)) / h

def metStycz (equation, a, b, E):
    counter=0
    x_n=0

    # warunek: twierdzenie bolzano cauchy'ego
    if (equation(a) * equation(b) >= 0):
        print("twierdzenie bolzano cauchy'ego nie zostało spełnione")
        return
    
    while(True):
        #sprawdź który koniec spełnia warunek f(?)*f``(?) < 0
        #koniec "a"
        if(equation(a) * second_derivative(equation,a) <= 0):
            if(counter == 0):
                x_n = a
            else:
                x_n = x_n - ( equation(x_n) )/( derivative(equation, x_n) )
            counter = counter + 1
            print("krok: {}, x_{} = {}" .format(counter,counter,x_n))
        #koniec "b"
        elif (equation(b) * second_derivative(equation,b) <= 0):
            if(counter == 0):
                x_n = b
            else:
                x_n = x_n - ( equation(x_n) )/( derivative(equation, x_n) )
            counter = counter + 1
            print("krok: {}, x_{} = {}" .format(counter,counter,x_n))
        else:
            print("ERR")
            return
        
        #sprawdź czy osiognięto E
        if(abs(equation(x_n)) < E):
            print("\n\n\nx = {}, obliczono w {} krokach".format(x_n, counter))
            return

"""
#ex1
wsp = [-1,16,17]       
# anonimowa funkcja lambda przyjmująca argument x
equation = lambda x: horner(wsp, x)

metStycz(equation,-8,4,0.1)
"""

#ex2
# anonimowa funkcja lambda przyjmująca argument x
equation = lambda x: math.sin(x) - x/2
metStycz(equation, math.pi/2, math.pi, 0.01)

