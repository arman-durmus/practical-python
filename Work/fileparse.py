# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a csv file into a list of records
    '''
    if isinstance(lines, str):
        raise SystemExit('lines argument should be an iterable.')
    rows = csv.reader(lines, delimiter=delimiter)

    idx = []
    if has_headers:
        # Read the file headers
        headers = next(rows)
        if select:
            idx = [headers.index(colname) for colname in select]
            headers = [headers[i] for i in idx]
    elif select:
        raise RuntimeError("Select argument requires column headers")
    records = []
    for i, row in enumerate(rows):
        if not row:
            continue
        if idx:
            row = [row[i] for i in idx]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {i+1}: Couldn't convert {row}")
                    print(f"Row {i+1}: {e}")
                continue
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
