print("Welcome to the First Game!")
name = input("What is your name? ")
age = int(input("How old are you? ").strip())
print(f"Hello {name}, you are {age} years old!")

if age >= 18:
    print("You are old enough to play this game!")
    wants_to_play = input("Do you want to play? (yes/no) ").strip().lower()
    if wants_to_play == 'yes':
        print("Great! Let's start the game.")
else:
    print("You are not old enough to play this game!")
  
