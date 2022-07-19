
def main():

    #________________________________________________________________________________________________________________________

    # ACT I - SCENARIO 1 - ENTRANCE

    #________________________________________________________________________________________________________________________

    from time import sleep
    import sys
    import random

    from gamefunc import title_screen, bank_entrance, game_over01

    score=2500

    print("\n_________________________________________________________________________________________________\n")
    print("\n_________________________________________________________________________________________________\n")

    title_screen()

    print("\n_________________________________________________________________________________________________\n")
    print("\n_________________________________________________________________________________________________\n")

    input("\nPress ENTER to start the game.\n")

    print("\n____________________________________________________________________________________\n")
    print("\n____________________________________________________________________________________\n")

    def printa(text):
        for c in text:          
            print(c, end='')    
            sys.stdout.flush()
            sleep(0.01) 

    def printb(text):
        for c in text:          
            print(c, end='')    
            sys.stdout.flush()
            sleep(0.05) 

    # game_over01, title_screen, bank_entrance, vault_door, game_complete

    attempts=0
    gold=0
    dial=0
    value=0
    guess=1
    guard=0

    bank_entrance()

    print("____________________________________________________________________________________\n")

    printb("\nThe political climate is bleak. Corruption is sky high.\n")
    printb("\nThe economy has tanked and the greedy bankers are hoarding all the money.\n")
    printb("\nIt is a dog eat dog world and chaos is the best ladder.\n")
    printb("\nAll the banks these days skimp on security. These fortress' leave a lot to be desired and more to be won!\n")
    printb("\nCracking this baby will be as easy as scrambling eggs.\n")
    printb("\nYou arrive at the imposing bank door.\n")
    printb("\nIt is locked up tight.\n")
    printb("\nUpon inspection, you notice the lock requires a three digit combination.\n")
    printb("\nTime is of the essence though, you don't want to get caught trying to break in.\n")
    printb("\nNow... time to put your deft hands to work.\n")

    print("\n________________________________________________________________________________\n")

    print("\nYou only have three attempts at each combination number. Each combination number is between 1-9.\n")
    print('\nThrough your years of experience, you have developed a kind of "sixth sense" when it comes to breaking locks.\n')
    print("\nYou should be able to feel whether you are hot or cold.")

    while dial <4:
        dial +=1
        attempts =0
        # This is to make up the safe number.
        random_safe_number=random.randint(1,9) 
        # Adding how close to safe number you are.
        boiling = random_safe_number-1
        boiling1 = random_safe_number+1
        hot = random_safe_number-2
        hot1 = random_safe_number+2 
        warm = random_safe_number-3
        warm1 = random_safe_number+3 
        cold = random_safe_number-4
        cold1 = random_safe_number+4
        # This is to make sure you only get 3 attempts.
        while attempts < (4):
            guard+=1
            attempts+=1
            print("\n________________________________________________________________________________\n")
            if attempts==1:
                print(f"\nFirst attempt on combination number {dial}.\n")
            elif attempts==2:
                print(f"\nSecond attempt on combination number {dial}.\n") 
            elif attempts==3:
                print(f"\nLast attempt on combination number {dial}.\n")
            
            if attempts<4:
                value=0
                while True:
                    try:
                        while value != 1 and value != 2 and value!= 3 and value != 4 and value!= 5 and value != 6 and value!= 7 and value != 8 and value!= 9:
                            value = int(input(F"Enter combination number {dial}.\n" ))
                            if value==0:
                                print("\nIt must be a number between 1 and 9.\n")
                    except ValueError:
                        print("\nTry again.\n")
                        continue
                    break
                # freeze is used if guess is over 4 away from safe number.
                
                freeze=1
                guess=value
                value=0
                # Checking if guess is correct.   
            if random_safe_number == guess:
                printb(f"\nYou feel the pin slide into place. Combination attempt successful.\n")
                #print("""""")
                attempts=4
                freeze =0
            # Checking if all 3 guesses are correct.    
            if dial ==3 and random_safe_number == guess:
                freeze =0 
                print("\n________________________________________________________________________________\n") 
                print("\nWith a final nudge of your pick, you feel the lock slide loose. You are now free to enter.")
                print("\n________________________________________________________________________________\n")
                
                # Resetting variables to finish game.          
                dial=4
                attempts =4
            # Checking how close guess is.
            
            if guard ==1 and guess != random_safe_number:
                print("\nWhere is the guard?\nThe guard is nowhere to be seen.\n") 
            if guard ==2 and guess != random_safe_number:
                print("\nWhere is the guard?\nPlenty of time left.\n")
            if guard == 3 and guess != random_safe_number:   
                print("\nWhere is the guard?\nDont be taking too long.\n")
            if guard == 4 and guess != random_safe_number:   
                print("\nWhere is the guard?\nThe guard will be here soon.\n")    
            if guard == 5 and guess != random_safe_number:   
                print("\nWhere is the guard?\nDont be making silly mistakes now.\n")
            if guard == 6 and guess != random_safe_number:   
                print("\nWhere is the guard?\nSweaty palm time.\n")    
            if guard == 7 and guess != random_safe_number:   
                print("\nWhere is the guard?\nOh no the guard is just around the corner.\n")
            if guard == 8 and guess != random_safe_number:   
                print("\nWhere is the guard?\nThe guard has seen you. You do a runner.\n")   
                print("\nI am afraid robbing banks is something your not very good at.\n")
                print("\nBack to your day job for you matey.\n")
                game_over01()
                start_again = input("Do you want to try again [Y/N]").lower()
                if start_again == "y":
                   main()
                else:
                  exit() 
                
                attempts =4
                dial=4
            if guess== boiling or guess == boiling1 and attempts<4 and guard<8: 
                freeze=0
                print("\nRed hot!\n")
            elif  guess == hot or guess== hot1 and guard<8:
                freeze =0
                print("\nHot!\n") 
            elif guess== warm or guess ==warm1 and attempts<4 and guard<8:
                freeze =0
                print("\nWarm.\n")
            elif guess== cold or guess ==cold1 and attempts<4 and guard<8:
                freeze =0
                print("\nCold.\n")
            else:
                if freeze ==1 and guard<8 :
                    print("\nIce cold.\n")
                    freeze =0
            # Checking if you have lost
            if attempts ==3 and guess != random_safe_number:
                print("\nYou have set off the Alarm.\n")
                game_over01()
                restart = input("\nDo you want to try again [Y/N]\n").lower()
                if restart == "y":
                   main()
                else: 
                    dial=4
                    freeze=0
                    guess=10
                    guard=10
                    exit()


    #________________________________________________________________________________________________________________________


    # ACT I - SCENARIO 2 - STEALTH

    #________________________________________________________________________________________________________________________

    from time import sleep
    import sys

    from gamefunc import game_over01

    # game_over01, title_screen, bank_entrance, vault_door, game_complete


    def printb(text):
        for c in text:          
            print(c, end='')    
            sys.stdout.flush()  
            sleep(0.05)   

    printb("\nYou have entered the bank, arriving in a dimly lit main hall.\n")
    printb("\nYou hear footsteps approaching from a corridor further on.\n")
    printb("\nIt sounds like it could be a guard patrol heading your way, if you don't make a move, you will be spotted.\n")
    printb("\nWhat will you do?")

    print("\n________________________________________________________________________________\n")

    printb("\nSelect a place to hide while the patrol passes by.\n")

    answer01=input("\n1. Hide in small alcove near the door.\n" "\n2. Hide behind greeting counter.\n" "\n3. Close your eyes, if you can't see him, he can't see you, right?\n")
    while answer01 !="1" and answer01 != "2" and answer01 != "3":
        printb("\nNo time to dawdle. You must do something!\n"); 
        answer01=input("\n1. Hide in small alcove near the door.\n" "\n2. Hide behind greeting counter.\n" "\n3. Close your eyes, if you can't see him, he can't see you, right?\n")
    if answer01 =="1":
        
        printb("\nYou hide within the small alcove near the entrance, however, by chance, the guard shines their flashlight your way, and you are discovered.\n") 
        game_over01()
        start_again = input("Do you want to try again [Y/N]").lower()
        if start_again == "y":
            main()
        else:
            exit()     
    elif answer01 =="2": 
        printb("\nYou hide behind the greeting counter, it is large enough to shield you from the guard's flashlight. You avoid detection.\n")
    elif answer01 =="3":
        printb("\nYou close your eyes, and hope the guard will not see you. However, the guard notices you right away, puzzled as to why you are just standing there in the middle of the hall with your eyes close. You have been detected.\n")
        game_over01()
        start_again = input("Do you want to try again [Y/N]").lower()
        if start_again == "y":
            main()
        else:
            exit()


    #________________________________________________________________________________________________________________________

    # ACT I - SCENARIO 3 - HALLWAYS 1

    #________________________________________________________________________________________________________________________  


    from time import sleep
    import sys

    print("\n________________________________________________________________________________\n")

    printb("You head towards the vault, but you are faced with a hallway, splitting off into three directions. Which direction do you choose?\n")


    print("\n________________________________________________________________________________\n")


    input01 = input("\n1. Left hallway.\n" "\n2. Onward hallway.\n" "\n3. Right hallway.\n")
    while input01 !="1" and input01 != "2" and input01 != "3":
        print("\nNo time to dawdle. You must do something!\n")
        input01 = input("\n1. Left hallway.\n" "\n2. Onward hallway.\n" "\n3. Right hallway.\n")

    print("\n________________________________________________________________________________\n")

    if input01 == "2" or input01 == "3":
        printb("\nYou arrive at the vault. Now to truly put your lockbreaking skills to the test!\n")   
    elif input01 == "1":
        printb("\nYou cautiously peak around the corner, but you are met with the formidable glare from a guard, standing mere feet away. It's no use now, you have been detected.\n")
        game_over01()
        start_again = input("\nDo you want to try again [Y/N]\n").lower()
        if start_again == "y":
            main()
        else:
            exit()
    print("\n_________________________________________________________________________________\n")

    #________________________________________________________________________________________________________________________  

    # ACT II - SCENARIO 1 - SAFECRACKING

    #________________________________________________________________________________________________________________________ 

    from time import sleep
    import sys
    import random
    from gamefunc import title_screen, bank_entrance, game_over01, vault_door


    vault_door()

    print("_________________________________________________________________________________\n")

    # >>>>>>>>>>>>>> score=2500 
    # >>>>>>>>>>>>>> score-=200 (per false attempt.)

    def printb(text):
        for c in text:          
            print(c, end='')    
            sys.stdout.flush()  
            sleep(0.05) 

    attempt=0
    gold=0
    dial=0
    value=0
    guess=0

    #****** Vault door game ******
    # Giving instruction and setting variables.    
    printb("You finally reach the vault.\n")
    printb("\nThe vault appears to have three dials that are used to unlock it.\n")
    printb("\nThey are all numbered between 1 and 9.\n")
    # printb("You can have up to 4 attempts at cracking each dial.")
    # printb("You will be given a clue after each attempt.\n")
    printb("\nYou lean in closer, and prepare to make your attempt.\n")
    printb("\nRemember, time is money, the longer you take, the less time you will have to gather the gold once inside.\n")
    printb("\nEvery mistake will cost you gold.\n")
    printb("\nHere it goes...\n")

    # This is to check which dial is going to be used.
    while dial <4:
        dial +=1
        # This is to make up the safe number.
        random_safe_number=random.randint(1,9) 
        attempt =0
        # This is to make sure you only get 4 attempts.
        while attempt < (5):
            print("\n________________________________________________________________________________\n")
            attempt+=1
            score-=50
            if attempt ==1:
                printb("\nFirst attempt.\n")
            elif attempt ==2:
                printb("\nSecond attempt.\n") 
            elif attempt ==3:
                printb("\nThird attempt.\n")
            elif attempt ==4:
                printb("\nLast attempt.\n")
            # Having a guess at the safe number.
            if attempt <5:
                while value != 1 and value != 2 and value != 3 and value != 4 and value != 5 and value != 6 and value != 7 and value != 8 and value != 9:
                    try:
                        while value != 1 and value != 2 and value != 3 and value != 4 and value != 5 and value != 6 and value != 7 and value != 8 and value != 9:
                            value = int(input(F"\nWhat is the number for dial {dial}?\n" ))
                            if value ==0:
                                printb("\nPlease pick a number between 1 and 9.\n")
                    except ValueError:
                        printb("\nTry again.\n")
                        continue
                    break
            guess=value
            value=0
            # Checking if guess is correct.     
            if random_safe_number == guess:
                printb("\nYou hear a distinct snap as you turn the dial.\n")
                attempt=5
                
                
                # if gold>0 and dial <3:
                #     print(f"You now have earnt £{gold},000 so far.\n")
                if random_safe_number == guess and dial <3:
                  printb(f"\nNow onto dial number {dial+1}.\n") 
            # Checking if all 3 guesses on dials are correct.    
            if dial ==3 and random_safe_number == guess:
                print("\nYou hear the final snap ring out as the mechanism releases, the vault is now open!")
                hard = False
                attempt =5
                dial=4
                
            # Showing if guess is too high or low. 
            if guess< random_safe_number and attempt<5:
                printb(f"\nYour guess of {guess} was too low.\n")
                 
            if guess>random_safe_number and attempt<5:
                printb(f"\nYour guess of {guess} was too high.\n")
                
            # Checking if you have lost.
            if attempt ==4 and guess != random_safe_number:
                printb("\nYou have set off the alarm.\n")
                attempt =5
                dial=4    
                game_over01()
                start_again = input("\nDo you want to try again [Y/N]\n").lower()
                if start_again == "y":
                    main()
                else:
                    exit()
                  

    print("\n________________________________________________________________________________\n")


    #________________________________________________________________________________________________________________________

    # ACT II - SCENARIO 2 - INSIDE VAULT

    #________________________________________________________________________________________________________________________

    from time import sleep
    import sys
    import random
    from gamefunc import title_screen, bank_entrance, game_over01

    def printb(text):
        for c in text:          
            print(c, end='')    
            sys.stdout.flush()  
            sleep(0.05) 

    printb("\nAll doors swing, even those reinforced with steel and titanium. Push on in and discover what awaits you.\n")
    printb("\nAs shiny as gold is, and it is so very shiny, it is also very heavy.\n")
    printb("\nHow much gold can you safely carry out of the vault with you? Or will your eyes prove to be bigger than your belly?\n")

    printb("\nHow much gold will you take?\n")

    answer01=input("""\n1. "Some" gold.\n""" """\n2. "A lot" of gold.\n""")
    while answer01 !="1" and answer01 != "2":
        printb("\nSo shiny!\n"); 
        answer01=input("""\n1. "Some" gold.\n""" """\n2. "A lot" of gold.\n""")
    if answer01 =="1":
        score-=1500    
        printb("\nYou fill your sack with a modest amount of gold. It is of a satisfying weight, but not heavy enough to impede your movement.\n") 
    elif answer01 =="2": 
        printb("\nYou fill your sack with as much gold as you can fit. You struggle to heave your sack over your shoulder, but with this much, you will be set for life!\n")
    #                                                                                                                            NEEDS REWORDING!!!


    #________________________________________________________________________________________________________________________

    # ACT III - SCENARIO 1 - HALLWAYS 2

    #________________________________________________________________________________________________________________________



    import sys
    from time import sleep
    from gamefunc import title_screen, bank_entrance, game_over01, game_complete

    def printb(text):
        for c in text:          # for each character in the text
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.05)         # wait a little to make the effect look good.

    printb("\nTime to make your escape. You must retrace your steps, and head out the way you came.\n")
    printb("\nYou are is faced with a hallway, splitting off into two directions.\n")

    print("\n________________________________________________________________________________\n")


    final_hallway = input("\n1. Left hallway.\n""\n2. Onward hallway.\n")

    while final_hallway !="1" and final_hallway != "2":
        print("\nNo time blah blah blah.\n")

        final_hallway = input("\n1. Left hallway.\n2. Onward hallway.\n")
    if final_hallway == "1" or final_hallway == "2":
        printb("\nYou are spotted by a patrol, but they are far enough away, that you might have a chance to escape if you run now.\n")

    #________________________________________________________________________________________________________________________

    # ACT IiI - SCENARIO 2 - ESCAPE

    #________________________________________________________________________________________________________________________

    # print(f"score = {score}")

    printb("\nWhat will you do?\n")
    print("\n________________________________________________________________________________\n")
    final_decision = input("\n1. Drop all gold, and attempt to flee.\n" "\n2. Try to escape with the gold.\n" "\n3. Throw a bar of gold at your pursuer.\n")

    while final_decision != "1" and final_decision != "2" and final_decision != "3":
        print("\nNo time to blah blah blah.\n")
        printb("\nYou are spotted by a patrol, but they are far enough away, that you might have a chance to escape if you run now.\n")
        printb("\nWhat will you do?\n")
        print("\n________________________________________________________________________________\n")
        final_decision = input("\n1. Drop all gold, and attempt to flee.\n" "\n2. Try to escape with the gold.\n" "\n3. Throw a bar of gold at your pursuer.\n")

    if 1010 <= score <= 2500 and final_decision == "1":
        printb("\nYou escaped, but have nothing to show for it. What a terrible thief you are.\n")
        game_over01()
        start_again = input("\nDo you want to try again [Y/N]\n").lower()
        if start_again == "y":
            main()
        else:
            exit()
    elif 1010 <= score <= 2500 and final_decision == "2":
        printb("\nYou try to run, but your burdensome haul weighs you down. You are not fast enough to escape the guard.\n")
        game_over01()
        start_again = input("\nDo you want to try again [Y/N]\n").lower()
        if start_again == "y":
            main()
        else:
            exit()
    elif 1010 <= score <= 2500 and final_decision == "3":
        printb("\nYour shiny projectile hits your pursuer square in the head, knocking them out, allowing you to escape unobstructed.\n")
        score -= 200
        printb("\nHeist successful!\n" f"\nYour score is {score}!\n")
        game_complete()
        restart = input("\nDo you want to try again [Y/N]\n").lower()
        if restart == "y":
            main()
        else:
            exit() 

    if 69 <= score <= 1000 and final_decision == "1":
        printb("\nYou escaped, but have nothing to show for it. What a terrible thief you are.\n")
        game_over01()
        start_again = input("\nDo you want to try again [Y/N]\n").lower()
        if start_again == "y":
            main()
        else:
            exit()
        
    elif 69 <= score <= 1000 and final_decision == "2":
        printb("\nYour lack of greed has payed off. You are light enough on your feet to escape the guard.\n")
        printb("\nHeist successful!\n" f"\nYour score is {score}!\n")
        game_complete()
        start_again = input("\nDo you want to try again [Y/N]\n").lower()
        if start_again == "y":
            main()
        else:
            exit()

    elif 69 <= score <= 1000 and final_decision == "3":
        printb("\nYour shiny projectile hits your pursuer square in the head, knocking them out, allowing you to escape unobstructed.\n")
        score -= 200
        printb("\nHeist successful!\n" f"\nYour score is {score}!\n")
        game_complete()
        start_again = input("\nDo you want to try again [Y/N]\n").lower()
        if start_again == "y":
            main()
        else:
            exit()
main()

    #________________________________________________________________________________________________________________________

    # GAME COMPLETE

    #________________________________________________________________________________________________________________________