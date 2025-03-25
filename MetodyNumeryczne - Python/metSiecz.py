from Horner1 import horner
import math
#TODO użyj sympy

def derivative(func, x, h=1e-6):
    return (func(x + h) - func(x)) / h

def second_derivative(func, x, h=1e-6):
    return (derivative(func, x + h, h) - derivative(func, x, h)) / h

def is_twice_differentiable(func, x, h=1e-6):
    try:
        first_derivative_value = derivative(func, x, h)
        second_derivative_value = second_derivative(func, x, h)
        return True
    except:
        return False

def is_twice_differentiable_over_range(func, a, b, num_points=100, h=1e-6):
    
    interval = (b - a) / num_points
    for i in range(num_points):
        x = a + i * interval
        if not is_twice_differentiable(func, x, h):
            return False
    return True

def metSiecz (equation, a, b, E):
    counter = 0
    x_n = 0
    x_prev_prev = b
    x_prev = 0

    # warunek: twierdzenie bolzano cauchy'ego
    if (equation(a) * equation(b) >= 0):
        print("twierdzenie bolzano cauchy'ego nie zostało spełnione")
        return
    # warunek: czy funkcja jest dwukrotnie różniczkowalna
    if (not is_twice_differentiable_over_range(equation, a, b)):
        print("funkcja nie jest 2-krotnie różniczkowalna na przedziale [{},{}]".format(a,b))
        return
    # warunek: czy f`(x) * f``(x) > 0 ,jest prawdziwe dla x=a lub x=b
    if (( derivative(equation , a) * second_derivative(equation , a) <= 0 ) and (  derivative(equation , b) * second_derivative(equation , b) <= 0  )):
        print("derivative(equation , a) * second_derivative(equation , a) = {}" .format(derivative(equation , a) * second_derivative(equation , a)))
        print("Nie spełniono warunku nr3")
        return
    # oblicz x_2
    x_n = b - ( equation(b) * ( b - a ) )/( equation(b) - equation(a) )
    #print(x_n)

    while(True):
        x_prev = x_n
        x_n = x_prev - ( equation(x_prev) * ( x_prev - x_prev_prev ) )/( equation(x_prev) - equation(x_prev_prev) )
        print("krok = {}:  x_{} = {}, (x_n - x_prev) = {}" .format(counter+1,counter+3,x_prev,abs(x_n - x_prev)))
        
        #check
        #if(equation(x_n) * equation(x_prev) > 0):
        #    print("x={}   f:{}   : x_p={}  f:{}     : twierdzenie bolzano cauchy'ego nie zostało spełnione" .format(x_n,equation(x_n),x_prev,equation(x_prev)))
        #    return
        
        #sprawdź czy osiognięto E
        if(abs(x_n - x_prev) < E or x_n - x_prev == 0):
            print("\n\nx = {}, obliczono w {} krokach".format(x_n, counter+1))
            return
        
        x_prev_prev = x_prev
        counter = counter + 1

"""
#ex1
wsp = [1,0,-2]       
# anonimowa funkcja lambda przyjmująca argument x
equation = lambda x: horner(wsp, x)

metSiecz(equation,1,2,0.01)
"""

"""
#ex2
wsp = [1,1,-3,-3]       
# anonimowa funkcja lambda przyjmująca argument x
equation = lambda x: horner(wsp, x)

metSiecz(equation,1,2,0.1)
"""

#ex3
# anonimowa funkcja lambda przyjmująca argument x
equation = lambda x: math.sin(x) - x/2
metSiecz(equation, math.pi/2, math.pi, 0.01)

