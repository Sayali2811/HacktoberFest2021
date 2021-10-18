#1."Winning Rules of the Rock paper scissor game as follows:
    # Rock vs paper->paper wins 
    # Rock vs scissor->Rock wins
    # paper vs scissor->scissor wins
# Rules for winning
print("______Rock Paper Scissor Game________\n")
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
while True:
    p_1 =str(input("Player 1, Enter rock/paper/scissors: "))
    p_2 =str(input("Player 2, Enter rock/paper/scissors: "))
    def rock_paper_scissor(player1,player2):
        a_list=["rock","paper","scissors"]

        while (player1 not in a_list or player2  not in a_list):
            print("You have entered invalid input!!...Please enter a valid input\n")
            player1 =str(input("Player 1, Enter rock/paper/scissors: "))
            player2 =str(input("Player 2, Enter rock/paper/scissors: "))

        while player1==player2:
            print("Nobody wins...Try Again")
            player1 =str(input("Player 1, Enter rock/paper/scissors: "))
            player2 =str(input("Player 2, Enter rock/paper/scissors: "))
        if ((player1== "rock") and (player2 == "paper")):
                print ("Player 2 wins!")
        elif ((player1 == "paper") and (player2 == "rock")):
                    print ("<=Player 1 wins!=>")

        elif ((player1 == "rock" )and( player2 == "scissors")):
                    print( "Player 1 wins!")

        elif ((player_ == "scissors") and (player2 == "rock")):
                    print ("Player 2 wins")
        elif ((player1 == "paper" )and (player2 == "scissors")):
                    print ("Player 2 wins!")

        elif ((player1 == "scissors" )and (player2 == "paper")):
                    print ("Player 1 wins!")
        
                
    rock_paper_scissor(p_1,p_2)     
    print("Do you want to play again? (Y/N)")
    ans = input()
  
    # if user input n or N then condition is True
    if ans == 'n' or ans == 'N':
        break
print("\nThanks for playing")
