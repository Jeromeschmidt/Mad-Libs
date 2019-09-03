
##################################### flask
# from flask import Flask
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'This will be a Mad Libs Machine!'
#
# if __name__ == '__main__':
#     app.run()
######################################

# from PyDictionary import PyDictionary
#
# dictionary = PyDictionary()
import random

noun = list()
adjective = list()
verb = list()
adverb = list()
sampleMadLib = "\nLittle Red Riding <nn is a \n \
<jj fairy tale for young children. \n \
It is a story about a <jj girl and a wolf. \n \
The girl's mother sends her to take <nn to her sick grandmother. \n \
The mother tells her she must not <vb on the way. \n \
A wolf sees the girl walking through the <nn (plural) and makes a plan to <vb her. \n \
The wolf <rb asks the girl where she is going. \n \
The girl <vb (plural) him, because he seems <jj . \n \
Then the wolf tells her to pick some <nn (plural) for her grandmother. \n \
While she is <vb (plural) flowers, the wolf goes to her grandmother's house and eats her. \n \
He puts on the grandmother's <nn and gets into her bed. \n \
When the girl arrives at her grandmother's house, she gets into <nn with the wolf. \n \
The wolf leaps upon the child and <vb (plural) her"

#color help found at https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

def user_input(prompt):
    #taken from Captain Rainbow checklist#
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    while(user_input.isalpha() == False):
        user_input = input(bcolors.RED + "Please enter a valid input:\n" + bcolors.END)
    return user_input

def getNoun():
    noun.append(user_input(bcolors.YELLOW + "Enter a noun:\n"+ bcolors.END))

def getAdjective():
    adjective.append(user_input(bcolors.YELLOW + "Enter a adjective:\n"+ bcolors.END))

def getVerb():
    verb.append(user_input(bcolors.YELLOW + "Enter a verb:\n"+ bcolors.END))

def getAdverb():
    adverb.append(user_input(bcolors.YELLOW + "Enter a adverb:\n"+ bcolors.END))

def fillInMadLib():
    i = 0
    j = 0
    final = ""
    while(i < len(sampleMadLib)):
        if(sampleMadLib[i] == "<"):
            j = i
            while(sampleMadLib[j] != " "):
                j+=1
            if(sampleMadLib[i:j] == "<nn"):
                final = final + noun[random.randint(0, len(noun)-1)]
            elif(sampleMadLib[i:j] == "<jj"):
                final = final + adjective[random.randint(0, len(adjective)-1)]
            elif(sampleMadLib[i:j] == "<vb"):
                final = final + verb[random.randint(0, len(verb)-1)]
            elif(sampleMadLib[i:j] == "<rb"):
                final = final + adverb[random.randint(0, len(adverb)-1)]

            i = j
        else:
            final = final + sampleMadLib[i]
            i += 1
    print(bcolors.GREEN + final + bcolors.END)

def initial_start():
    runWhile = True
    while(runWhile == True):
        for i in range(len(sampleMadLib)):
            if(sampleMadLib[i-1] == "<"):
                compString = ((sampleMadLib[i] + sampleMadLib[i+1] +sampleMadLib[i+2]))
                if(compString == "nn "):
                    getNoun()
                elif(compString == "jj "):
                    getAdjective()
                elif(compString == "vb "):
                    getVerb()
                else:#(compString == "rb "):
                    getAdverb()

        runWhile = False
        fillInMadLib()
initial_start()
