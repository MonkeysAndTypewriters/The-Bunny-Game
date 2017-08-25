#The bunny game 14/08/2017

import random
Bunnies = 10
Carrots = 100
Bunny_Strikes = False
End_Turn = 0
Strike = False
List_Of_Scores= []

print ("hello user")

Valid2 = ["Y","N"]

print ("if the day is rainy, then the bunnies on the field do not earn carrots\nBunnies in the barn earn half the carrots earned on the field")

for Turn in range(1,51):

    Valid1 = [
        ]
    for i in range (0,int(Bunnies)+1):
        Valid1.append(str(i))
    
    if Bunny_Strikes == True:
        if Strike == False:
            Strike = True
            Last = random.randint(1,3)
            End_Turn = int(Turn) + int(Last)
        print ("Turn",Turn)
        print ("today the bunnies are striking")
        if int(Turn) == int(End_Turn):
            Bunny_Strikes = False
            
    else:
        Strike = False
        print ("Turn",Turn)
        print ("You have",Carrots,"carrots")
        print ("you have",Bunnies,"Bunnies")
        
        
        Chance = random.randint(0,100)
        print ("There is a",str(Chance)+"% chance of rain")    
        Field = input("How many bunnies would you like to send to the field\n(the rest will go to work at the farm where it is safe) \n >>> ")
        while Field not in Valid1:
            print ("There was an error with your input please try again") 
            Field = input("How many bunnies would you like to send to the field\n(the rest will go to work at the Barn where it is safe) \n >>> ")

        Barn = Bunnies - int(Field)
        Roll = random.randint(0,100)
        if Roll > Chance:
            print ("there was no rain today")
            Days_Carrots = (int(Field) * 10) + (Barn * 5)
        else:
            print ("There was rain today")
            Days_Carrots = Barn * 5
        
        Special_Roll = random.randint(0,100)
        if Special_Roll == 1:
            if Field == 0:
                print ("Your bunnies avoided SNOW FALL")
            else:
                Max = int(Field)
                Cold_Kill = random.randint(1,Max)
                print ("SNOW FALL")
                print ("The snow has fallen bringing freezing cold to you bunnies in the field,\n",Cold_Kill,"Bunnies did not make it back.")
                Bunnies = Bunnies - Cold_Kill
            
        elif Special_Roll == 2:
            if Field == 0:
                print ("Your bunnies avoided LIGHTNING")
            else:
                print ("LIGHTNING")
                print ("One of your bunnies has been smited, they are no more")
                Bunnies = Bunnies - 1
                   
        elif Special_Roll == 3:
            print ("DONKEY")
            Eaten = Carrots//10
            print ("A donkey barged into your storeage, it has eaten",Eaten,"carrots")
            Carrots = Carrots - Eaten
                   
        elif Special_Roll == 4:
            if Field == 0:
                print ("Your bunnies avoided PLAGUE OF BUTTERFLYS")
            else:
                print ("PLAGUE OF BUTTERFLYS")
                print ("A Plague of butterflys flutter over the field, your bunnies are mesmorised and gaze at their splender.\nyou earn no carrots from th field.")
                Days_Carrots = 0
                   
        elif Special_Roll == 5:
            print ("FESTIVAL")
            print ("You can pay for your bunnies to go to the local Bunny festival\nif you do not pay then your bunnies will go on strike for up to 3 days")
            Pay = input("Y = Yes , N = No\nWould you like to pay 100 carrots to send your bunnies to the Festival?")
            while Pay.upper() not in Valid2:
                print ("There was an error with your input please try again")
                Pay = input("Y = Yes , N = No\nWould you like to pay 100 carrots to send your bunnies to the Festival?")

            if Pay.upper() == "Y":
                print ("Your bunnies drop their tools after work and run off to the festival to have an evening of fun")
                Carrots = Carrots - 100
            else:
                print ("Your bunnies are displeased that you are not letting them go to the festival, they stand united and go on strike")
                Bunny_Strikes = True
                
        elif Special_Roll == 6:
            print ("MR FOXY BANKER")
            print ("Mr Foxy Banker is collecting tax for the bunnies under employment, you pay 5 Carrots per bunny")
            Carrots = Carrots - Bunnies*5
            
        elif Special_Roll == 7:
            print ("OVERWORKED")
            print("Your bunnies have been over workd, they are demanding a break so they have gone on strike")
            Bunny_Strikes = True
            
        elif Special_Roll == 8:
            print ("FROST")
            print ("Frost has struck, carrots have rotted bunnies have to search harder for lushouse carrots, income is halved today")
            Days_Carrots = Days_Carrots // 2
            
        elif Special_Roll == 9:
            print ("MR BADGEER")
            print ("Mr Badger is going to take one of your Bunnies for a delicous dinner with his family, but he could buy a better dinner with 50 Carrots")
            Pay = input("Y = Yes , N = No\nWould you like to pay 50 carrots instead of your bunny?\n >>> ")
            while Pay.upper() not in Valid2:
                print ("There was an error with your input please try again")
                Pay = input("Y = Yes , N = No\nWould you like to pay 50 carrots instead of your bunny?\n >>> ")

            if Pay.upper() == "Y":
                print ("Mr Badger sped away with his carrots in the direction of the market")
                Carrots = Carrots - 50
            else:
                print ("Mr Badger chose the plumpest looking rabbit and made off before he could be stopped")
                Bunnies = Bunnies - 1
            
        elif Special_Roll == 10:
            print ("FALLEN TREE")
            print ("A tree has fallen and has damaged the barn, you must pay 150 Carrots for the repairs")
            Carrots = Carrots - 150

        elif Special_Roll == 11:
            print ("VALENTINES")
            print ("Its Valentines day and theres the sound of love in the air, your bunny population has increased by 50%")
            Bunnies = (Bunnies * 3)//2

        elif Special_Roll == 12:
            print ("BOARING DAY")
            print ("Your bunnies have had a very boaring day, this has meant that they have got on with the work as there were no distractions, todays profits have doubled")
            Days_Carrots = Days_Carrots * 2
            
        elif Special_Roll == 13:
            print ("GRANDMA MIXI")
            print ("Grandma Mixi has sadly passed away, she has left Carrots in your name how ever, you gain 200 carrots")
            Carrots = Carrots + 200
            
        elif Special_Roll == 14:
            print ("BIG MAN FLOPSY")
            Gift = Bunnies // 3
            print ("Big man Flopsy has found your farm and would like to see your company grow, so he has given you",Gift,"Bunnies to help you out")
            Bunnies = Bunnies + Gift
            
        elif Special_Roll in range(15,20):
            print ("FARMER")
            print ("A nearby farm has gone bust, the farmer is selling his Bunnies")
            Buy = input("Y = Yes , N = No\nwhould you like to buy from him?\n >>> ")
            while Buy.upper() not in Valid2:
                print ("There was an error with your input please try again")
                Buy = input("Y = Yes , N = No\nwhould you like to buy from him?\n >>> ")

            if Buy.upper() == "Y":
                print ("The farmer is selling them for 50 Carrots each")
                Many = input("How many would you like tou buy?\n >>> ")
                Valid3 = []
                for Num in range (0,(Carrots//50)+1):
                    Valid3.append(str(Num))
                while str(Many) not in Valid3:
                    print("There was an error with your input please try again")
                    Many = input ("How many would you like tou buy?\n >>> ")
                Cost = Many*50
                Bunnies = Bunnies + int(Many)
                Carrots = Carrots - int(Many)*50

        print ("Today you have earned",Days_Carrots,"carrots")
        Carrots = Carrots + Days_Carrots
    
print ("""

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~                                  ~
~                                  ~
~  Your final score was,""",Carrots,"""   ~
~                                  ~
~                                  ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
