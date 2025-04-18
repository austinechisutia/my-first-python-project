import pandas as pd
from bs4 import BeautifulSoup

tableData = pd.read_html("https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub", header=0, flavor='bs4')

tdSorted = tableData[0].sort_values(by=["y-coordinate","x-coordinate"], ignore_index=True)

xcoord = tdSorted['x-coordinate']
ycoord = tdSorted['y-coordinate']
char = tdSorted['Character']

for i in range(1, len(ycoord)):
    if ((xcoord[i] == 12) & (ycoord[i] == 0)):
        print(" ", end='')
    if xcoord[i] - xcoord[i - 1] != 1:
        print(" " * int((xcoord[i]) - (xcoord[i - 1]) - 1), end='')
    if (ycoord[i] != (ycoord[i - 1])):
        print('\r')
    print (char[i], end='') 
print('\n')          