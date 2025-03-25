def horner(wsp,value):
    lenght = len(wsp)
    result = wsp[0]

    for i in range(1,lenght):
        result = result * value + wsp[i]
    return result

#polynomial = [1,0,1,-1]
#print(horner(polynomial,1))