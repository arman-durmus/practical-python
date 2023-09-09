# report.py
#
# Exercise 2.4
from fileparse import parse_csv


def read_portfolio(filename):
    with open(filename) as f:
        return parse_csv(f,  types=[str, int, float])


def read_prices(filename):
    with open(filename) as f:
        prices = parse_csv(f, types=[str, float], has_headers=False)
    return {name: price for name, price in prices}


def make_report(pf, prices):
    report = []
    for stock in pf:
        new_price = prices[stock['name']]
        report.append((stock['name'], stock['shares'],
                      new_price, new_price - stock['price']))
    return report


def print_report(report, headers=('Name', 'Shares', 'Price', 'Change')):
    print(
        f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(' '.join([''.join(['-' for _ in range(10)])
          for _ in range(len(headers))]))

    for r in report:
        print(
            f'{r[0]:>10s} {r[1]:>10d} {"$"+str(round(r[2], 2)):>10s} {r[3]:>10.3f}')


def portfolio_report(portfolio_filename, prices_filename):
    pf = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(pf, prices)
    print_report(report)


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)
