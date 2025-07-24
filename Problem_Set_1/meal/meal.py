def main(): 
#input_time variable holds the user input and supports 12-hour time formats, it also takes into consideration case-insensititvity.
    input_time = input("What's the time? ").split(".a.m",".p.m").lower()
    
#conditional statements will check if the user input times that have been convertedd in def convert(), falls within the specified time frames 
    if input_time >= 7.0 or input_time <= 8.0: 
        return "Breakfast"
    
    if input_time >= 12.0 or input_time <= 13.0:
            return "Lunch"
   
    if input_time >= 18.0 or input_time <= 19.0:
            return "Supper"

def convert(input_time):
#input time has been passed as an argument and will be seperated into hours and minutes variables and then converted to float
    hours,minutes = input_time.split(":")

    hours = hours.float()
    minutes = int(minutes.float())/60 

    time =f"{hours} + {minutes}"
    return time

if __name__ == "__main__":
    main()
