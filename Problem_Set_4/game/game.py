import random 
while True: 
    try: 
        level = int(input("Level: ")) 
        if level > 0 :
            break 
    except ValueError:
        pass

        
        
rand = random.randrange(1, level) 
while True:
        try:
             
            guess = int(input("Guess: "))
            if guess < 1:
                 continue 
            
            if guess > rand: 
                print("Too large!") 
            elif guess < rand: 
                print("Too small!") 
            else:  
                print("Just right!") 
            break 
        except ValueError:  
             pass
    