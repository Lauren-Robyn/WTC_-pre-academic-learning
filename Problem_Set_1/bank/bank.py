def main():
    greeting = input("greetings: ").strip().lower()
    
    if greet_hello(greeting):
        print("$0")
    elif first_letter_h(greeting):
        print("$20")
    else:
        print("$100")

def greet_hello(greeting):
    # Check if the first word is "hello"
    return greeting.startswith("hello")

def first_letter_h(greeting):
    return greeting.startswith("h")

main()
