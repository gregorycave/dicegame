import random

def printRules():
    print("""The rules of the game are as follows:
Players take turns to throw a dice.
If the throw is a 'Double', i.e. two 2's, two 3's, ect.
The player's score reverts to zero and their turn ends""")
    main()
    
def playerTurn(player,score):
    print("Your turn {0}!".format(player))
    anotherGo = "Y"
    scoreThisTurn = 0
    while anotherGo == "Y" or anotherGo == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print("You rolled {0} and {1}".format(die1,die2))
        if die1 == die2:
            scoreThisTurn = 0
            cumulativeScore = 0
            anyKey = input("Bad luck! Press any key to coninue")
            anotherGo = "n"
        else:
            scoreThisTurn = scoreThisTurn + die1 + die2
            cumulativeScore = score + scoreThisTurn
            print("Your score this turn is {0}".format(scoreThisTurn))
            print("Your cumulative score is {0}".format(cumulativeScore))
            if  cumulativeScore >= 50:
                anotherGO = "y"
            else:
                anotherGo = input("Another go? (Answer y or n)")
                
    return  cumulativeScore

def startGame():
    score1 = 0
    score2 = 0
    player1 = input("Enter player 1's name :")
    player2 = input("Enter player 2's name :")
    while score1 < 50 and score2 < 50:
        totalScore = playerTurn(player1, score1)
        score1 = totalScore
        if score1 >= 50:
            print("You Win!")
        else:
            totalScore = playerTurn(player2, score2)
            score2 = totalScore
            if score2 >= 50:
                print("You Win!")



def menu():
      print("\n\n*********MENU*********")
      print("1. Display rules.")
      print("2. Start new game."   )
      print("3. Exit"   )
      print("*********MENU*********")
      choice=input("\nEnter choice: ")
      return choice

def main():
    choice=menu()
    while choice!=3:
            if choice=='1':
                  printRules()
            elif choice=='2':
                  startGame()
            elif choice=='3':
                  break
            else:
                  print("Incorrect input, returning to menu.")
                  main()
                  
main()
                
