# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

EMAIL_CONNECT = {
    'login': 'homm86@gmail.com',
    'password': 'noivofnzttlgldpg',
    'server': 'imap.gmail.com',
    'ssl': True,
}

EMAIL_SEARCH = {
    'mailbox': 'INBOX',
    # 'from': 'paymentcenter@yamoney.ru',
    'from': 'info@city4people.ru',
    'subject': 'Yandex.Dengi payment for',
}

PARSE_RULES = [
    ('id', 'Извещение № '),
    ('date', 'Время платежа: '),
    ('summ', 'Сумма: '),
    ('purpose', 'Содержание заказа:\n\n'),
]
