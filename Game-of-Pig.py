import random

def roll():
    lower_limit=1
    upper_limit=6
    turn=random.randint(lower_limit, upper_limit)
    return turn
    
check =True
while check == True:
    num_players=input("Please give us the number of players in the game. 4 players total, 2 players minimum \n ")
    if num_players.isdigit():
        num_players= int(num_players)
        if 2 <= num_players <= 4:
            check=False
            
        else:
            print("Players must be between 2 and 4")    
        
    else:
        print("Try again")    

max_points=50
players_points=[0 for _ in range(num_players)]

while max(players_points) < max_points:
    
    for players_index in range(num_players):
        
        print("Player", players_index+1, "turn has just started \n")
        print("Your total score is = ", players_points[players_index], "\n")
        current_player_score=0
        
        while True:
    
            ask_roll=input("Would you like to roll? (y) ")
            
            if ask_roll.lower()=="y":
                value=roll()
                if value==1:
                    current_player_score=0
                    print("You rolled a 1. Your score turns to 0 and your turn is over\n")
                    break
                    
                else:
                    current_player_score += value
                    print("You rolled a: ", value)
                    print("Your current score is:", current_player_score, "\n")
                
            else:
                break
            
        players_points[players_index]+= current_player_score
        print("Your  new total score is: ",players_points[players_index])

winner= max(players_points)
winner_index= players_points.index(winner)

print("Player ", winner_index+1, "is the winner with a score of ", winner )