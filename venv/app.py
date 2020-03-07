"""A study focuses on Python Containers

    author: Fatih IZGI
    date: 06-Mar-2020
    version: python 3.8.1
"""

from typing import DefaultDict, List, Tuple
from collections import defaultdict, Counter


def anagrams_lst(str1: str, str2: str) -> bool:
    """ returns True if str1 and str2 are anagrams, False if not """
    return sorted(list(str1)) == sorted(list(str2))


def anagrams_dd(str1: str, str2: str) -> bool:
    """ returns True if str1 and str2 are anagrams, False if not """
    ddict: DefaultDict[str, int] = defaultdict(int)

    for char in str1:
        ddict[char] += 1

    for char in str2:
        if char in ddict:
            ddict[char] -= 1
        else:
            return False

    return not any(ddict.values()) # if any of the value is not 0, return False, else return True.


def anagrams_cntr(str1: str, str2: str) -> bool:
    """ returns True if str1 and str2 are anagrams, False if not """
    return Counter(str1) == Counter(str2)


def covers_alphabet(sentence: str) -> bool:
    """ returns True if sentence includes at least
        one instance of every character in the alphabet or False"""
    # greater than or equal to include , ; ! etc.
    return set(sentence.lower()) >= set("abcdefghijklmnopqrstuvwxyz")


def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    """ returns a summary of the weblogs with each distinct site
        and a sorted list of names of distinct people who visited that site """
    ddict: DefaultDict[str, List[str]] = defaultdict(List[str])

    for key in sorted([(log[1], log[0]) for log in set(weblogs)]):
        ddict[key[0]] = sorted([log[0] for log in set(weblogs) if log[1] == key[0]])

    return list(ddict.items())
