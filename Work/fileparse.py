# fileparse.py
#
# Exercise 3.3

import csv
import os

cwd_path =  os.getcwd()
data_path = cwd_path + '\Work\Data'

def parse_csv(filename,select=None,types=None,has_headers=True,delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    full_path = data_path + filename
    with open(full_path) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        headers = next(rows) if has_headers else []

        if select:
            indices = [headers.index(col_name) for col_name in select]
            headers = select
        else:
            indices = []

        records = []
        for rowno, row in enumerate(rows, 1):
            if not row:     # Skip rows with no data
                continue

            # If specific column indices are selected, pick them out
            if select:
                row = [ row[index] for index in indices]

            # Apply type conversion to the row
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue

            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records

portfolio = parse_csv('\portfolio.csv',select=['name','shares','price'],types=[str, int, float])
print(portfolio)