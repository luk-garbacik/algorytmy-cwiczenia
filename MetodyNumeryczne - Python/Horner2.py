def horner(inputPolynomial,binomial):
    lenght = len(inputPolynomial)

    print("( x " + str(binomial) +" ) * ",end="")

    resultingPolynomial = [0] * lenght  # init list

    resultingPolynomial[0] = inputPolynomial[0]
    print("( " + str(resultingPolynomial[0]) + " x^" + str(lenght) + " ", end="")

    for i in range(1,lenght):
        resultingPolynomial[i] = resultingPolynomial[i-1] * binomial + inputPolynomial[i]
        if ( i!=(lenght - 1)):
            print(str(resultingPolynomial[i]) + " x^" + str(lenght - i - 1) + " ", end="")
        else:
            print(str(resultingPolynomial[i]) + " )")

    return resultingPolynomial

polynomial = [2,-6,2,-1]
print(horner(polynomial,3))