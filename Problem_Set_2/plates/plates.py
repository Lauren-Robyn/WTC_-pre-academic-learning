def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #check if the length of the string is between 2 and 7 characters long
    if not ( 2 <= len(s) <= 7):
        return False
    #check if the first two characters are letters from the alphabet
    if not s[:2].isalpha():
             return False
    #Check if the characters of the string is alphanumeric
    if not s.isalnum():
            return False
    #check if the first number is not 0, enumerate() returns the value and the index
    for i, char in enumerate(s):
        if char.isdigit():
             if char == "0":
                return False
        #ensure that all the characters from index i are digits
             if not s[i:].isdigit():
                return False
             break
    return True

main()
