
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

noun = list()
plural_noun = list()
adjective = list()
verb = list()
interjection = list()
preposition = list()
adverb = list()
sampleMadLib = "\nLittle Red Riding <nn  is a/an <jj fairy tale for young children.\nIt is a story about a/an <jj girl and a wolf.\nThe girl's mother sends her to take <food to her sick grandmother.\nThe mother tells her she must not <vb on the way.\nA wolf sees the girl walking through the <nns and makes a plan to <vb her.\nThe wolf <rb asks the girl where she is going.\nThe girl <vbz him, because he seems <jj.\nThen the wolf tells her to pick some <nns for her grandmother.\nWhile she is <vbg flowers, the wolf goes to her grandmother's house and eats her.\nHe puts on the grandmother's <nn and gets into her bed.\nWhen the girl arrives at her grandmother's house, she gets into <nn with the wolf.\nThe wolf leaps upon the child and <vbz her"

def user_input(prompt):
    #taken from Captain Rainbow checklist#
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def getNoun():
    noun.append(user_input("Enter a noun:\n"))

def getPlural_Noun():
    plural_noun.append(user_input("Enter a plural noun:\n"))

def getAdjective():
    adjective.append(user_input("Enter a adjective:\n"))

def getVerb():
    verb.append(user_input("Enter a verb:\n"))

def getInterjection():
    interjection.append(user_input("Enter a interjection:\n"))

def getPreposition():
    preposition.append(user_input("Enter a preposition:\n"))

def getAdverb():
    adverb.append(user_input("Enter a adverb:\n"))

def fillInMadLib():
    for i in range(len(sampleMadLib)):
        if(sampleMadLib[i-1] == "<"):
            j = i
            while(sampleMadLib[j] != " "):
                j += 1
            sampleMadLib.split(i-1, j) = noun[1]
    for i in range(len(sampleMadLib)):
        print(sampleMadLib[i])

def test():
    for i in range(len(sampleMadLib)):
        if(sampleMadLib[i-1] == "<"):
            compString = ((sampleMadLib[i] + sampleMadLib[i+1] +sampleMadLib[i+2]))
            if(compString == "nn "):
                getNoun()
            elif(compString == "jj "):
                getAdjective()
            elif(compString == "vb "):
                getVerb()
            elif(compString == "nns "):
                getPlural_Noun()
            elif(compString == "rb "):
                getAdverb()
            elif(compString == "vbg "):
                getNoun()
            elif(compString == "vbz "):
                getNoun()
            else:
                getNoun()

            # if( == "nn "):
            #     print((sampleMadLib[i] + sampleMadLib[i+1] +sampleMadLib[i+2]))
            #     getNoun()

            #elif():

            #else:
    fillInMadLib()


test()
