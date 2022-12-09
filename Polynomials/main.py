def number_to_string(argument):
    match argument:
        case 1:
            addition()
        case 2:
            multiplication()
        case 3:
            return "Exiting the process"
            exit();
        case default:
            return "Enter a valid option"
def creating_tuple():
    print("Enter the maximum power")
    power = int(input())
    tuple = ()
    for i in range(power, -1, -1):
        print("Enter the coefficient of power ", i)
        coeff = int(input())
        tuple += (coeff,)
    return tuple
def multiplication():
    from numpy.polynomial import polynomial as P
    p1 = creating_tuple()
    p2 = creating_tuple()
    print(p1)
    print(p2)
    mulRes = P.polymul(p1, p2);
    x = len(mulRes)
    s = ""
    for i in range(x):
        if (mulRes[i] != 0):
            s += str(mulRes[i]) + "x^" + str(i)
    print(s)
    print("Do you want to continue (Y/N")
    choice=input()
    if((choice=="Y") |(choice=="y")):
        return multiplication()
    else:
        input_collection()
def addition():
    from numpy.polynomial import polynomial as P
    p1 = creating_tuple()
    p2 = creating_tuple()
    print("Polynomial 1...", p1)
    print("Polynomial 2...", p2)
    sumRes = P.polyadd(p1, p2);
    print("Result (Sum)...", sumRes)
    print("Do you want to continue (Y/N")
    choice=input()
    if((choice=="Y") |(choice=="y")):
        return addition()
    else:
        input_collection()
def input_collection():
    print("1. Add polynomial")
    print("2. Multiply polynomial")
    print("3. Exit")
    argument = int(input())
    return argument
if __name__ == "__main__":
    print(number_to_string(input_collection()))