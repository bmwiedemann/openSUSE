#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from formats import FormatBank


class TestFormats(unittest.TestCase):

    def test_discovery(self):
        formats = FormatBank()
        formats.discover()

    def test_registering(self):
        formats = FormatBank()
        formats.discover_json()
        def composer(text):
            return '1:%s' % text
        def parser(text):
            return text[2:]
        formats.register('test', parser, composer)
        assert formats.parse('test', '1:hello') == 'hello'
        assert formats.compose('test', 'hello') == '1:hello'
        assert formats.convert('test', 'json', '1:hello') == '"hello"'
        assert formats.convert('test', 'test', '1:hello') == '1:hello'


if __name__ == '__main__':
    unittest.main()
