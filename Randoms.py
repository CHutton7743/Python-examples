import random


grammarFile = input("What is the name of the file you want to run?")

lines = open(grammarFile).readlines()

grammar = {}

for line in lines:
    if(line.__contains__("\n")):
        line = line.replace("\n", "")
    header = line.split(":")[0]
    line = line.split("=")
    line.pop(0)
    grammar[header] = line


rules = grammar.keys()
print("Available keys to generate are: ")
print(rules)


Validkey= False
startRule = ""
while Validkey == False:
    startRule = input("What rule would you like to start at? ")
    if rules.__contains__(startRule):
        print("Key found!")
        Validkey = True
    else:
        print("Key not found, please enter a valid key")

Validkey = False

while Validkey == False:
    reps = int(input("How many repetitions would you like this program to execute?"))
    if(reps <1):
        print("Please enter a positive number to determine how many times this program will run")
    else:
        Validkey = True
        print("This program will run ", reps, " times")

def isRule(ruleString):
    if rules.__contains__(ruleString):
        return True
    else:
        return False

returnString = ""  # 1 | 2| + etc.
def recursiveSolution(rulesList):
    #startRule          --------- the rule we are attempting to use
    #reps           -------- how many times to recursively call function

    #run recursiveSolution reps times
    #each call of recursiveSolutions should run the startRule a Randomly select the rule to call
            # read each line of the grammar file and find the rule we want
            # once we find the rule split that line into its rule and tokens, keep tokens
    for rule in rulesList:
        if isRule(rule) == True:
            tokens = grammar.get(rule)
            #tokens = tokens.split("|")
            #split the string into individual tokens, return randomly one of those strings
            temp = tokens[0]
            temp = temp.split("|")
            list = temp[random.randint(0, len(temp)-1)]
            list = list.split(" ")
            recursiveSolution(list)
        else:
            global returnString 
            returnString += rule + " "
            return -1

def getStart(startRule):
    rule1 =grammar.get(startRule)
    value1 = rule1[0].split("|")
    ruleList = value1[random.randint(0, len(value1)-1)]
    ruleList =  ruleList.split (" ")
    return ruleList


for i in range(reps):
    returnString = ""

    recursiveSolution(getStart(startRule))
    print(returnString)

        

    # call recursiveSolution(reps-1)






    


    


            

