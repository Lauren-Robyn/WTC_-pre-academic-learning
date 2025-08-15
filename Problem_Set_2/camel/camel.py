#input variable will be passed as an argument to  a function
def  main():
    variable_name = input("Variable name: ")
    print("variable name is: ", change_case)

#function for finding the capital cases in the string 
def change_case(variable_name):
    snake_case ="" 
    for char in variable_name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

main()
