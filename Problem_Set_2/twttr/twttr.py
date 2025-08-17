def main():
    phrase = input("Input: ")
    print("Output: ", vowless(phrase))

def vowless(phrase):
    output = " "
    for c in phrase:
        if c.lower() not in ["a","e","i","o","u"]:
            output += c
    print(output)
main()