# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals
import string
import gspread
from oauth2client.client import SignedJwtAssertionCredentials


def connect(conf):
    credent = SignedJwtAssertionCredentials(
        conf['client_email'],
        conf['private_key'],
        ['https://spreadsheets.google.com/feeds'],
    )
    return gspread.authorize(credent)


def prepend_rows(conn, rows, config):
    spreadsheet = conn.open_by_key(config['id'])
    worksheet = spreadsheet.get_worksheet(config['worksheet'])
    headers = rows[0]

    col_count = len(headers)
    all_values = worksheet.get_all_values()

    cols_values = get_cols_values(all_values, col_count)

    new_values = [[cell[1] for cell in row] for row in rows]

    # Getting index of cells with ids
    col_names = [cell[0] for cell in headers]
    id_index = col_names.index('id')

    new_values = sorted(new_values, key=lambda x: int(float(x[id_index])), reverse=True)

    # Inserting new values after headers
    cols_values = [cols_values[0]] + new_values + cols_values[1:]

    row_count = len(cols_values)

    # Add extra cols or rows if not enough existing
    if worksheet.row_count < row_count:
        worksheet.add_rows(row_count - worksheet.row_count)
    if worksheet.col_count < col_count:
        worksheet.add_cols(col_count - worksheet.col_count)

    # Select cells
    cell_list = worksheet.range("A1:" + string.uppercase[col_count - 1] + str(row_count))

    # Make flat list of data
    cell_values = reduce(lambda res, x: res + x, cols_values, [])

    for i, val in enumerate(cell_values):
        cell_list[i].value = val

    worksheet.update_cells(cell_list)

def get_cols_values(all_values, col_count):
    cols_values = []
    for row in all_values:
        cell_values = row[:col_count]
        diff = col_count - len(cell_values)
        if diff > 0:
            for i in range(diff):
                cell_values.append('')
        cols_values.append(cell_values)
    return cols_values
