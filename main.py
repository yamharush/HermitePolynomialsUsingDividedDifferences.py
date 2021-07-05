import math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'


def printPoints(listOfPoints):
    """This function print the list of points
    :param listOfPoints: list of points ( x , y )
    :return: no return value
    """
    for i in range(len(listOfPoints)):
        point = " ( "
        for j in range(len(listOfPoints[i])):
            point += str(listOfPoints[i][j])
            if j < 1:
                point += " , "
        point += " ) "
        print(point)
    print(" ")


def printDerivativeValues(listOfDerivativeVal):
    """This function prints the list Of derivative values
    :param listOfDerivativeVal: list of ( x , y' )
    :return: no return value
    """
    for i in range(len(listOfDerivativeVal)):
        point = " f'( "
        for j in range(len(listOfDerivativeVal[i])):
            point += str(listOfDerivativeVal[i][j])
            if j < 1:
                point += " ) = "
        # point += " ) "
        print(point)
    print(" ")


def HermitePolynomialsUsingDividedDifferences(pointsList, derivedValues, value):
    """ This function calculates Hermite Polynomials using Divided Differences
    :param pointsList: list of points [x,y]
    :param derivedValues: the value of the points in the derivative
    :param value:specific x val
    :return: the value of y at the given point
    """
    rows = len(pointsList) * 2  # multiply the number of points - size of z table
    ZTable = [[0]] * rows  # build z table
    tempTable = [[0] * 2] * rows
    i, j = 0, 0
    while i != rows:  # initialize z table
        ZTable[i] = [pointsList[j][1]]
        ZTable[i + 1] = [pointsList[j][1]]
        tempTable[i] = pointsList[j]
        tempTable[i + 1] = pointsList[j]
        i = i + 2
        j = j + 1
    temp = 0
    for i in range(0, (rows - 1)):
        if i % 2 == 0:
            ZTable[i].append(derivedValues[temp][1])
            temp += 1
        else:
            ZTable[i].append((ZTable[i + 1][0] - ZTable[i][0]) / (tempTable[i + 1][0] - tempTable[i][0]))

    i, n = 0, 0
    k = 2
    j = 1

    while n <= rows - 2:
        for i in range(rows - k):
            ZTable[i].append((ZTable[i + 1][j] - ZTable[i][j]) / (tempTable[i + k][0] - tempTable[i][0]))
        j += 1
        i = 0
        k += 1
        n += 1

    i, k, p = 2, 2, 2
    j = 0

    result = (pointsList[0][1]) + ((derivedValues[0][1]) * (value - pointsList[0][0]))  # the solution
    for i in range(len(ZTable[0])):  # calculate hermit polynomial
        mul = 1
        if i < len(ZTable[0]) - 2:
            for j in range(k):
                mul = mul * (value - tempTable[j][0])
            result += ZTable[0][p] * mul
            j = 0
            p += 1
            if i != (len(ZTable[0]) - 1):
                k += 1
    i = 1
    strOfDividing = "\t Z|\t"
    for _ in ZTable[0]:
        strOfDividing += str(i) + "nd divided diff|\t"
        i = i + 1
    i, j = 0, 0
    print(" ")
    print(bcolors.MAGENTA+strOfDividing+bcolors.ENDC)
    for row in ZTable:
        strOfRow = "z" + str(i) + "=" + str(tempTable[i][j]) + "\t\t"
        k = 0
        for _ in row:
            strOfRow += str(row[k]) + "\t"
            k = k + 1
        print(strOfRow)
        i = i + 1
        if j % 2 == 0 and j > 0:
            j = j + 1
    print("\n")

    i, k, p = 2, 2, 2
    j = 0

    print("H{0}({1}) = ".format(rows - 1, value), end=" ")
    print("{0}  + {1} * {2} ".format(tempTable[0][1], derivedValues[0][1],
                                     (math.ceil((value - pointsList[0][0]) * 1000) / 1000)), end=" ")

    for i in range(len(ZTable[0])):  # hermite polynomial
        mul = 1
        if i < len(ZTable[0]) - 2:
            for j in range(k):
                mul = mul * (value - tempTable[j][0])
            print("+ {0} * {1} ".format(ZTable[0][p], math.ceil(mul * 100000000) / 100000000), end=" ")
            j = 0
            p += 1
            if i != (len(ZTable[0]) - 1):
                k += 1

    print(bcolors.BOLD + bcolors.OKBLUE + "\n\n-----> Final Result: H{0}({1}) = {2}".format(rows - 1, value, result))
    return result


def main():
    print("----------------Hermite Polynomials using Divided Differences----------------")
    print(
        bcolors.BOLD + bcolors.GREEN + "\nH₂ₙ₊₁(X) = f[z₀] + sigma from k = 1 to 2n+1 of f[z₀,...,zₖ](x-z₀)(x-z₁)···("
                                       "x-zₖ₋₁) \n" + bcolors.ENDC)
    print("-----------------------------------------------------------------------------")
    listOfPoints_x_y = [[1.3, 0.620086], [1.6, 0.4554022], [1.9, 0.2818186]]
    derivativeValues = [[1.3, -0.5220232], [1.6, -0.5698959], [1.9, -0.5811571]]
    print(bcolors.MAGENTA + "The points ( x , y ): ")
    printPoints(listOfPoints_x_y)
    print("The points ( x , y' ) ")
    printDerivativeValues(derivativeValues)
    print(bcolors.ENDC + bcolors.BOLD + "The table: ")
    HermitePolynomialsUsingDividedDifferences(listOfPoints_x_y, derivativeValues, 1.5)


if __name__ == "__main__":
    main()

"""
b = [[1, 0], [2, 0.6931]]
bDer = [[1, 1], [2, 0.5]]
HermitePolynomialsUsingDividedDifferences(b, bDer, 1.5)

listOfPoints_x_y = [[1.3, 0.620086], [1.6, 0.4554022], [1.9, 0.2818186]]
derivativeValues = [[1.3, -0.5220232], [1.6, -0.5698959], [1.9, -0.5811571]]
HermitePolynomialsUsingDividedDifferences(listOfPoints_x_y, derivativeValues, 1.5)

listOfPoints_x_y = [[0, 1], [1, math.e]]
derivativeValues = [[0, 1], [1, math.e]]
HermitePolynomialsUsingDividedDifferences(listOfPoints_x_y, derivativeValues, 1.5)
"""
