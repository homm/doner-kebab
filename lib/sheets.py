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


def prepend_rows(conn, rows, config):
    spreadsheet = conn.open_by_key(config['id'])
    worksheet = spreadsheet.get_worksheet(config['worksheet'])
    row_index = find_empty_row(worksheet)
    for row in rows:
        new_row = [cell[1] for cell in row]
        worksheet.insert_row(new_row, 2)
