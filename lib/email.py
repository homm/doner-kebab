# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import re
from imaplib import IMAP4, IMAP4_SSL
from email import message_from_string

from html2text import html2text, unescape

from . import grouping


def connect(connect_conf):
    # Construct IMAP client
    imap4_class = IMAP4_SSL if connect_conf['ssl'] else IMAP4
    imap = imap4_class(connect_conf['server'])

    imap.login(connect_conf['login'], connect_conf['password'])
    return imap


def search(imap, search_conf):
    imap.select(search_conf['mailbox'])

    res, found = imap.search(
        'utf-8',
        # 'ALL',
        'FROM', '"{0}"'.format(search_conf['from']),
        'SUBJECT', '"{0}"'.format(search_conf['subject']),
    )

    for uids in grouping(found[0].split(' '), 20):
        res, fetched = imap.fetch(','.join(uids), '(RFC822)')

        for uid, i in zip(uids, range(0, len(fetched), 2)):
            yield uid, message_from_string(fetched[i + 0][1])


def message_to_plain_text(message):
    content_type = None
    content_charset = None

    if message.is_multipart():
        for part in message.get_payload():
            if part.is_multipart():
                # print('+', part.get_content_type(), part.get_content_charset())
                payload = message_to_plain_text(part)
                content_type = 'text/plain'
                content_charset = ''
                break

            # print('|', part.get_content_type(), part.get_content_charset())
            if part.get_content_type() in ['text/plain', 'text/html']:
                payload = part.get_payload(decode=True)
                content_type = part.get_content_type()
                content_charset = part.get_content_charset()

                if content_type == 'text/plain':
                    break
    else:
        payload = message.get_payload(decode=True)
        content_type = message.get_content_type()
        content_charset = message.get_content_charset()

    if not content_type:
        return

    if content_charset is None:
        content_charset = 'ascii'
    if content_charset:
        payload = payload.decode(content_charset, 'ignore')

    if content_type == 'text/html':
        payload = unescape(html2text(payload))

    # Convert line endings.
    payload = payload.replace('\r\n', '\n').replace('\r', '\n')

    return payload
