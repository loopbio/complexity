#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_conf
------------

Tests for `complexity.conf` module.
"""

import logging
import sys

from complexity import conf

if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest


# Log debug and above to console
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


class TestConf(unittest.TestCase):

    def test_read_conf(self):
        conf_dict = conf.read_conf('tests/conf_proj')
        logging.debug("read_conf returned {0}".format(conf_dict))
        self.assertTrue(conf_dict)
        self.assertEqual(
            conf_dict,
            {
                'output_dir': '../www',
                'templates_dir': 'templates',
                'unexpanded_templates': ['404.html', '500.html']
            }
        )

    def test_get_unexpanded_list(self):
        conf_dict = {
            'output_dir': '../www',
            'templates_dir': 'templates',
            'unexpanded_templates': ['404.html', '500.html']
        }
        self.assertEqual(
            conf.get_unexpanded_list(conf_dict),
            ['404.html', '500.html']
        )

    def test_get_unexpanded_list_empty(self):
        self.assertEqual(conf.get_unexpanded_list({}), ())

if __name__ == '__main__':
    unittest.main()
