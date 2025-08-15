def main(): 
    input_time = input("What is the time ? ").lower().strip("a.m").strip("p.m")

    time = convert(input_time)

    if 7 <= time <= 8:
        print ("breakfast time")
    elif 12 <= time <=13: 
        print("lunch time")
    elif 18<= time <= 19:
        print("dinner time")

def convert(input_time):
     #split the user input at the ":" and place the values into two different variables. 
     hours, minutes = input_time.split(":")
    #convert hours and minutes to float
     time = float(hours) + float(minutes)/60
     return time
if __name__ == "__main__":
    main() 

    