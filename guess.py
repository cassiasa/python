print("Welcome!")
guess = int(input("Guess the number: "))
if guess < 5:
     print("Too low!")
else:
     if guess == 5:
          print("You win!")
     else:
          if guess > 5:
               print("Too high!")
while guess !=5:
     guess = int(input("Guess the number: "))
     if guess < 5:
          print("Too low!")
     else:
          if guess > 5:
               print("Too high!")
          else:
               print("You win!")          
print("Game over")
