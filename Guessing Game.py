import random
number = random.randint(1,100)
score = 100
for i in range(1,8):
    user_guess = int(input("🤔 Enter Your Guess:"))
    if user_guess == number:
        print("🎉You Got it! Congratulations!")
        break
    elif user_guess>number:
        print("Wrong Guess!HEHEHE")
        print("You gone tooo high")
    elif user_guess<number:
        print("Wrong Guess!Hehehe")
        print("You put too small Number. Make it Big Niiggaaaaa Hehehe")
    
    if user_guess != number:
        score = score - 10


print("CORRECT NUMBER IS:",number)
print("\nYour Final Score is: ",score)