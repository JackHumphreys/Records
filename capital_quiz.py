#Country Quiz
import random

def answers():
    countries_capitals = [
        ["England","London"],
        ["France","Paris"],
        ["Belgium","Brussels"],
        ["Germany","Berlin"],
        ["America","Washington DC"],
        ["Holland","Amstadam"]
        ]
    return countries_capitals

def quiz(quiz_list):
    for count in range(0,7):
        score = 0
        question = random.randint[1,len(quiz_list)-1]
        user_answer = input("Capital of {0}: ".format(quiz_list[question][0]))
        if user_answer == quiz_list[question][1]:
            score = score + 1
            print("Correct")
        else:
            print("Inncorrect")
        quiz_list.pop(question)
        

#Main

quiz_list = answers()
quiz(quiz_list)
