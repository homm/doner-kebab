# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import re
import logging


logger = logging.getLogger(__name__)


def parse_body(body, rules):
    result = []
    for rule in rules:
        name = rule[0]
        prefix = rule[1]
        postfix = None
        if len(rule) > 2:
            postfix = rule[2]
        if postfix:
            regexp = r'^\s*{}\s*([^{}]*)'.format(prefix, postfix)
        else:
            regexp = r'^\s*{}\s*([^\n]*)\n'.format(prefix)

        match = re.search(regexp, body, re.M)

        if match:
            match = match.group(1).strip()

        else:
            logger.info('{} not found.'.format(name))

        result.append((name, match))
    return result
