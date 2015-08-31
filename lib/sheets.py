# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import gspread
from oauth2client.client import SignedJwtAssertionCredentials


def connect(conf):
    credent = SignedJwtAssertionCredentials(
        conf['client_email'],
        conf['private_key'],
        ['https://spreadsheets.google.com/feeds'],
    )
    return gspread.authorize(credent)


def append_rows(conn, rows, config):
    spreadsheet = conn.open_by_key(config['id'])
    worksheet = spreadsheet.get_worksheet(config['worksheet'])
    row_index = find_empty_row(worksheet)
    for row in rows:
        cell_index = 1
        for cell in row:
            worksheet.update_cell(row_index, cell_index, cell[1])
            cell_index += 1
        row_index += 1

def find_empty_row(worksheet):
    row_index = 1
    row = worksheet.row_values(row_index);
    while (not is_empty_row(row)):
        row_index += 1
        row = worksheet.row_values(row_index);
    return row_index

def is_empty_row(row_values):
    for value in row_values:
        if (value != 'None'):
            return False
    return True
