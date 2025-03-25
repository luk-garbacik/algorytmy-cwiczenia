import sympy as sp
import numpy as np
 
def lagrang (points):
 
    x = sp.symbols('x')
 
    #zapisuje listę x i listę y
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
 
    #obliczam wielomian interpolacyjny
    interpoplacjaLagr = 0
    for i in range(len(points)):
        wsp = 0
        top = 1
        bot = 1
        y = y_values.pop(i)
        X = x_values.pop(i)
 
        for j in range(len(x_values)):
            top *=  x - x_values[j]
            print(" " * i*3 + "top: x - {}".format(x_values[j]))
            bot *= X - x_values[j]
            print(" " * i*3 +"bot: {} - {}".format(X,x_values[j]))
 
        wsp = top / bot
        y_values.insert(i, y)
        x_values.insert(i, X)
 
        interpoplacjaLagr += y_values[i] * wsp
 
    return sp.simplify(interpoplacjaLagr)
 

points = [(1, 4), (2, 5), (3, 6)]
funkcja = lagrang(points)
print("\n\nFunkcja interpolacji:", funkcja)

 