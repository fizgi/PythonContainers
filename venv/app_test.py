""" Test implementation class of the study
    which focuses on Python Containers

    author: Fatih IZGI
    date: 06-Mar-2020
    version: python 3.8.1
"""

import unittest

from typing import List, Tuple
from app import anagrams_lst, anagrams_dd, anagrams_cntr, covers_alphabet, web_analyzer


class ListTest(unittest.TestCase):
    """ Test class of the methods """

    def test_anagrams_lst(self):
        """ testing anagram list """
        self.assertTrue(anagrams_lst("debit card", "bad credit"))
        self.assertTrue(anagrams_lst("listen", "silent"))

    def test_anagrams_dd(self):
        """ testing anagram defaultdict """
        self.assertTrue(anagrams_dd("debit card", "bad credit"))
        self.assertTrue(anagrams_dd("listen", "silent"))

    def test_anagrams_cntr(self):
        """ testing anagram counter """
        self.assertTrue(anagrams_cntr("debit card", "bad credit"))
        self.assertTrue(anagrams_cntr("listen", "silent"))

    def test_covers_alphabet(self):
        """ testing covers alphabet """
        self.assertFalse(covers_alphabet("xyz"))
        self.assertFalse(covers_alphabet("AdefghiJklomnopqrStu"))
        self.assertTrue(covers_alphabet("abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(covers_alphabet("AbCdefghiJklomnopqrStuvwxyz"))
        self.assertTrue(covers_alphabet("aabbcdefghijklmnopqrstuvwxyzzabc"))
        self.assertTrue(covers_alphabet("The quick, brown, fox; jumps over the lazy dog!"))
        self.assertTrue(covers_alphabet("We promptly judged antique ivory"
                                        "buckles for the next prize"))

    def test_web_analyzer(self):
        """ testing web analyzer """
        weblogs: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'), ]

        summary: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']), ]

        self.assertEqual(web_analyzer(weblogs), summary)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
