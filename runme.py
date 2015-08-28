# coding: utf-8
from __future__ import absolute_import

# Pythonic shit
import sys
from os.path import join, abspath, dirname, realpath
current = realpath(dirname(__file__))
if current not in sys.path:
    sys.path.insert(0, current)


import config
from lib import email


def run():
    conn = email.connect(config.EMAIL_CONNECT)
    for uid, message in email.search(conn, config.EMAIL_SEARCH):
        text = email.message_to_text(message)
        print
        print '>>>', uid, type(text), text


if __name__ == "__main__":
    run()
