# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

EMAIL_CONNECT = {
    'login': 'your.mail@yandex.ru',
    'password': 'not a real password',
    'server': 'imap.yandex.ru',
    'ssl': True,
}

EMAIL_SEARCH = {
    'mailbox': 'INBOX',
    # 'from': 'paymentcenter@yamoney.ru',
    'from': 'info@city4people.ru',
    'subject': 'Yandex.Dengi payment for',
}

PARSE_RULES = [
    ('id', 'Извещение №'),
    ('date', 'Время платежа:'),
    ('summ', 'Сумма:'),
    ('purpose', 'Содержание заказа:'),
]


GOOGLE_AUTH = {
    "private_key_id": "1507b7afc047816d9beee41abbb9e3d9e6b041c8",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9B5ufE8oZW1DV\nwOWloCodzddfjNEqPHoJ4UG/bh3nNFVOdQJDFmt0u6Y7JKyUnc4p2RY7FOpuElFj\nU9mFIzZdgeJLvNdIqT69r7Ccr5CKM8bd6KYBGRW2u1uoJg9wa7fznN9YkVtobQmc\nQeGhnN+SgO/GtuPmLEfHQ/DRy5KX85oXoGu2wPLUrmQ9EcWDjLC7ztCwryijemqD\n6PyryJiXmijaD2xk2fRh8m+BqxT/icSh0eG+xvSv/ksaFfw1Fj1Z8o/fhCx8pgxi\nCA2FrnE+VDJ5a0B3hlYj6nkT1GmjRCV4YiX4jn8PjZpzhjNmr0YoRomO0CzAQLBC\nISFqLaF3AgMBAAECggEBAKvZCsVn/EdpGOf64cvc++z0gWRAZLd9G4V334nk1hKn\nJRaakV/kNfR90/XYtXy2qgKpdOhpb2Z6CLvAMvQyuu3vcodgOme4VW2lF26avVCn\nGZgMNT6yS2dAlWccktSlWSqD5xhhrTQWTLJdwn5mW2qZBWMmSbGrd+XUAk74P2Eb\nZn2vmSt0n/+lN+Uqy7jSASj7O1AjTOhQqVBQbd9hIfjYeK8Z/mB0eEXyQ/MBGp+4\nbPDTqMMt72U15qIDkgvM1k3IetREKJsaU1VPqXTYZ5AQ8v1BibWoXQGdqackWAY6\nL3xa6R5RToCey8KHrFSKV5qajkLO/VVjAWK4Z8q5DOECgYEA+HNMJ3lgPwfvy5K1\nMu29FxskFEAbmv7XfjQVYHMEGuW2WUTvA0J+E6McIlrHEjl3hEH5n81I5DtYs3vY\nJcxXewhmfQVNfrM2s5+ryVMMQSyNK3mJavFa8EkBcQZ3f3iisfQTYfi4y9E8uCsW\nlHpUOrGRRFdysg+Q6PuHGoEt/XUCgYEAwsYTTgGKy6vcUInmqoc/A8daZyS8eJLS\n7766BtDx/w2AzqxnSI3rgZ9SjhiWKf2odnk+mWVJZG9Um5+BAQS0Xnw+rZViVHyL\nhdwB+Kiqayf/fZjuDvdn1UCps1nwhSFkSukHviIhKibeCfZEfIOW7G/o8qlPNqU0\nS5dFBs+O6bsCgYBJSZl5O3CMp0axAkG5GC/jFPp7jr2V5v6iF7MGlGbtmD1F7/Oh\nPof6Ou8dozF9yr3aoauE3AVYbbkomKuV2sUjYcL5tgq6CRtluP/vjzPaNc4euOc0\nSKXOo3ptYL73Nxqm65ycFcZNORd0LCGpAry944s6YaFPrQ/N6gRcaSar0QKBgDN+\nyPXTxI1qp7oHa5vkXA20tDsW5FmAgBJwu6A3t/N173s0662sD/raU6pL58+8R8Di\n92D4/Xl3Ucg/WI0bYFCmyq98El5B+2VtsHu8pCnmjk73kuEUGjiweu13NvcLyAdi\nKvDi9x+83PGHUb4V0F48jDsz9kR9UyE1IkPVtnQnAoGAT0Zq2iWvTCA10ZmZxjhS\nrmtiOsKSxh99qwNwSqmKGgail7r69s3bTCaQexOeigQTvYLBaZf9EjvTqoaZA+TI\nlWxSzY5qDugcH8xXjzlLD1KAewZvo79A7cOFX48Bw//0nRZF6CHgUNWLgT1dtH1I\nXn3BvHh3uO2iVrTOYfnlv+Y\u003d\n-----END PRIVATE KEY-----\n",
    "client_email": "869161537625-9td4miap838n6of58o0vq82am5iihe8k@developer.gserviceaccount.com",
    "client_id": "869161537625-9td4miap838n6of58o0vq82am5iihe8k.apps.googleusercontent.com",
    "type": "service_account"
}

GOOGLE_DOC = {
    'id': '1Ht2e2tmiHWOv6UsQ1T0UMoWd2T_zs5XMlQ_oTakOrrQ',
}
