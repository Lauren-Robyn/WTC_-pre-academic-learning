def main():
#my application should allow user input in the form of 3 variables
    x, y, z = input("Expression: ").split(" ")
#float the x and y values
    x = float(x)
    z = float(z)
# use match case to determine the expression operator
    match y:
        case "+":
            result = x + z
        case "-":
            result = x - z
        case "*":
            result = x * z
        case "/":
            result = x / z
        case _:
            result = "invalid operator"

    print ("answer :", result)

main()