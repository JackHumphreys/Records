import random
import pdb

class LotteryRecord:
    def __init__(self):
        self.date = None
        self.numbers = []

finalRecord = []
finished = False
while not finished:
    tempRecord = LotteryRecord()
    date = input("Please enter the date of the lottery draw (type stop if finished): ")
    if date == "stop":
        finished = True
    else:
        tempRecord.date = date
        amount = int(input("Please enter who many lottery tickets you want for this date: "))
        numbers = []
        for count in range(amount):
            for count in range(6):
                randomNum = random.randint(1,49)
                numbers.append(randomNum)
            tempRecord.numbers.append(numbers)
            numbers = []
    finalRecord.append(tempRecord)

for tempRecord in finalRecord:
        print(tempRecord.date)
        print(tempRecord.numbers)

    
