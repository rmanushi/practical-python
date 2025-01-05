# pcost.py
#
# Exercise 1.27

import os

def portfolio_cost(filename):
    cwd_path =  os.getcwd()
    full_path = cwd_path + '\Work\Data' + filename
    #print(full_path)

    file = open(full_path, 'rt')

    headers = next(file).split(',')

    total = 0

    #full file content display
    print(headers)
    for line in file:
        row = line.split(',')
        #caclculate total cost for all shares
        try:
            total += (int(row[1]) * round(float(row[2].replace('\n','')),2))
        except ValueError:
            print('Bad row:', row)
    
        print(row)

    print('Total Cost: ',total)

portfolio_cost('\portfolio.csv')