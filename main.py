print("Welcome to the First Game!")
name = input("What is your name? ")
age = int(input("How old are you? ").strip())
print(f"Hello {name}, you are {age} years old!")

if age >= 18:
    print("You are old enough to play this game!")
    wants_to_play = input("Do you want to play? (yes/no) ").strip().lower()
    if wants_to_play == 'yes':
        print("Great! Let's start the game.")

        # Here you can add the game logic
        left_or_right = input("Do you want to go left or right? (left/right) ").strip().lower()
        if left_or_right == 'left':
            ans = input("You encounter a monster! Do you want to fight or run? (fight/run) ").strip().lower()
            if ans == 'fight':
                print("You fought bravely and won the game!")
            elif ans == 'run':
                print("You ran away safely, but the game is over!")
            else:
                print("Invalid choice! You lost the game!")
        else:
            print("You fell down a hole and lost the game!")
    

        

    else:
        print("Okay, maybe next time!")
else:
    print("You are not old enough to play this game!")
  
