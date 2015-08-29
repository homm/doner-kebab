# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

# Pythonic shit
import sys
from os.path import join, abspath, dirname, realpath
current = realpath(dirname(__file__))
if current not in sys.path:
    sys.path.insert(0, current)


import logging

import config
from lib import email, parser, sheets


logger = logging.getLogger(__name__)


def run():
    email_conn = email.connect(config.EMAIL_CONNECT)
    if not email_conn:
        return

    handled = []
    for uid, message in email.search(email_conn, config.EMAIL_SEARCH):
        text = email.message_to_plain_text(message)
        if not text:
            logger.warn('No text body for message {}.'.format(uid))
            continue

        parsed = parser.parse_body(text, config.PARSE_RULES)
        missed = [name for name, value in parsed if value is None]
        if missed:
            logger.warn('No value for fields {} for message {}.'.format(
                        ','.join(missed), uid))
            continue

        logger.info("id: {} {}".format(uid, repr(parsed)))

        handled.append(uid)

    connection = sheets.connect(config.GOOGLE_AUTH)

    if handled:
        email.mark_as_seen(email_conn, handled)


if __name__ == "__main__":
    logging.basicConfig(level='INFO')
    run()
