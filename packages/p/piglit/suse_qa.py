# -*- coding: utf-8 -*-

# quick.tests minus tests that are known to fail

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from framework.profile import load_test_profile

__all__ = ['profile']

profile = load_test_profile('quick')

with open("/usr/lib64/piglit/tests/suse_qa-skip-tests.txt") as f:
    to_skip = frozenset(map(lambda line: line[:-1], f))

    profile.filters.append(lambda p, _: p not in to_skip)
