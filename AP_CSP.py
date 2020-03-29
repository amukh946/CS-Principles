def creating_list():
    rcm_boston = []
    for i in range(5):
        score = input()
        rcm_boston.append(score)
    print(rcm_boston)
    return rcm_boston

def readingInputs(path):
        with open(path, "rt") as f:
            return f.read()

def max_score(rcm_boston):
    maximum = rcm_boston[0]
    for x in rcm_boston:
        print(x, maximum, x>maximum)
        if int(x) > int(maximum):
            print("if statement", maximum)
            maximum = x
    print(maximum)
    return maximum


def swap(i, numbers):
    x = numbers[i]
    y = numbers[i+1]
    numbers[i] = y
    numbers[i+1] = x


def bubbleSort(numbers):
    for x in range(len(numbers)-1):
        for i in range(len(numbers)-1):
            if int(numbers[i]) > int(numbers[i+1]):
                swap(i, numbers)
    print(numbers)


def result():
    x = readingInputs("/Users/Haga/Anushka/intro-to-python/Examples/inputScores.txt")
    print(x)
    #readInputs(70 60 98 93 99 90 88 99 83 72)
    l = creating_list()
    max_score(l)
    bubbleSort(l)



result()



