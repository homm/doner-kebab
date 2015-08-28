# coding: utf-8
from __future__ import absolute_import

import itertools


def grouping(it, n):
    it = iter(it)
    while True:
        chunk = list(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk
