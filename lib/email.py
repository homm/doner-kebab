# coding: utf-8
from __future__ import absolute_import

from imaplib import IMAP4, IMAP4_SSL
from email import message_from_string

from . import grouper


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
        'FROM', '"{0}"'.format(search_conf['from']),
        'SUBJECT', '"{0}"'.format(search_conf['subject']),
    )

    for uids in grouper(found[0].split(' '), 10):
        res, fetched = imap.fetch(','.join(uids), '(RFC822.HEADER BODY.PEEK[1])')

        for uid, i in zip(uids, range(0, len(fetched), 3)):
            headers = message_from_string(fetched[i + 0][1])
            yield uid, headers, fetched[i + 1][1]
