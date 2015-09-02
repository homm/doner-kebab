# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

EMAIL_CONNECT = {
    'login': 'lenivezbest@yandex.ru',
    'password': 'teslaGENIUS1856alive',
    'server': 'imap.yandex.ru',
    'ssl': True,
}

EMAIL_SEARCH = {
    'mailbox': 'INBOX',
    # 'from': 'paymentcenter@yamoney.ru',
    'from': 'kirill@kirillchernakov.ru',
    'subject': 'Yandex.Dengi payment for',
}

PARSE_RULES = [
    ('id', 'Извещение №'),
    ('date', 'Время платежа:'),
    ('summ', 'Сумма:'),
    ('purpose', 'Содержание заказа:'),
]


GOOGLE_AUTH = {
    "private_key_id": "c2924367491071f6924d70ab9298d6450232945d",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCjpPvLIjtBmMeK\n6JsuB2Y1mO+c/Ftv9x1pOup9VS31e3xhNzWc2kMa1MsyFPHRKzn1mj9895ojpMem\nuowFhC8+vatnEaFSj8SEy7YjR1EOIPu8L9HcFg001deHOeFHhfB/vtkqzH0kOyvN\njcc5Fkxklsh9Q9jU1TnsBSiUgkvXAWDEG3yxr1NwMbR9A9J09gX4AmrEkT09calr\nQRGkH1rXmGd5PtjdIteq6PH/ppYxpiXl1fgXCXxWL1FoRo/eIxU7Z7IwSIQcbcKi\nCsfnrXyKx5NzEC+cJZLSXWVqgdGsoZlkZYjrowLvyvNPf9/oWCWq57/UADz8MBc0\nLEoTL5g3AgMBAAECggEAS/m+OUpUTpk7E3/5A/7Fcl7l6HG1lh8Z1ZBX7AaPBujl\nD1GNn5wqCZwAFulod99k0mVh0og2VRQc6Yi0l58OPEfc+0ZRKr6605isoGZs+G1R\n0sY03cSTLxOVNCAoOoex5+1YcCludFLQfGe1tghnQVBMFvRYCEBS2wRuGb0Arvoj\nehGL6/CXxfN6iTNqaLJXxRiwWxvwCqpH/Xm/vR5iMjidMDOq1t0Rpajy9Sue3tR/\nftM3O4hFC7njj70SUxzrWjksgOS/Q7hbXWL3tFTsIEVfLTdidFyIYSUPn/N6gNJo\n+CrymS5dF2dMOk2MMVPLUh6gtPLlHuMjL2hfrhATUQKBgQDX8Ob4MJPPMmxNSraU\nTAhD88jdWJPPMaZWpumL1Ob+72i8vk7rUbmvCUuMrPMW8EACcC8KImtgCe4VcVn8\nrmnoU67N3IGpgavJm2biih2k2Cs+CEH38PJyoOvJxAcrtUZozQqX04s8LDtKR41d\nK+W08p6N7zTnF7oeDfL4petfvwKBgQDCAIDwL4ZsA5bN+r9M8zOjHBccoY6HeaoZ\n2eQpjBh4CXJZeTHZFAooHKiOL9Ju+K1j8EP+ZdW+o0+I72N98MmnWMeM9+6ZLTUp\nkOf8fex0lYd21uPcJeDTiAQMXe+z3xEinqz+M44ccyQSDX5mLE5Bp6+1GUGc8ENO\nWVtgIU1liQKBgHRNQgiQGTux25SxVa5/WMBIb3mPeGRSSFVJJmXyb8sEZHOrR9QD\nuy8joXYNvAsxsDff9eXObehW0MzptN6bjVzcnTwwtAD4Xu6BbSM74gVji76oMed4\n9Qt50iRkGLyYsGhHbpohDE+HPxOdf+ybdOdE+NJW8DY6mDoRpzf2HNP/AoGAIEQd\nLdV5sfVW26NctdutNu+xGF32aqndlLccr5xRZYWMszzpAYXHuqwpjJx/j11k2T5Y\n0LL3PeHDlK7cCVJG98JYTiXeVTOjp+ol62S2Mx27jhRniXHzVrtEkRn+iBgNrYhe\nlVjVxf2QfkAoSa4MxfaxzpkIxKVhTGKoQ/DGAqECgYAgVfUh5y2qDLBiAjpVQUiz\nAhUPLUq7mDu1C/bA/ZmsY23+cLwOERfZNJtuSszOJRxV+iC3E/I7q0NwZks+fiG5\nH+310MObHyW/lGPtbLOAhaAQX+pj1ktBCn/Gq5V56I9oRYnl103GFiitljRHZlI1\n/tbdNxRljaobBScQSQ8cDQ\u003d\u003d\n-----END PRIVATE KEY-----\n",
    "client_email": "242258052705-i3q6r7ts0b0hk3keeludt7e182h1tq42@developer.gserviceaccount.com",
    "client_id": "242258052705-i3q6r7ts0b0hk3keeludt7e182h1tq42.apps.googleusercontent.com",
    "type": "service_account"
}

GOOGLE_DOC = {
    'id': '1ewAwn_qGkfJOLSoxJ7MBt3kUBFoVQC1rLo1zFtnEpQs',
    'worksheet': 0,
}
