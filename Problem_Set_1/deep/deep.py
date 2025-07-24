answer = input("What is the answer to the Great Question of life, the Universe, and Everything? ").strip(" ").lower()

match answer:
    case "42" | "Forty-Two" | "forty-two" | "Forty-two"| "forty-Two" | "Forty Two"| "Forty two" | "forty two" | "forty Two" :
        print("Yes")
    case _:
        print("No")