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

    col_count = len(rows[0])
    # Remove unnecessary cols values
    all_values = [x[:col_count] for x in worksheet.get_all_values()]

    new_values = [[cell[1] for cell in row] for row in rows]

    # Getting index of cells with ids
    col_names = [cell[0] for cell in rows[0]]
    id_index = col_names.index('id')

    new_values = sorted(new_values, key=lambda x: int(float(x[0])), reverse=True)
    print(new_values)

    # Inserting new values after headers
    all_values = [all_values[0]] + new_values + all_values[1:]

    row_count = len(all_values)

    # Add extra cols or rows if not enough existing
    if worksheet.row_count < row_count:
        worksheet.add_rows(row_count - worksheet.row_count)
    if worksheet.col_count < col_count:
        worksheet.add_cols(col_count - worksheet.col_count)

    # Select cells
    cell_list = worksheet.range("A1:" + string.uppercase[col_count - 1] + str(row_count))

    # Make flat list of data
    cell_values = reduce(lambda res, x: res + x, all_values, [])

    for i, val in enumerate(cell_values):
        cell_list[i].value = val

    worksheet.update_cells(cell_list)
