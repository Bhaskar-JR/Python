#P4.25 The Monty Hall Paradox. Marilyn vos Savant described the following problem
#(loosely based on a game show hosted by Monty Hall) in a popular magazine: “Suppose
#you’re on a game show, and you’re given the choice of three doors: Behind one
#door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who
#knows what’s behind the doors, opens another door, say No. 3, which has a goat. He
#then says to you, ‘Do you want to pick door No. 2?’ Is it to your advantage to switch?”
#Ms. vos Savant proved that it is to your advantage, but many of her readers, including
#some mathematics professors, disagreed, arguing that the probability would not
#change because another door was opened.

#Your task is to simulate this game show. In each iteration, randomly pick a door number
#between 1 and 3 for placing the car. Randomly have the player pick a door. Randomly have
#the game show host pick a door having a goat (but not the door that the player picked). 
#Increment a counter for strategy 1 if the player wins by switching to the third door, and 
#increment a counter for strategy 2 if the player wins by sticking with the original choice.
#Run 1,000 iterations and print both counters.

#press <Ctrl+"/"> for commenting block of code in Jupyter notebook

#Solution

#Creating a function to run a monte carlo simulation 
#Taking user input for the number of simulations

def monte_carlo():
    n = int(input("Enter the no. of iterations:"))
    
    #Taking user input(Y/N) if the user wants to see results of each simulation row-wise 
    #https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers?rq=1
    while True:
        try:
            table = input("Do you want to see row-wise results (Y/N):")

            if table.lower() not in ["y","n"]:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
            print("Invalid entry. Please enter either of Y/N.")
    
    #calling a function defined below to run the actual simulation
    monte_carlo_hood(n,table)

#defining a function taking two inputs - simulation count and display requirement
def monte_carlo_hood(n,table): 
    Strategy_1 =[]
    Strategy_2 = []

    #Formatting the header row in case the user wants the display of the simulation
    if table.lower() =="y":
        print('{0:>5}{1:>20}{2:>20}{3:>10}{4:>25}{5:>10}'.format("car","first_choice", "Strategy_1(Switch)",
                                                                 "Outcome","Strategy_2(NoSwitch)","Outcome"))
    else:
        pass
    
    #The Actual logic : for every initial choice of the participant, the host reveals a door without the car
    #Step 1: Three doors corresponding to three integers - 0,1,2
    #Step 2: The Car door is randomly initialised from (0,1,2)
    #Step 3: The First choice is randomly initialised from range(0,1,2) 
    #Step 4: The host reveals the door excluding the doors (Car,First choice)
    
    #Strategy 1: The participant switches the door. i.e he chooses the door excluding (First choice,Host Reveal)
    #Strategy 2: The participant retains his initial choice 
    #The participant wins if his final choice matches the car door
    
    for i in range(n+1):
        car = random.randint(0,2)
        #goat = random.choice([x for x in range(0,3) if x != car])
        first_choice = random.randint(0,2)
        host_reveal = random.choice([x for x in range(0,3) if x not in (car,first_choice)]) 
        remaining_door = random.choice([x for x in range(0,3) if x not in (host_reveal,first_choice)]) 
    
    #Strategy 1: Switching
        final_1 = remaining_door
        if final_1 == car:
            Strategy_1.append("Win")
        else:
            Strategy_1.append("Loss")
        
    #Strategy 2: Not Switching
        final_2 = first_choice
        if final_2 == car:
            Strategy_2.append("Win")
        else:
            Strategy_2.append("Loss")
        if table == "Y":
            print(f"{car:>5d}{first_choice:>20d}",end="")
            print(f"{final_1:>20d}{Strategy_1[i]:>10s}{final_2:>25d}{Strategy_2[i]:>10s} ")
            #print(f"Final Door : Strategy_2 = {final_2} and Outcome = {Strategy_2[i]}", end = " ")
        else:
            pass
    print("")    
    
    #for i in list(zip(Strategy_1,Strategy_2)):
    #    print(i)
    
    #Win Ratio in Strategy-1(Switching) and Strategy-2(No Switching) 
    x1 = Strategy_1.count("Win")
    y1 = len(Strategy_1)
    Win_Ratio_1 = x1/y1
    print(f"Win% in strategy 1: {Win_Ratio_1:.2f}")

    x2 = Strategy_2.count("Win")
    y2 = len(Strategy_2)
    Win_Ratio_2 = x2/y2
    print(f"Win% in strategy 2: {Win_Ratio_2:.2f}")
    


#Output of the above code (Please copy the above code for execution in IDE)
>>> monte_carlo()    
    Enter the no. of iterations:10
Do you want to see row-wise results (Y/N):y
  car        first_choice  Strategy_1(Switch)   Outcome     Strategy_2(NoSwitch)   Outcome
    2                   2                   0      Loss                        2       Win 
    2                   0                   2       Win                        0      Loss 
    0                   2                   0       Win                        2      Loss 
    0                   2                   0       Win                        2      Loss 
    0                   2                   0       Win                        2      Loss 
    1                   0                   1       Win                        0      Loss 
    0                   1                   0       Win                        1      Loss 
    0                   1                   0       Win                        1      Loss 
    0                   2                   0       Win                        2      Loss 
    2                   1                   2       Win                        1      Loss 
    1                   2                   1       Win                        2      Loss 

Win% in strategy 1: 0.91
Win% in strategy 2: 0.09
    
    
    
    
