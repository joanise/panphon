#!//usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division

import unittest
import sonority


class TestSonority(unittest.TestCase):

    def setUp(self):
        self.son = sonority.Sonority()

    def test_sonority_nine(self):
        segs = ['a', 'ɑ', 'æ', 'ɒ', 'e', 'o']
        scores = [9] * 6
        self.assertEqual(map(self.son.sonority, segs), scores)

    def test_sonority_eight(self):
        segs = ['i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u']
        scores = [8] * 6
        self.assertEqual(map(self.son.sonority, segs), scores)

    def test_sonority_seven(self):
        segs = ['j', 'w', 'ʋ', 'ɰ', 'ɹ']
        scores = [7] * 5
        self.assertEqual(map(self.son.sonority, segs), scores)

    def test_sonority_six(self):
        segs = ['l', 'ɭ', 'r', 'ɾ']
        scores = [6] * 4
        self.assertEqual(map(self.son.sonority, segs), scores)

    def test_sonority_five(self):
        segs = ['n', 'm', 'ɲ', 'ɴ']
        scores = [5] * 4
        self.assertEqual(map(self.son.sonority, segs), scores)

    def test_sonority_four(self):
        segs = ['v', 'z', 'ʒ', 'ɣ']
        scores = [4] * 4
        self.assertEqual(map(self.son.sonority, segs), scores)

    def test_sonority_three(self):
        segs = ['f', 's', 'x', 'θ', 'ʃ']
        scores = [3] * 5
        self.assertEqual(map(self.son.sonority, segs), scores)

    def test_sonority_two(self):
        segs = ['b', 'ɡ', 'd', 'ɢ']
        scores = [2] * 4
        self.assertEqual(map(self.son.sonority, segs), scores)

    def test_sonority_one(self):
        segs = ['p', 'k', 'c', 'q']
        scores = [1] * 4
        self.assertEqual(map(self.son.sonority, segs), scores)