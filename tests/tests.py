#!/usr/bin/env python
from __future__ import print_function
from random import *
import unittest

class SomeTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(1, 1)

    def test_2(self):
        self.assertEqual(1, 1)

    def test_3_randomly_fails(self):
        self.assertNotEqual(1, randint(1, 3))

    def test_4(self):
        self.assertEqual(1, 1)
