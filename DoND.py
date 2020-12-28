# Deal or No Deal?
import random
import time
from datetime import datetime
import pickle

current_time = datetime.now()
today_date = current_time.strftime('%m/%d/%Y')
myScore = 0

defaultData = [25_000, "CPU", "12/25/2020"]
default_out = open("DefaultScore.pkl", "wb")
pickle.dump(defaultData, default_out)
default_out.close()
scoreData = [24_999, 0, 0]
# pickle_out = open("HighScore.pkl", "wb")
# pickle.dump(scoreData, pickle_out)
# pickle_out.close()

amounts = [.01,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]
cases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def menu():
    print(color.BOLD + "\nWelcome to Deal or No Deal!" + color.END)
    print("To navigate the menu, type the number of one of the options below and press ENTER.\n")
    print("(1) Play")
    print("(2) Instructions")
    print("(3) High Score")
    print("(4) Exit\n")
    
    while True:
        try:
            menu_select = input("Select an option: ")
            if menu_select.strip() == "":
                raise ValueError("No selection was made.\n")
            elif menu_select.isdecimal() == False:
                raise ValueError("Only numbers are allowed for menu selections.\n")
            elif int(menu_select) > 4 or int(menu_select) < 1:
                raise ValueError("That option does not exist.\n")
            else:
                if int(menu_select) == 1:
                    play()
                elif int(menu_select) == 2:
                    instructions()
                elif int(menu_select) == 3:
                    leaderboard()
                elif int(menu_select) == 4:
                    print("\nThanks for playing Deal or No Deal.\nCreated by Brandon Koch\n")
                    break
            return
        except ValueError as e:
            print(e)
            time.sleep(1)
    return

def instructions():
    print("\n" + color.UNDERLINE + color.BOLD + "Deal or No Deal Instructions" + color.END)
    print("In Deal or No Deal, there are 26 briefcases containing dollar amounts that range from")
    print("$0.01 to $1,000,000. To begin the game, you will select one of the cases to keep with you.")
    print("Each round you will eliminate a certain amount of the remaining cases. When a case is removed,")
    print("you can no longer win the dollar amount in that case. Once the round ends, the banker will")
    print("make you an offer based on the average of the dollar amounts in the remaining cases. You can accept")
    print("the banker's offer and end the game, or continue to play in hopes of a larger reward. In the final")
    print("round, you will decide between keeping your original case or switching to the other case that remains.")
    print("Do you have what it takes to bring home $1,000,000? Find out today by playing Deal or No Deal!\n")

    input("Press ENTER to return to the menu. ")
    menu()

def play():
    amounts = [.01,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]
    cases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    global myScore
    random.shuffle(amounts)
    print(color.BOLD + "\nIt's time to play Deal or No Deal!" + color.END)

    while True:
        try:
            myCase = (input("Select a case number between 1 and 26: "))
            if myCase.strip() == "":
                raise ValueError("No case was selected.\n")
            elif myCase.isdecimal() == False:
                raise ValueError("Only numbers are allowed for case selections.\n")
            elif int(myCase) not in cases:
                raise ValueError("That case does not exist.\n")
            else:
                print(f"You selected case {myCase}.")
                cases.remove(int(myCase))
                break  
        except ValueError as e:
            print(e)
            time.sleep(1)

    time.sleep(1)
    print("\nIn the first round, you will select 6 of the remaining cases to eliminate.")
    print("After you have selected 6 cases to eliminate, the banker will make you an offer.\n")
    time.sleep(2)

    R1_Cases_Left = 6
    while True:
        try:
            if R1_Cases_Left < 6 and R1_Cases_Left > 1:
                print(f"There are {R1_Cases_Left} more cases to eliminate this round.")
            elif R1_Cases_Left == 1:
                print(f"There is 1 more case to eliminate this round.")
            R1_Elim = input("Select a case to eliminate: ")
            if R1_Elim.strip() == "":
                raise ValueError("No case was selected.\n")
            elif R1_Elim.isdecimal() == False:
                raise ValueError("Only numbers are allowed for case selections.\n")
            elif int(R1_Elim) not in cases:
                if int(R1_Elim) < 1 or int(R1_Elim) > 26:
                    raise ValueError("That case does not exist.\n")
                else:   
                    raise ValueError("That is not one of the remaining cases.\n")
            else:
                print(f"You eliminated case {R1_Elim}.\n")
                R1_E = int(R1_Elim)
                cases.remove(R1_E)
                R1_Cases_Left -= 1
                time.sleep(1)
                if amounts[R1_E - 1] < 999:
                    print(f"Case {R1_E} was worth " + color.GREEN + f"${amounts[R1_E - 1]:,}" + color.END + ".\n")
                elif amounts[R1_E - 1] > 999 and amounts[R1_E - 1] < 33333:
                    print(f"Case {R1_E} was worth ${amounts[R1_E - 1]:,}.\n")
                else:
                    print(f"Case {R1_E} was worth " + color.RED + f"${amounts[R1_E - 1]:,}" + color.END + ".\n")
                time.sleep(2)
                amounts[R1_E - 1] = 0
                if R1_Cases_Left == 0:
                    break
        except ValueError as e:
            print(e)
            time.sleep(1)
    
    print("This is the end of round 1.")
    time.sleep(1)
    print("The banker did some calculations and is ready to make an offer.\n")
    time.sleep(2)
    input("Press ENTER to see the banker's offer. ")
    R1_Offer = round((sum(amounts) / 20) * 0.3)
    print("\nThe banker is willing to offer you " + color.BOLD + f"${R1_Offer:,}" + color.END + ".")
    time.sleep(2)
    print("\nYou can accept this offer and walk away with the money,")
    print("or you can reject the offer and keep playing.")
    time.sleep(2)
    print("\nType 'D' for Deal, or 'N' for No Deal.")
    time.sleep(1)
    R1_DoND = input("Deal or No Deal? ")

    while True:
        if R1_DoND == "D" or R1_DoND == "d":
            print(color.BOLD + f"\nCongratulations, you won ${R1_Offer:,}!" + color.END)
            time.sleep(2)
            print("\nWould you like to find out the value of your case?")
            R1_View = input("Type 'Y' for Yes, or 'N' for No: ")
            while True:
                if R1_View == "Y" or R1_View == "y":
                    print("\nYour case was worth " + color.BOLD + f"${amounts[int(myCase) - 1]:,}." + color.END)
                    time.sleep(2)
                    break
                elif R1_View == "N" or R1_View == "n":
                    break
                else:
                    print("\nThat is not a valid selection.\n")
                    time.sleep(1)
                    print("Would you like to find out the value of your case?")
                    R1_View = input("Type 'Y' for Yes, or 'N' for No: ")
            break
        elif R1_DoND == "N" or R1_DoND == "n":
            print("\nYou chose to decline the banker's offer.")
            time.sleep(1)
            break
        else:
            print("\nThat is not a valid selection.\n")
            time.sleep(1)
            print("Type 'D' for Deal, or 'N' for No Deal.")
            time.sleep(1)
            R1_DoND = input("Deal or No Deal? ")
    if R1_DoND == "D" or R1_DoND == "d":
        myScore = R1_Offer
        if myScore > scoreData[0]:
            newHigh()
        else:
            print("\nThanks for playing Deal or No Deal.\nCreated by Brandon Koch\n")
            time.sleep(2)
            input("Press ENTER to return to the menu. ")
            menu()
    else:
        time.sleep(1)
        print("\nIn the second round, you will select 5 of the remaining cases to eliminate.")
        print("After you have selected 5 cases to eliminate, the banker will make you an offer.\n")
        time.sleep(2)

        R2_Cases_Left = 5
        while True:
            try:
                if R2_Cases_Left < 5 and R2_Cases_Left > 1:
                    print(f"There are {R2_Cases_Left} more cases to eliminate this round.")
                elif R2_Cases_Left == 1:
                    print(f"There is 1 more case to eliminate this round.")
                print("Cases remaining: ", end="")
                print(*cases, sep=", ")
                R2_Elim = input("Select a case to eliminate: ")
                if R2_Elim.strip() == "":
                    raise ValueError("No case was selected.\n")
                elif R2_Elim.isdecimal() == False:
                    raise ValueError("Only numbers are allowed for case selections.\n")
                elif int(R2_Elim) not in cases:
                    if int(R2_Elim) < 1 or int(R2_Elim) > 26:
                        raise ValueError("That case does not exist.\n")
                    else:   
                        raise ValueError("That is not one of the remaining cases.\n")
                else:
                    print(f"You eliminated case {R2_Elim}.\n")
                    R2_E = int(R2_Elim)
                    cases.remove(R2_E)
                    R2_Cases_Left -= 1
                    time.sleep(1)
                    if amounts[R2_E - 1] < 999:
                        print(f"Case {R2_E} was worth " + color.GREEN + f"${amounts[R2_E - 1]:,}" + color.END + ".\n")
                    elif amounts[R2_E - 1] > 999 and amounts[R2_E - 1] < 33333:
                        print(f"Case {R2_E} was worth ${amounts[R2_E - 1]:,}.\n")
                    else:
                        print(f"Case {R2_E} was worth " + color.RED + f"${amounts[R2_E - 1]:,}" + color.END + ".\n")
                    time.sleep(2)
                    amounts[R2_E - 1] = 0
                    if R2_Cases_Left == 0:
                        break
            except ValueError as e:
                print(e)
                time.sleep(1)

        print("This is the end of round 2.")
        time.sleep(1)
        print("The banker did some calculations and is ready to make an offer.\n")
        time.sleep(2)
        input("Press ENTER to see the banker's offer. ")
        R2_Offer = round((sum(amounts) / 15) * 0.5)
        print("\nThe banker is willing to offer you " + color.BOLD + f"${R2_Offer:,}" + color.END + ".")
        time.sleep(2)
        print("\nYou can accept this offer and walk away with the money,")
        print("or you can reject the offer and keep playing.")
        time.sleep(2)
        print("\nType 'D' for Deal, or 'N' for No Deal.")
        time.sleep(1)
        R2_DoND = input("Deal or No Deal? ")

        while True:
            if R2_DoND == "D" or R2_DoND == "d":
                print(color.BOLD + f"\nCongratulations, you won ${R2_Offer:,}!" + color.END)
                time.sleep(2)
                print("\nWould you like to find out the value of your case?")
                R2_View = input("Type 'Y' for Yes, or 'N' for No: ")
                while True:
                    if R2_View == "Y" or R2_View == "y":
                        print("\nYour case was worth " + color.BOLD + f"${amounts[int(myCase) - 1]:,}." + color.END)
                        time.sleep(2)
                        break
                    elif R2_View == "N" or R2_View == "n":
                        break
                    else:
                        print("\nThat is not a valid selection.\n")
                        time.sleep(1)
                        print("Would you like to find out the value of your case?")
                        R2_View = input("Type 'Y' for Yes, or 'N' for No: ")
                break
            elif R2_DoND == "N" or R2_DoND == "n":
                print("\nYou chose to decline the banker's offer.")
                time.sleep(1)
                break
            else:
                print("\nThat is not a valid selection.\n")
                time.sleep(1)
                print("Type 'D' for Deal, or 'N' for No Deal.")
                time.sleep(1)
                R2_DoND = input("Deal or No Deal? ")
        if R2_DoND == "D" or R2_DoND == "d":
            myScore = R2_Offer
            if myScore > scoreData[0]:
                newHigh()
            else:
                print("\nThanks for playing Deal or No Deal.\nCreated by Brandon Koch\n")
                time.sleep(2)
                input("Press ENTER to return to the menu. ")
                menu()
        else:
            time.sleep(1)
            print("\nIn the third round, you will select 4 of the remaining cases to eliminate.")
            print("After you have selected 4 cases to eliminate, the banker will make you an offer.\n")
            time.sleep(2)

            R3_Cases_Left = 4
            while True:
                try:
                    if R3_Cases_Left < 4 and R3_Cases_Left > 1:
                        print(f"There are {R3_Cases_Left} more cases to eliminate this round.")
                    elif R3_Cases_Left == 1:
                        print(f"There is 1 more case to eliminate this round.")
                    print("Cases remaining: ", end="")
                    print(*cases, sep=", ")
                    R3_Elim = input("Select a case to eliminate: ")
                    if R3_Elim.strip() == "":
                        raise ValueError("No case was selected.\n")
                    elif R3_Elim.isdecimal() == False:
                        raise ValueError("Only numbers are allowed for case selections.\n")
                    elif int(R3_Elim) not in cases:
                        if int(R3_Elim) < 1 or int(R3_Elim) > 26:
                            raise ValueError("That case does not exist.\n")
                        else:   
                            raise ValueError("That is not one of the remaining cases.\n")
                    else:
                        print(f"You eliminated case {R3_Elim}.\n")
                        R3_E = int(R3_Elim)
                        cases.remove(R3_E)
                        R3_Cases_Left -= 1
                        time.sleep(1)
                        if amounts[R3_E - 1] < 999:
                            print(f"Case {R3_E} was worth " + color.GREEN + f"${amounts[R3_E - 1]:,}" + color.END + ".\n")
                        elif amounts[R3_E - 1] > 999 and amounts[R3_E - 1] < 33333:
                            print(f"Case {R3_E} was worth ${amounts[R3_E - 1]:,}.\n")
                        else:
                            print(f"Case {R3_E} was worth " + color.RED + f"${amounts[R3_E - 1]:,}" + color.END + ".\n")
                        time.sleep(2)
                        amounts[R3_E - 1] = 0
                        if R3_Cases_Left == 0:
                            break
                except ValueError as e:
                    print(e)
                    time.sleep(1)
            
            print("This is the end of round 3.")
            time.sleep(1)
            print("The banker did some calculations and is ready to make an offer.\n")
            time.sleep(2)
            input("Press ENTER to see the banker's offer. ")
            R3_Offer = round((sum(amounts) / 11) * 0.6)
            print("\nThe banker is willing to offer you " + color.BOLD + f"${R3_Offer:,}" + color.END + ".")
            time.sleep(2)
            print("\nYou can accept this offer and walk away with the money,")
            print("or you can reject the offer and keep playing.")
            time.sleep(2)
            print("\nType 'D' for Deal, or 'N' for No Deal.")
            time.sleep(1)
            R3_DoND = input("Deal or No Deal? ")

            while True:
                if R3_DoND == "D" or R3_DoND == "d":
                    print(color.BOLD + f"\nCongratulations, you won ${R3_Offer:,}!" + color.END)
                    time.sleep(2)
                    print("\nWould you like to find out the value of your case?")
                    R3_View = input("Type 'Y' for Yes, or 'N' for No: ")
                    while True:
                        if R3_View == "Y" or R3_View == "y":
                            print("\nYour case was worth " + color.BOLD + f"${amounts[int(myCase) - 1]:,}." + color.END)
                            time.sleep(2)
                            break
                        elif R3_View == "N" or R3_View == "n":
                            break
                        else:
                            print("\nThat is not a valid selection.\n")
                            time.sleep(1)
                            print("Would you like to find out the value of your case?")
                            R3_View = input("Type 'Y' for Yes, or 'N' for No: ")
                    break
                elif R3_DoND == "N" or R3_DoND == "n":
                    print("\nYou chose to decline the banker's offer.")
                    time.sleep(1)
                    break
                else:
                    print("\nThat is not a valid selection.\n")
                    time.sleep(1)
                    print("Type 'D' for Deal, or 'N' for No Deal.")
                    time.sleep(1)
                    R3_DoND = input("Deal or No Deal? ")
            if R3_DoND == "D" or R3_DoND == "d":
                myScore = R3_Offer
                if myScore > scoreData[0]:
                    newHigh()
                else:
                    print("\nThanks for playing Deal or No Deal.\nCreated by Brandon Koch\n")
                    time.sleep(2)
                    input("Press ENTER to return to the menu. ")
                    menu()
            else:
                time.sleep(1)
                print("\nIn the 4th round, you will select 3 of the remaining cases to eliminate.")
                print("After you have selected 3 cases to eliminate, the banker will make you an offer.\n")
                time.sleep(2)

                R4_Cases_Left = 3
                while True:
                    try:
                        if R4_Cases_Left < 3 and R4_Cases_Left > 1:
                            print(f"There are {R4_Cases_Left} more cases to eliminate this round.")
                        elif R4_Cases_Left == 1:
                            print(f"There is 1 more case to eliminate this round.")
                        print("Cases remaining: ", end="")
                        print(*cases, sep=", ")
                        R4_Elim = input("Select a case to eliminate: ")
                        if R4_Elim.strip() == "":
                            raise ValueError("No case was selected.\n")
                        elif R4_Elim.isdecimal() == False:
                            raise ValueError("Only numbers are allowed for case selections.\n")
                        elif int(R4_Elim) not in cases:
                            if int(R4_Elim) < 1 or int(R4_Elim) > 26:
                                raise ValueError("That case does not exist.\n")
                            else:   
                                raise ValueError("That is not one of the remaining cases.\n")
                        else:
                            print(f"You eliminated case {R4_Elim}.\n")
                            R4_E = int(R4_Elim)
                            cases.remove(R4_E)
                            R4_Cases_Left -= 1
                            time.sleep(1)
                            if amounts[R4_E - 1] < 999:
                                print(f"Case {R4_E} was worth " + color.GREEN + f"${amounts[R4_E - 1]:,}" + color.END + ".\n")
                            elif amounts[R4_E - 1] > 999 and amounts[R4_E - 1] < 33333:
                                print(f"Case {R4_E} was worth ${amounts[R4_E - 1]:,}.\n")
                            else:
                                print(f"Case {R4_E} was worth " + color.RED + f"${amounts[R4_E - 1]:,}" + color.END + ".\n")
                            time.sleep(2)
                            amounts[R4_E - 1] = 0
                            if R4_Cases_Left == 0:
                                break
                    except ValueError as e:
                        print(e)
                        time.sleep(1)
                
                print("This is the end of round 4.")
                time.sleep(1)
                print("The banker did some calculations and is ready to make an offer.\n")
                time.sleep(2)
                input("Press ENTER to see the banker's offer. ")
                R4_Offer = round((sum(amounts) / 8) * 0.7)
                print("\nThe banker is willing to offer you " + color.BOLD + f"${R4_Offer:,}" + color.END + ".")
                time.sleep(2)
                print("\nYou can accept this offer and walk away with the money,")
                print("or you can reject the offer and keep playing.")
                time.sleep(2)
                print("\nType 'D' for Deal, or 'N' for No Deal.")
                time.sleep(1)
                R4_DoND = input("Deal or No Deal? ")

                while True:
                    if R4_DoND == "D" or R4_DoND == "d":
                        print(color.BOLD + f"\nCongratulations, you won ${R4_Offer:,}!" + color.END)
                        time.sleep(2)
                        print("\nWould you like to find out the value of your case?")
                        R4_View = input("Type 'Y' for Yes, or 'N' for No: ")
                        while True:
                            if R4_View == "Y" or R4_View == "y":
                                print("\nYour case was worth " + color.BOLD + f"${amounts[int(myCase) - 1]:,}." + color.END)
                                time.sleep(2)
                                break
                            elif R4_View == "N" or R4_View == "n":
                                break
                            else:
                                print("\nThat is not a valid selection.\n")
                                time.sleep(1)
                                print("Would you like to find out the value of your case?")
                                R4_View = input("Type 'Y' for Yes, or 'N' for No: ")
                        break
                    elif R4_DoND == "N" or R4_DoND == "n":
                        print("\nYou chose to decline the banker's offer.")
                        time.sleep(1)
                        break
                    else:
                        print("\nThat is not a valid selection.\n")
                        time.sleep(1)
                        print("Type 'D' for Deal, or 'N' for No Deal.")
                        time.sleep(1)
                        R4_DoND = input("Deal or No Deal? ")
                if R4_DoND == "D" or R4_DoND == "d":
                    myScore = R4_Offer
                    if myScore > scoreData[0]:
                        newHigh()
                    else:
                        print("\nThanks for playing Deal or No Deal.\nCreated by Brandon Koch\n")
                        time.sleep(2)
                        input("Press ENTER to return to the menu. ")
                        menu()
                else:
                    time.sleep(1)
                    print("\nIn the 5th round, you will select 2 of the remaining cases to eliminate.")
                    print("After you have selected 2 cases to eliminate, the banker will make you an offer.\n")
                    time.sleep(2)

                    R5_Cases_Left = 2
                    while True:
                        try:
                            if R5_Cases_Left == 1:
                                print(f"There is 1 more case to eliminate this round.")
                            print("Cases remaining: ", end="")
                            print(*cases, sep=", ")
                            R5_Elim = input("Select a case to eliminate: ")
                            if R5_Elim.strip() == "":
                                raise ValueError("No case was selected.\n")
                            elif R5_Elim.isdecimal() == False:
                                raise ValueError("Only numbers are allowed for case selections.\n")
                            elif int(R5_Elim) not in cases:
                                if int(R5_Elim) < 1 or int(R5_Elim) > 26:
                                    raise ValueError("That case does not exist.\n")
                                else:   
                                    raise ValueError("That is not one of the remaining cases.\n")
                            else:
                                print(f"You eliminated case {R5_Elim}.\n")
                                R5_E = int(R5_Elim)
                                cases.remove(R5_E)
                                R5_Cases_Left -= 1
                                time.sleep(1)
                                if amounts[R5_E - 1] < 999:
                                    print(f"Case {R5_E} was worth " + color.GREEN + f"${amounts[R5_E - 1]:,}" + color.END + ".\n")
                                elif amounts[R5_E - 1] > 999 and amounts[R5_E - 1] < 33333:
                                    print(f"Case {R5_E} was worth ${amounts[R5_E - 1]:,}.\n")
                                else:
                                    print(f"Case {R5_E} was worth " + color.RED + f"${amounts[R5_E - 1]:,}" + color.END + ".\n")
                                time.sleep(2)
                                amounts[R5_E - 1] = 0
                                if R5_Cases_Left == 0:
                                    break
                        except ValueError as e:
                            print(e)
                            time.sleep(1)
                    
                    print("This is the end of round 5.")
                    time.sleep(1)
                    print("The banker did some calculations and is ready to make an offer.\n")
                    time.sleep(2)
                    input("Press ENTER to see the banker's offer. ")
                    R5_Offer = round((sum(amounts) / 6) * 0.8)
                    print("\nThe banker is willing to offer you " + color.BOLD + f"${R5_Offer:,}" + color.END + ".")
                    time.sleep(2)
                    print("\nYou can accept this offer and walk away with the money,")
                    print("or you can reject the offer and keep playing.")
                    time.sleep(2)
                    print("\nType 'D' for Deal, or 'N' for No Deal.")
                    time.sleep(1)
                    R5_DoND = input("Deal or No Deal? ")

                    while True:
                        if R5_DoND == "D" or R5_DoND == "d":
                            print(color.BOLD + f"\nCongratulations, you won ${R5_Offer:,}!" + color.END)
                            time.sleep(2)
                            print("\nWould you like to find out the value of your case?")
                            R5_View = input("Type 'Y' for Yes, or 'N' for No: ")
                            while True:
                                if R5_View == "Y" or R5_View == "y":
                                    print("\nYour case was worth " + color.BOLD + f"${amounts[int(myCase) - 1]:,}." + color.END)
                                    time.sleep(2)
                                    break
                                elif R5_View == "N" or R5_View == "n":
                                    break
                                else:
                                    print("\nThat is not a valid selection.\n")
                                    time.sleep(1)
                                    print("Would you like to find out the value of your case?")
                                    R5_View = input("Type 'Y' for Yes, or 'N' for No: ")
                            break
                        elif R5_DoND == "N" or R5_DoND == "n":
                            print("\nYou chose to decline the banker's offer.")
                            time.sleep(1)
                            break
                        else:
                            print("\nThat is not a valid selection.\n")
                            time.sleep(1)
                            print("Type 'D' for Deal, or 'N' for No Deal.")
                            time.sleep(1)
                            R5_DoND = input("Deal or No Deal? ")
                    if R5_DoND == "D" or R5_DoND == "d":
                        myScore = R5_Offer
                        if myScore > scoreData[0]:
                            newHigh()
                        else:
                            print("\nThanks for playing Deal or No Deal.\nCreated by Brandon Koch\n")
                            time.sleep(2)
                            input("Press ENTER to return to the menu. ")
                            menu()
                    else:
                        time.sleep(1)
                        print("\nIn the 6th round, you will select 2 of the remaining cases to eliminate.")
                        print("After you have selected 2 cases to eliminate, the banker will make you an offer.\n")
                        time.sleep(2)

                        R6_Cases_Left = 2
                        while True:
                            try:
                                if R6_Cases_Left == 1:
                                    print(f"There is 1 more case to eliminate this round.")
                                print("Cases remaining: ", end="")
                                print(*cases, sep=", ")
                                R6_Elim = input("Select a case to eliminate: ")
                                if R6_Elim.strip() == "":
                                    raise ValueError("No case was selected.\n")
                                elif R6_Elim.isdecimal() == False:
                                    raise ValueError("Only numbers are allowed for case selections.\n")
                                elif int(R6_Elim) not in cases:
                                    if int(R6_Elim) < 1 or int(R6_Elim) > 26:
                                        raise ValueError("That case does not exist.\n")
                                    else:   
                                        raise ValueError("That is not one of the remaining cases.\n")
                                else:
                                    print(f"You eliminated case {R6_Elim}.\n")
                                    R6_E = int(R6_Elim)
                                    cases.remove(R6_E)
                                    R6_Cases_Left -= 1
                                    time.sleep(1)
                                    if amounts[R6_E - 1] < 999:
                                        print(f"Case {R6_E} was worth " + color.GREEN + f"${amounts[R6_E - 1]:,}" + color.END + ".\n")
                                    elif amounts[R6_E - 1] > 999 and amounts[R6_E - 1] < 33333:
                                        print(f"Case {R6_E} was worth ${amounts[R6_E - 1]:,}.\n")
                                    else:
                                        print(f"Case {R6_E} was worth " + color.RED + f"${amounts[R6_E - 1]:,}" + color.END + ".\n")
                                    time.sleep(2)
                                    amounts[R6_E - 1] = 0
                                    if R6_Cases_Left == 0:
                                        break
                            except ValueError as e:
                                print(e)
                                time.sleep(1)
                        
                        print("This is the end of round 6.")
                        time.sleep(1)
                        print("The banker did some calculations and is ready to make an offer.\n")
                        time.sleep(2)
                        input("Press ENTER to see the banker's offer. ")
                        R6_Offer = round((sum(amounts) / 4) * 0.9)
                        print("\nThe banker is willing to offer you " + color.BOLD + f"${R6_Offer:,}" + color.END + ".")
                        time.sleep(2)
                        print("\nYou can accept this offer and walk away with the money,")
                        print("or you can reject the offer and keep playing.")
                        time.sleep(2)
                        print("\nType 'D' for Deal, or 'N' for No Deal.")
                        time.sleep(1)
                        R6_DoND = input("Deal or No Deal? ")

                        while True:
                            if R6_DoND == "D" or R6_DoND == "d":
                                print(color.BOLD + f"\nCongratulations, you won ${R6_Offer:,}!" + color.END)
                                time.sleep(2)
                                print("\nWould you like to find out the value of your case?")
                                R6_View = input("Type 'Y' for Yes, or 'N' for No: ")
                                while True:
                                    if R6_View == "Y" or R6_View == "y":
                                        print("\nYour case was worth " + color.BOLD + f"${amounts[int(myCase) - 1]:,}." + color.END)
                                        time.sleep(2)
                                        break
                                    elif R6_View == "N" or R6_View == "n":
                                        break
                                    else:
                                        print("\nThat is not a valid selection.\n")
                                        time.sleep(1)
                                        print("Would you like to find out the value of your case?")
                                        R6_View = input("Type 'Y' for Yes, or 'N' for No: ")
                                break
                            elif R6_DoND == "N" or R6_DoND == "n":
                                print("\nYou chose to decline the banker's offer.")
                                time.sleep(1)
                                break
                            else:
                                print("\nThat is not a valid selection.\n")
                                time.sleep(1)
                                print("Type 'D' for Deal, or 'N' for No Deal.")
                                time.sleep(1)
                                R6_DoND = input("Deal or No Deal? ")
                        if R6_DoND == "D" or R6_DoND == "d":
                            myScore = R6_Offer
                            if myScore > scoreData[0]:
                                newHigh()
                            else:
                                print("\nThanks for playing Deal or No Deal.\nCreated by Brandon Koch\n")
                                time.sleep(2)
                                input("Press ENTER to return to the menu. ")
                                menu()
                        else: 
                            time.sleep(1)
                            print("\nIn the 7th round, you will select 1 of the remaining cases to eliminate.")
                            print("After you have selected 1 case to eliminate, the banker will make you an offer.\n")
                            time.sleep(2)

                            R7_Cases_Left = 1
                            while True:
                                try:
                                    print("Cases remaining: ", end="")
                                    print(*cases, sep=", ")
                                    R7_Elim = input("Select a case to eliminate: ")
                                    if R7_Elim.strip() == "":
                                        raise ValueError("No case was selected.\n")
                                    elif R7_Elim.isdecimal() == False:
                                        raise ValueError("Only numbers are allowed for case selections.\n")
                                    elif int(R7_Elim) not in cases:
                                        if int(R7_Elim) < 1 or int(R7_Elim) > 26:
                                            raise ValueError("That case does not exist.\n")
                                        else:   
                                            raise ValueError("That is not one of the remaining cases.\n")
                                    else:
                                        print(f"You eliminated case {R7_Elim}.\n")
                                        R7_E = int(R7_Elim)
                                        cases.remove(R7_E)
                                        R7_Cases_Left -= 1
                                        time.sleep(1)
                                        if amounts[R7_E - 1] < 999:
                                            print(f"Case {R7_E} was worth " + color.GREEN + f"${amounts[R7_E - 1]:,}" + color.END + ".\n")
                                        elif amounts[R7_E - 1] > 999 and amounts[R7_E - 1] < 33333:
                                            print(f"Case {R7_E} was worth ${amounts[R7_E - 1]:,}.\n")
                                        else:
                                            print(f"Case {R7_E} was worth " + color.RED + f"${amounts[R7_E - 1]:,}" + color.END + ".\n")
                                        time.sleep(2)
                                        amounts[R7_E - 1] = 0
                                        if R7_Cases_Left == 0:
                                            break
                                except ValueError as e:
                                    print(e)
                                    time.sleep(1)
                            
                            print("This is the end of round 7.")
                            time.sleep(1)
                            print("The banker did some calculations and is ready to make an offer.\n")
                            time.sleep(2)
                            input("Press ENTER to see the banker's offer. ")
                            R7_Offer = round((sum(amounts) / 3))
                            print("\nThe banker is willing to offer you " + color.BOLD + f"${R7_Offer:,}" + color.END + ".")
                            time.sleep(2)
                            print("\nYou can accept this offer and walk away with the money,")
                            print("or you can reject the offer and keep playing.")
                            time.sleep(2)
                            print("\nType 'D' for Deal, or 'N' for No Deal.")
                            time.sleep(1)
                            R7_DoND = input("Deal or No Deal? ")

                            while True:
                                if R7_DoND == "D" or R7_DoND == "d":
                                    print(color.BOLD + f"\nCongratulations, you won ${R7_Offer:,}!" + color.END)
                                    time.sleep(2)
                                    print("\nWould you like to find out the value of your case?")
                                    R7_View = input("Type 'Y' for Yes, or 'N' for No: ")
                                    while True:
                                        if R7_View == "Y" or R7_View == "y":
                                            print("\nYour case was worth " + color.BOLD + f"${amounts[int(myCase) - 1]:,}." + color.END)
                                            time.sleep(2)
                                            break
                                        elif R7_View == "N" or R7_View == "n":
                                            break
                                        else:
                                            print("\nThat is not a valid selection.\n")
                                            time.sleep(1)
                                            print("Would you like to find out the value of your case?")
                                            R7_View = input("Type 'Y' for Yes, or 'N' for No: ")
                                    break
                                elif R7_DoND == "N" or R7_DoND == "n":
                                    print("\nYou chose to decline the banker's offer.")
                                    time.sleep(1)
                                    break
                                else:
                                    print("\nThat is not a valid selection.\n")
                                    time.sleep(1)
                                    print("Type 'D' for Deal, or 'N' for No Deal.")
                                    time.sleep(1)
                                    R7_DoND = input("Deal or No Deal? ")
                            if R7_DoND == "D" or R7_DoND == "d":
                                myScore = R7_Offer
                                if myScore > scoreData[0]:
                                    newHigh()
                                else:
                                    print("\nThanks for playing Deal or No Deal.\nCreated by Brandon Koch\n")
                                    time.sleep(2)
                                    input("Press ENTER to return to the menu. ")
                                    menu()
                            else:
                                time.sleep(1)
                                print("\nIn the 8th round, you will select 1 of the remaining cases to eliminate.")
                                print("After you have selected 1 case to eliminate, the banker will make you an offer.\n")
                                time.sleep(2)

                                R8_Cases_Left = 1
                                while True:
                                    try:
                                        print("Cases remaining: ", end="")
                                        print(*cases, sep=", ")
                                        R8_Elim = input("Select a case to eliminate: ")
                                        if R8_Elim.strip() == "":
                                            raise ValueError("No case was selected.\n")
                                        elif R8_Elim.isdecimal() == False:
                                            raise ValueError("Only numbers are allowed for case selections.\n")
                                        elif int(R8_Elim) not in cases:
                                            if int(R8_Elim) < 1 or int(R8_Elim) > 26:
                                                raise ValueError("That case does not exist.\n")
                                            else:   
                                                raise ValueError("That is not one of the remaining cases.\n")
                                        else:
                                            print(f"You eliminated case {R8_Elim}.\n")
                                            R8_E = int(R8_Elim)
                                            cases.remove(R8_E)
                                            R8_Cases_Left -= 1
                                            time.sleep(1)
                                            if amounts[R8_E - 1] < 999:
                                                print(f"Case {R8_E} was worth " + color.GREEN + f"${amounts[R8_E - 1]:,}" + color.END + ".\n")
                                            elif amounts[R8_E - 1] > 999 and amounts[R8_E - 1] < 33333:
                                                print(f"Case {R8_E} was worth ${amounts[R8_E - 1]:,}.\n")
                                            else:
                                                print(f"Case {R8_E} was worth " + color.RED + f"${amounts[R8_E - 1]:,}" + color.END + ".\n")
                                            time.sleep(2)
                                            amounts[R8_E - 1] = 0
                                            if R8_Cases_Left == 0:
                                                break
                                    except ValueError as e:
                                        print(e)
                                        time.sleep(1)
                                
                                print("This is the end of round 8.")
                                time.sleep(1)
                                print("The banker did some calculations and is ready to make an offer.\n")
                                time.sleep(2)
                                input("Press ENTER to see the banker's offer. ")
                                R8_Offer = round((sum(amounts) / 2) * 1.1)
                                print("\nThe banker is willing to offer you " + color.BOLD + f"${R8_Offer:,}" + color.END + ".")
                                time.sleep(2)
                                print("\nYou can accept this offer and walk away with the money,")
                                print("or you can reject the offer and keep playing.")
                                time.sleep(2)
                                print("\nType 'D' for Deal, or 'N' for No Deal.")
                                time.sleep(1)
                                R8_DoND = input("Deal or No Deal? ")

                                while True:
                                    if R8_DoND == "D" or R8_DoND == "d":
                                        print(color.BOLD + f"\nCongratulations, you won ${R8_Offer:,}!" + color.END)
                                        time.sleep(2)
                                        print("\nWould you like to find out the value of your case?")
                                        R8_View = input("Type 'Y' for Yes, or 'N' for No: ")
                                        while True:
                                            if R8_View == "Y" or R8_View == "y":
                                                print("\nYour case was worth " + color.BOLD + f"${amounts[int(myCase) - 1]:,}." + color.END)
                                                time.sleep(2)
                                                break
                                            elif R8_View == "N" or R8_View == "n":
                                                break
                                            else:
                                                print("\nThat is not a valid selection.\n")
                                                time.sleep(1)
                                                print("Would you like to find out the value of your case?")
                                                R8_View = input("Type 'Y' for Yes, or 'N' for No: ")
                                        break
                                    elif R8_DoND == "N" or R8_DoND == "n":
                                        print("\nYou chose to decline the banker's offer.")
                                        time.sleep(1)
                                        break
                                    else:
                                        print("\nThat is not a valid selection.\n")
                                        time.sleep(1)
                                        print("Type 'D' for Deal, or 'N' for No Deal.")
                                        time.sleep(1)
                                        R8_DoND = input("Deal or No Deal? ")
                                if R8_DoND == "D" or R8_DoND == "d":
                                    myScore = R8_Offer
                                    if myScore > scoreData[0]:
                                        newHigh()
                                    else:
                                        print("\nThanks for playing Deal or No Deal.\nCreated by Brandon Koch\n")
                                        time.sleep(2)
                                        input("Press ENTER to return to the menu. ")
                                        menu()
                                else:
                                    time.sleep(1)
                                    print(f"\nOnly 2 cases remain: the case you selected in the beginning, and case {cases[0]}.")
                                    time.sleep(2)
                                    print(f"You can decide to stay with your case, or switch to case {cases[0]}.")
                                    time.sleep(2)
                                    print("The dollar amount in the case you select will determine how much money you win.\n")
                                    time.sleep(1.5)
                                    print(f"Type 'K' to keep your original case, or 'S' to switch to case {cases[0]}.")
                                    Final_Elim = input("Keep your case or switch cases? ")

                                    while True:
                                        if Final_Elim == "K" or Final_Elim == "k":
                                            print("\nYou chose to keep your original case.")
                                            time.sleep(1.5)
                                            print(color.BOLD + f"\nCongratulations, you won ${amounts[int(myCase) - 1]:,}!" + color.END)
                                            time.sleep(2)
                                            print(f"\nWould you like to find out the value of case {cases[0]}?")
                                            Other_View = input("Type 'Y' for Yes, or 'N' for No: ")
                                            while True:
                                                if Other_View == "Y" or Other_View == "y":
                                                    print(f"\nCase {cases[0]} was worth " + color.BOLD + f"${amounts[int(cases[0]) - 1]:,}." + color.END)
                                                    time.sleep(2)
                                                    break
                                                elif Other_View == "N" or Other_View == "n":
                                                    break
                                                else:
                                                    print("\nThat is not a valid selection.\n")
                                                    time.sleep(1)
                                                    print("Would you like to find out the value of your case?")
                                                    Other_View = input("Type 'Y' for Yes, or 'N' for No: ")
                                            break
                                        elif Final_Elim == "S" or Final_Elim == "s":
                                            print(f"\nYou chose to switch to case {cases[0]}.")
                                            time.sleep(1.5)
                                            print(color.BOLD + f"\nCongratulations, you won ${amounts[int(cases[0]) - 1]:,}!" + color.END)
                                            time.sleep(2)
                                            print("\nWould you like to find out the value of your original case?")
                                            Final_View = input("Type 'Y' for Yes, or 'N' for No: ")
                                            while True:
                                                if Final_View == "Y" or Final_View == "y":
                                                    print("\nYour original case was worth " + color.BOLD + f"${amounts[int(myCase) - 1]:,}." + color.END)
                                                    time.sleep(2)
                                                    break
                                                elif Final_View == "N" or Final_View == "n":
                                                    break
                                                else:
                                                    print("\nThat is not a valid selection.\n")
                                                    time.sleep(1)
                                                    print("Would you like to find out the value of your case?")
                                                    Final_View = input("Type 'Y' for Yes, or 'N' for No: ")
                                            break
                                        else:
                                            print("\nThat is not a valid selection.\n")
                                            time.sleep(1)
                                            print(f"Type 'K' to keep your original case, or type 'S' to switch to case {cases[0]}.")
                                            time.sleep(1)
                                            Final_Elim = input("Keep your case or switch cases? ")
                                    if Final_Elim == "K" or Final_Elim == "k":
                                        myScore = amounts[int(myCase) - 1]
                                        if myScore > scoreData[0]:
                                            newHigh()
                                        else:
                                            print("\nThanks for playing Deal or No Deal.\nCreated by Brandon Koch\n")
                                            time.sleep(2)
                                            input("Press ENTER to return to the menu. ")
                                            menu()
                                    elif Final_Elim == "S" or Final_Elim == "s":
                                        myScore = amounts[int(cases[0]) - 1]
                                        if myScore > scoreData[0]:
                                            newHigh()
                                        else:
                                            print("\nThanks for playing Deal or No Deal.\nCreated by Brandon Koch\n")
                                            time.sleep(2)
                                            input("Press ENTER to return to the menu. ")
                                            menu()

def newHigh():
    print("\nYou just recorded a new high score!")

    while True:
        try:
            initials = input("Enter your initials (3 characters): ")
            if initials.strip() == "":
                raise ValueError("No initials were entered.\n")
            if len(initials) < 3 and len(initials) > 0:
                raise ValueError("Please enter 3 characters.\n")
            if len(initials) > 3:
                raise ValueError("You can only enter 3 characters.\n")
            else:
                break
        except ValueError as e:
            print(e)
            time.sleep(1)

    scoreData[0] = myScore
    scoreData[1] = str(initials)
    scoreData[2] = today_date

    print("The leaderboards have been updated with your new score.")
    time.sleep(1)
    input("\nPress ENTER to return to the menu.")

    pickle_out = open("HighScore.pkl", "wb")
    pickle.dump(scoreData, pickle_out)
    pickle_out.close()

    menu()

def leaderboard():
    default_in = open("DefaultScore.pkl", "rb")
    default = pickle.load(default_in)
    pickle_in = open("HighScore.pkl", "rb")
    updated = pickle.load(pickle_in)

    print("\n" + color.BOLD + color.UNDERLINE + "High Score" + color.END)
    if default[0] > updated[0]:
        print(f"An amount of ${default[0]:,} was won by '{default[1]}' on {default[2]}.\n")
    elif updated[0] >= default[0]:
        print(f"An amount of ${updated[0]:,} was won by '{updated[1]}' on {updated[2]}.\n")
    
    input("Press ENTER to return to the menu. ")
    menu()

menu()