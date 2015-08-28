# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

# Pythonic shit
import sys
from os.path import join, abspath, dirname, realpath
current = realpath(dirname(__file__))
if current not in sys.path:
    sys.path.insert(0, current)


import config
from lib import email, parser


def run():
    conn = email.connect(config.EMAIL_CONNECT)
    for uid, message in email.search(conn, config.EMAIL_SEARCH):
        # print()
        # print('+', uid, message.get_content_type(), message.get_content_charset())
        text = email.message_to_plain_text(message)
        if not text:
            continue
        parsed = parser.parse_body(text, config.PARSE_RULES)
        # print(uid, type(text), len(text), parsed)


if __name__ == "__main__":
    run()
