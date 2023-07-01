import random 
from sre_constants import BIGCHARSET                                  


sum = 0
for i in range(100):
    Small_Count = 9                                                                 # I have 9 rings for each size
    Medium_Count = 9
    Big_Count = 9
    place1_1 = ""
    place1_2 = ""
    place1_3 = ""
    place2_1 = ""
    place2_2 = ""
    place2_3 = ""
    place3_1 = ""
    place3_2 = ""
    place3_3 = ""
    win = False                                                                     # Var win was made as a Flag to start/stop the loop
    while win == False:

        random_play_size = random.randint(0, 2)
        random_place = random.randint(0, 8)



        if random_play_size == 0 and Small_Count > 0:                               # We check if we have enought Small rings to play
            if random_place == 0 and place1_1 != "SMALL":                           # We check if the first place has a Small sized ring
                if place1_1 == "MEDIUM":                                            # We check if the first place has a Medium sized ring
                    Medium_Count = Medium_Count + 1
                elif place1_1 == "BIG":                                             # We check if the first place has a Big Sized ring
                    Big_Count = Big_Count + 1
                place1_1 = "SMALL"                                                  # We put the Small sized ring on the first place
                Small_Count = Small_Count - 1
                sum = sum + 1                                                       # We update the number of moves we did


                                                                                    ########################################################
                                                                                    #          We continue with the same logic             #
                                                                                    #             on EVERY place of the 3*3                #
                                                                                    #                 so we can play the game peacefully   #
                                                                                    ########################################################


            elif random_place == 1 and place1_2 != "SMALL":
                if place1_2 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                elif place1_2 == "BIG":
                    Big_Count = Big_Count + 1
                place1_2 = "SMALL"
                Small_Count = Small_Count - 1
                sum = sum + 1
            elif random_place == 2 and place1_3 != "SMALL":
                if place1_3 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                elif place1_3 == "BIG":
                    Big_Count = Big_Count + 1
                place1_3 = "SMALL"
                Small_Count = Small_Count - 1
                sum = sum + 1
            elif random_place == 3 and place2_1 != "SMALL":
                if place2_1 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                elif place2_1 == "BIG":
                    Big_Count = Big_Count + 1
                place2_1 = "SMALL"
                Small_Count = Small_Count - 1
                sum = sum + 1
            elif random_place == 4 and place2_2 != "SMALL":
                if place2_2 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                elif place2_2 == "BIG":
                    Big_Count = Big_Count + 1
                place2_2 = "SMALL"
                Small_Count = Small_Count - 1
                sum = sum + 1
            elif random_place == 5 and place2_3 != "SMALL":
                if place2_3 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                elif place2_3 == "BIG":
                    Big_Count = Big_Count + 1
                place2_3 = "SMALL"
                Small_Count = Small_Count - 1
                sum = sum + 1
            elif random_place == 6 and place3_1 != "SMALL":
                if place3_1 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                elif place3_1 == "BIG":
                    Big_Count = Big_Count + 1
                place3_1 = "SMALL"
                Small_Count = Small_Count - 1
                sum = sum + 1
            elif random_place == 7 and place3_2 != "SMALL":
                if place3_2 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                elif place3_2 == "BIG":
                    Big_Count = Big_Count + 1
                place3_2 = "SMALL"
                Small_Count = Small_Count - 1
                sum = sum + 1
            elif random_place == 8 and place3_3 != "SMALL":
                if place3_3 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                elif place3_3 == "BIG":
                    Big_Count = Big_Count + 1
                place3_3 = "SMALL"
                Small_Count = Small_Count - 1
                sum = sum + 1



        if random_play_size == 1 and Medium_Count > 0:                              # We check if we have enought Medium rings to play
            if random_place == 0 and place1_1 != "MEDIUM":                          # We check if the first place has a Medium sized ring
                if place1_1 == "SMALL":                                             # We check if the first place has a Small sized ring
                    Small_Count = Small_Count + 1
                elif place1_1 == "BIG":                                             # We check if the first place has a Big sized ring
                    Big_Count = Big_Count + 1
                place1_1 = "MEDIUM"                                                 # We put the Medium sized ring on the first place
                Medium_Count = Medium_Count - 1
                sum = sum + 1                                                       # We update the number of moves we did


                                                                                    ########################################################
                                                                                    #          We continue with the same logic             #
                                                                                    #             on EVERY place of the 3*3                #
                                                                                    #                 so we can play the game peacefully   #
                                                                                    ########################################################


            elif random_place == 1 and place1_2 != "MEDIUM":
                if place1_2 == "SMALL":
                    Small_Count = Small_Count + 1
                elif place1_2 == "BIG":
                    Big_Count = Big_Count + 1
                place1_2 = "MEDIUM"
                Medium_Count = Medium_Count - 1
                sum = sum + 1
            elif random_place == 2 and place1_3 != "MEDIUM":
                if place1_3 == "SMALL":
                    Small_Count = Small_Count + 1
                elif place1_3 == "BIG":
                    Big_Count = Big_Count + 1
                place1_3 = "MEDIUM"
                Medium_Count = Medium_Count - 1
                sum = sum + 1
            elif random_place == 3 and place2_1 != "MEDIUM":
                if place2_1 == "SMAL":
                    Small_Count = Small_Count + 1
                elif place2_1 == "BIG":
                    Big_Count = Big_Count + 1
                place2_1 = "MEDIUM"
                Medium_Count = Medium_Count - 1 
                sum = sum + 1
            elif random_place == 4 and place2_2 != "MEDIUM":
                if place2_2 == "SMALL":
                    Small_Count = Small_Count + 1
                elif place2_2 == "BIG":
                    Big_Count = Big_Count + 1
                place2_2 = "MEDIUM"
                Medium_Count = Medium_Count - 1
                sum = sum + 1
            elif random_place == 5 and place2_3 != "MEDIUM":
                if place2_3 == "SMALL":
                    Small_Count = Small_Count + 1
                elif place2_3 == "BIG":
                    Big_Count = Big_Count + 1
                place2_3 = "MEDIUM"
                Medium_Count = Medium_Count - 1
                sum = sum + 1
            elif random_place == 6 and place3_1 != "MEDIUM":
                if place3_1 == "SMALL":
                    Small_Count = Small_Count + 1
                elif place3_1 == "BIG":
                    Big_Count = Big_Count + 1
                place3_1 = "MEDIUM"
                Medium_Count = Medium_Count - 1
                sum = sum + 1
            elif random_place == 7 and place3_2 != "MEDIUM":
                if place3_2 == "SMALL":
                    Small_Count = Small_Count + 1
                if place3_2 == "BIG":
                    Big_Count = Big_Count + 1
                place3_2 = "MEDIUM"
                Medium_Count = Medium_Count - 1
                sum = sum + 1
            elif random_place == 8 and place3_3 != "MEDIUM":
                if place3_3 == "SMALL":
                    Small_Count = Small_Count + 1
                elif place3_3 == "BIG":
                    Big_Count = Big_Count + 1
                place3_3 = "MEDIUM"
                Medium_Count = Medium_Count - 1
                sum = sum + 1
            
            

        if random_play_size == 2 and Big_Count > 0:                                 # We check if we have enought Big rings to play
            if random_place == 0 and place1_1 != "BIG":                             # We check if the first place has a Big sized ring
                if place1_1 == "SMALL":                                             # We check if the first place has a Small sized ring
                    Small_Count = Small_Count + 1
                elif place1_1 == "MEDIUM":                                          # We check if the first place has a Medium sized ring
                    Medium_Count = Medium_Count + 1
                place1_1 = "BIG"                                                    # We put the Big sized ring on the first place
                Big_Count = Big_Count - 1
                sum = sum + 1                                                       # We update the number of moves we did

                                                                                    
                                                                                    ########################################################
                                                                                    #          We continue with the same logic             #
                                                                                    #             on EVERY place of the 3*3                #
                                                                                    #                 so we can play the game peacefully   #
                                                                                    ########################################################

                                                                                    
            if random_place == 1 and place1_2 != "BIG":
                if place1_2 == "SMALL":
                    Small_Count = Small_Count + 1
                elif place1_2 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                place1_2 = "BIG"
                Big_Count = Big_Count - 1
                sum = sum + 1
            if random_place == 2 and place1_3 != "BIG":
                if place1_3 == "SMALL":
                    Small_Count = Small_Count + 1
                elif place1_3 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                place1_3 = "BIG"
                Big_Count = Big_Count - 1
                sum = sum + 1
            if random_place == 3 and place2_1 != "BIG":
                if place2_1 == "SMALL":
                    Small_Count = Small_Count + 1
                elif place2_1 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                place2_1 = "BIG"
                Big_Count = Big_Count - 1
                sum = sum + 1
            if random_place == 4 and place2_2 != "BIG":
                if place2_2 == "SMALL":
                    Small_Count = Small_Count + 1
                elif place2_2 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                place2_2 = "BIG"
                Big_Count = Big_Count - 1
                sum = sum + 1
            if random_place == 5 and place2_3 != "BIG":
                if place2_3 == "SMALL":
                    Small_Count = Small_Count + 1
                elif place2_3 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                place2_3 = "BIG"
                Big_Count = Big_Count - 1
                sum = sum + 1
            if random_place == 6 and place3_1 != "BIG":
                if place3_1 == "SMALL":
                    Small_Count = Small_Count + 1
                if place3_1 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                place3_1 = "BIG"
                Big_Count = Big_Count - 1
                sum = sum + 1
            if random_place == 7 and place3_2 != "BIG":
                if place3_2 == "SMALL":
                    Small_Count = Small_Count + 1
                if place3_2 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                place3_2 = "BIG"
                Big_Count = Big_Count - 1
                sum = sum + 1
            if random_place == 8 and place3_3 != "BIG":
                if place3_3 == "SMALL":
                    Small_Count = Small_Count + 1
                if place3_3 == "MEDIUM":
                    Medium_Count = Medium_Count + 1
                place3_3 = "BIG"
                Big_Count = Big_Count - 1
                sum = sum + 1

        if place1_1 != "" and place1_2 != "" and place1_3 != "" and place2_1 != "" and place2_2 != "" and place2_3 != "" and place3_1 != "" and place3_1 != "" and place3_2 != "" and place3_3 != "" :
                                                                                    
                                                                                    
                                                                                    ##############################################################################################################
                                                                                    #   On line 280 we make sure the 3*3 isn't empty, so we can check if any of the winning situations are True  #
                                                                                    ##############################################################################################################


            if place1_1 == place1_2 and place1_1 == place1_3:                       # On the first 5 if/elif situations we check if the rings are of the same size
                win = True
            elif place2_1 == place2_2 and place2_1 == place2_1:
                win = True
            elif place3_1 == place3_2 and place3_1 == place3_3:
                win = True
            elif place1_1 == place2_2 and place1_1 == place3_3:
                win = True
            elif place1_3 == place2_2 and place1_3 == place3_1:
                win = True

                                                                                    ######################################################################################################
                                                                                    #         On the rest elif situations we check if we have a small-medium-big ring situation          #
                                                                                    ######################################################################################################


            elif place1_1 == "SMALL" and place1_2 == "MEDIUM" and place1_3 == "BIG":
                win = True
            elif place2_1 == "SMALL" and place2_2 == "MEDIUM" and place2_3 == "BIG":
                win = True
            elif place3_1 == "SMALL" and place3_2 == "MEDIUM" and place3_3 == "BIG":
                win = True
            elif place1_1 == "SMALL" and place2_2 == "MEDIUM" and place3_3 == "BIG":
                win = True
                
            

else:                                                                               # In case the game is over,
    Average_Moves = sum / 100                                                       #         We caculate the average moves to win
    print("Average Moves to finish the game was", Average_Moves)                    #                  And we make sure the user know 'bout it