print('''
"' _..._  ,s$$$s.'"
 '$$$$$$$s$$ss$$$$,'
 '$$$sss$$$$s$$$$$$$'
 '$$ss$$$$$$$$$$$$$$'
 '$$$s$$$$$$$$$$$$'
  '$$$$$$$$$$$$$$'
    '$$$$$$$$$$$'
     '$$$$$$$$$'
       '$$$$$'
        '$$$'
          ';'
         ';'
          ';'
         ','
          ;
         ,'
         ;
         ',
          ',
           ;
           ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road, Where do you want to go? Type "Left" or "Right".')

if choice1 == "Left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "Swim" to swim across.')
    if choice2 == "Wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if choice3 == "red":
            print("You Burned by fire. Game Over")
        elif choice3 == "blue":
            print("You were eaten by beasts. Game over.")
        elif choice3 == "yellow":
            print("Hurrahhhh!! You win.")
        else:
            print("Game over.")
    else:
        print("You get attacked by an angry trout. Game over!!")
else:
    print("You fall into a hole. Game Over!!")