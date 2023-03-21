tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(lists):
    for i in range(len(lists)+1):
        for j in range(len(lists)):
            print(lists[j][i], end=" ")
        print('', end='\n')


printTable(tableData)