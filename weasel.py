import random as rd

genes = "abcdefghijklmnopqrstuvwxyz "
from termcolor import colored, cprint


def str_sub(test, target):
    foo = zip(test, target)
    lock = "".join(["1" if i[0] == i[1] else "0" for i in foo])
    return lock


def score(test, target):
    if len(test) != len(target):
        raise Exception("String lengths are not equal")
    s = 0
    for i in enumerate(test):
        if i[1] in target:
            s += 2

            if i[1] == target[i[0]]:
                s = s + 2

            elif test.count(i[1]) > target.count(target):
                s -= 2 * (test.count(i[1]) > target.count(target))

    return s, str_sub(test, target)


def projeny(test, target, mut_rate=10):
    lock = score(test, target)[1]
    for i in range(len(test)):
        if rd.randint(1, 100) < mut_rate and lock[i] != "1":
            # test = test.replace(test[i], rd.choice(genes),1)
            test = test[:i] + rd.choice(genes) + test[i + 1 :]

    return test


def reproducer(test, target, mut_rate=10, n=10):
    fitness_chart = {}
    for i in range(n):
        child = projeny(test, target, mut_rate)
        if child not in fitness_chart.keys():
            fitness_chart[child] = score(child, target)[0]
    fitness_chart = sorted([i[::-1] for i in fitness_chart.items()])[::-1]
    return fitness_chart


def god(target, mut_rate, gen=50):
    test = "".join(rd.sample(genes, len(target)))
    g = 0
    while g <= gen:
        if test == target:
            cprint(
                "Generation: {}   Child: {}   Fitness: {}".format(g, test, fitness),
                "red",
                "on_grey",
            )
            break
        else:
            g += 1
            fitness, test = reproducer(test, target, mut_rate)[0]
            print("Generation: {}   Child: {}   Fitness: {}".format(g, test, fitness))


target = str(input("What is your desired sentence? (Only Lower Case and Space)"))
mut_rate = int(input("Mutation rate of the population? "))
gen = int(input("Maximum Number Of Generations "))
god(target, mut_rate, gen)
