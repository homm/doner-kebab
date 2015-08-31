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
    for j, row in enumerate(rows, start=row_index):
        for i, cell in enumerate(row):
            worksheet.update_cell(j, i + 1, cell[1])

def find_empty_row(worksheet):
    row_index = 1
    while True:
        row = worksheet.row_values(row_index)
        if is_empty_row(row):
            return row_index
        row_index += 1

def is_empty_row(row_values):
    if not row_values:
         return True
    for value in row_values:
        if value != 'None':
            return False
    return True
