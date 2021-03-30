import random

def print2DArray(x):
    
    for r in x:
        array = str()
        for c in r:
            array += str(c) + " "
        print(array)
        
def findSum(arr):
    total = 0
    for r in arr:
        for c in r:
            total +=c
    print(total)


table = []
counter = 1
for r in range(10):
    row = []
    for c in range(10):
        row.append(counter)
        counter = random.randint(0,9)
    table.append(row)

print2DArray (table)

findSum(table)
    

    
