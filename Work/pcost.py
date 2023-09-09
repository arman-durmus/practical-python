# pcost.py
#
# Exercise 1.27
import sys
from report import read_portfolio


def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    total_worth = 0
    for idx, line in enumerate(portfolio):
        try:
            total_worth += line['shares'] * line['price']
        except ValueError:
            print(f'Row {idx}: Bad row: {line}')
    return total_worth


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/missing.csv'

    cost = portfolio_cost(filename)
    print('Total cost:', cost)
