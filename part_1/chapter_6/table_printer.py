tableData = [['apples', 'oranges', 'cherries', 'banana'], 
            ['Alice', 'Bob', 'Carol', 'David'], 
            ['dogs', 'cats', 'moose', 'goose']]

def tablePrinter(table):
    colWidth = [max(len(item) for item in column)for column in table]
    for row in range(len(table[0])):
        for col in range(len(table)):
            print(table[col][row].rjust(colWidth[col]), end=' ')
        print()
    
tablePrinter(tableData)