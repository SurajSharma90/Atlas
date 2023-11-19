import random as rand
import time
import os
import math


class Difficulty:
    def __init__(self, name, range, sleep):
        self.name = name
        self.range = range
        self.sleep = sleep


difficulties = [Difficulty("easy", 100, 1), Difficulty("medium", 1000, 1), Difficulty("hard", 1000000, 1)]

level = [1]
exp = [0]
expNext = [100]


def UpdateLevel():
    if exp[0] >= expNext[0]:
        level[0] = level[0] + 1
        exp[0] = exp[0] - expNext[0]
        expNext[0] = (50 * math.pow(level[0], 3) - 150 * math.pow(level[0], 2) + 400 * level[0]) / 3


class Game:
    def __init__(self):
        self.running = True
        self.difficulty = 0

    def Run(self):
        while self.running:
            number = rand.randint(0, difficulties[2].range)
            print(number)
            print("...")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            print("...")
            time.sleep(difficulties[2].sleep)
            os.system("cls" if os.name == "nt" else "clear")
            print("What was the number?")
            answer = input()

            if answer == "exit()":
                self.running = False
                break

            if int(answer) == int(number):
                expGain = 10 + rand.randint(0, 100)
                print("You got it %d EXP!" % expGain)
                exp[0] = exp[0] + expGain
                UpdateLevel()
            else:
                print("Wrong, it was %d." % number)

            print("Level: %d | EXP: %d/%d" % (level[0], exp[0], expNext[0]))
            print("Press any key to continue...")
            input()
