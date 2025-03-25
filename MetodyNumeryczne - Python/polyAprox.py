import sympy as sp
import numpy as np
 
def polyAprox (points, m):
 
    x = sp.symbols('x')
 
    #listy x i y
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
 
    matrix = []
    for i in range(len(points)):
        matrix.append([])
        for j in range(m + 1):
            matrix[i].append(0)

    #macierz
    for i in range(len(points)):
        for j in range(m + 1):
            matrix[i][j] = np.power(x_values[i] , j)
 
    #obliczanie parametru  
    wsp = [i for i in range(len(points))]
    a, b, c, d = sp.symbols('a b c d')
    symbolArr = (d,c,b,a)
    symbolArr=symbolArr[-m:]
 
    for i in range(len(points)):
        temp = 0
        for j in range(m):
            temp += matrix[i][j]  * symbolArr[j]
        temp =temp- y_values[i]
        print(temp)
        wsp[i]=temp
    suma = 0

    for i in range(len(wsp)):
        suma += np.power(wsp[i],2)

    pochodnaSumy = [i for i in range(m)]
    
    for i in range(m):
        pochodnaSumy[i]=sp.diff(suma, symbolArr[len(symbolArr) - i-1 ])
 
    solution = sp.solve(pochodnaSumy, symbolArr)
 
    stopien = len(symbolArr) - 1
    przyblizonyWielomian = 0
    for i in range(len(symbolArr)):
        przyblizonyWielomian += solution[symbolArr[len(symbolArr) - i-1]] * np.power(x,stopien)
        stopien =stopien- 1
    print("Przyblizony wielomian: ",przyblizonyWielomian)
    return przyblizonyWielomian
 

points = [(0, 4), (3, 5), (6, 4), (9, 1), (12, 2)]
func = polyAprox(points, 2)
 