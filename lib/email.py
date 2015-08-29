# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import re
import logging
from imaplib import IMAP4, IMAP4_SSL
from email import message_from_string

from html2text import HTML2Text, unescape

from . import grouping


logger = logging.getLogger(__name__)


def connect(connect_conf):
    # Construct IMAP client
    imap4_class = IMAP4_SSL if connect_conf['ssl'] else IMAP4
    try:
        imap = imap4_class(connect_conf['server'])
    except Exception as e:
        logger.error('Can not connect to host {}.\n{}'.format(
                     connect_conf['server'], e))
        return

    try:
        imap.login(connect_conf['login'], connect_conf['password'])
    except Exception as e:
        logger.error('Can not login as {}.\n{}'.format(
                     connect_conf['login'], e))
        return

    return imap


def search(imap, search_conf):
    imap.select(search_conf['mailbox'], readonly=False)

    res, found = imap.search(
        'utf-8',
        'UNSEEN',
        'FROM', '"{0}"'.format(search_conf['from']),
        'SUBJECT', '"{0}"'.format(search_conf['subject']),
    )
    if not found[0]:
        logger.debug('not found')
        return

    for uids in grouping(found[0].split(' '), 20):
        logger.debug('found: {}'.format(repr(uids)))
        res, fetched = imap.fetch(','.join(uids), '(RFC822)')

        for uid, i in zip(uids, range(0, len(fetched), 2)):
            yield uid, message_from_string(fetched[i + 0][1])


def mark_as_seen(imap, uids):
    imap.store(','.join(uids), '+FLAGS', '(SEEN)')


def message_to_plain_text(message):
    content_type = None
    content_charset = None

    if message.is_multipart():
        for part in message.get_payload():
            if part.is_multipart():
                logger.debug('+ {} {}'.format(part.get_content_type(),
                                              part.get_content_charset()))
                payload = message_to_plain_text(part)
                content_type = 'text/plain'
                content_charset = ''
                break

            logger.debug('| {} {}'.format(part.get_content_type(),
                                          part.get_content_charset()))
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
        h = HTML2Text()
        h.body_width = 0
        h.unicode_snob = True
        payload = h.unescape(h.handle(payload))

    # Convert line endings.
    payload = payload.replace('\r\n', '\n').replace('\r', '\n')

    return payload
