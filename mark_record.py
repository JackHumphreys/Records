

class MarkRecord:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.module1 = None
        self.module2 = None
        self.module3 = None
        self.module4 = None
        self.total = None
        self.mean = None

records = []
for count in range(2):
    record = MarkRecord()
    record.first_name = input("Please enter your first name: ")
    record.last_name = input("Please enter your last name: ")
    record.module1 = int(input("Please enter marks for module 1: "))
    record.module2 = int(input("Please enter marks for module 2: "))
    record.module3 = int(input("Please enter marks for module 3: "))
    record.module4 = int(input("Please enter marks for module 4: "))
    record.total = (record.module1+record.module2+record.module3+record.module4)
    records.append(record)


#Mean Total
total = 0
for count in range(2):
    total = total + records[count].total
mean = total/len(records)-1

    

#Main
print("_"*40)
print("|{0:>18}|{1:>2}|{2:>2}|{3:>2}|{4:>2}|{5:>3}|{6:>5}".format("Name","M1","M2","M3","M4","Total","Mean"))
for record in records:
    for count in range(2):
        meanCompare = records[count].total - mean
    print("|{0:>5} {1:>12}|{2:>2}|{3:>2}|{4:>2}|{5:>2}|{6:>5}|{7:>5}".format(record.first_name, record.last_name, record.module1, record.module2, record.module3, record.module4, record.total, meanCompare))
    print("-"*40)







    


        
