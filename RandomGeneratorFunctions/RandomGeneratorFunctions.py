import random

class RandomGeneratorFunctions:

    def GenRandom(start, end):
        return random.randint(start, end), random.uniform(start, end)

    def GenRandomWithSeed(seednum, start, end):
        random.seed(seednum)
        return random.randint(start, end), random.uniform(start, end)

    def GenRandomListWithSeed(seednum, start, end, listSize):
        intList = []
        decimalList = []
        random.seed(seednum)
        for x in range(listSize):
            intList.append(random.randint(start, end))
            decimalList.append(random.uniform(start, end))

        return intList, decimalList

    def GetRandomItemFromList(list):
        random.seed()
        index = random.randint(0, len(list)-1)
        return list[index]

    def GetRandomItemFromListWithSeed(seednum, list):
        random.seed(seednum)
        index = random.randint(0, len(list)-1)
        return list[index]

    def GetSubsetFromList(n, list):
        random.seed()
        indexList = []
        response = []

        for index in range(n):
            indexList.append(random.randint(0, len(list)-1))

        for index in indexList:
            response.append(list[index])

        return response

    def GetSubsetFromListWithSeed(seednum, n, list):
        random.seed(seednum)
        indexList = []
        response = []

        for index in range(n):
            indexList.append(random.randint(0, len(list)-1))

        for index in indexList:
            response.append(list[index])

        return response