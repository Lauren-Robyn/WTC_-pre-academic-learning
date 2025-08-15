def main():
    answer = input("What is the answer to the Great Question of life, the Universe, and Everything? ").replace("-"," ").strip(" ").lower()

    if answer == "42" or answer == "Forty two":
        print("Yes")
    else:
        print("No")
main()