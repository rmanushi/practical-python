# report.py
#
# Exercise 2.4
import csv
import os

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0
    cwd_path =  os.getcwd()
    full_path = cwd_path + '\Work\Data' + filename

    with open(full_path) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return total_cost


def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    cwd_path =  os.getcwd()
    full_path = cwd_path + '\Work\Data' + filename
    portfolio = []

    with open(full_path, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name' : row[0], 'shares': int(row[1]), 'price' : float(row[2])}
            portfolio.append(holding)
        
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    cwd_path =  os.getcwd()
    full_path = cwd_path + '\Work\Data' + filename
    prices = {}

    with open(full_path) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
     
    return prices

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for r in portfolio:
        curr_price = prices[r['name']]
        change = curr_price - r['price']
        report_record = (r['name'], r['shares'], curr_price, round(change,2))
        rows.append(report_record )

    return rows


portfolio = read_portfolio('\portfolio.csv')
prices = read_prices('\prices.csv')
report = make_report_data(portfolio,prices)

###total = 0.0
###for s in portfolio:
###    total += s['shares'] * s['price']
###print(total)
#print(prices)
#print(portfolio_cost('\portfolio.csv'))
#headers = ('Name', 'Shares', 'Price', 'Change')
#print('%10s %10s %10s %10s' % headers)
#print(('-' * 10 + ' ') * len(headers))
#for row in report:
#    print('%10s %10d %10.2f %10.2f' % row)

print(portfolio_cost('\portfoliodate.csv'))
            