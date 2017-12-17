#d4-high_entropy_passphrases

from itertools import permutations

d4 = open('d4-input.txt').read().split('\n')

def is_repeated(word, p):
    return p.count(word) > 1

def contains_anagram(word, p):
    anagrams = set("".join(anagram) for anagram in permutations(word))
    return is_repeated(word, p) or len(anagrams.intersection(p)) > 1 #counting sets does not catch repeats

def is_valid(p, fn):
    p = p.split()
    for word in p:
        if fn(word, p):
            return False
    return True

def count_valid(passphrases, fn):
    return len(list(filter(lambda p: is_valid(p, fn), passphrases)))

advent_4a = count_valid(d4, is_repeated)
advent_4b = count_valid(d4, contains_anagram)

print (advent_4a, advent_4b)

