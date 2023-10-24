#Simple game that allows the user to guess if a number is a prime number or not.

import random

running = True
score = 0
streak = 0


def checkPrime(number):
    isPrime = True
    for n in range(1, int(number / 2)):
        if number % n == 0:
            isPrime = False
            break

    return isPrime


while running == True:
    print("Welcome to the Prime Game!")
    print("Guess if the number is a prime number...")

    genNumber = random.randint(1000, 10000)
    print("Number: " + str(genNumber))
    isPrime = checkPrime(genNumber)
    print(isPrime)

    guess = input()

    if guess == str(isPrime):
        print("Correct! +1 score and streak!")
        score += 1
        streak += 1
    else:
        print("Wrong! streak reset!")
        streak = 0

    print("Score: " + str(score))
    print("Streak: " + str(streak))
