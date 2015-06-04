#!/usr/bin/env python3
# This script will try to solve the problem described in:
# https://www.hackerrank.com/challenges/the-love-letter-mystery


def palin_counter(phrase):
    """
    This function will try to check for the number of operations required to
    convert the leters in a palindrome
    """
    num_changes = 0
    phrase_len = len(phrase)
    for i in range(phrase_len//2):
        num_changes += abs(ord(phrase[i])-ord(phrase[phrase_len-1-i]))

    return num_changes

if __name__ == "__main__":
    num_phrases = int(input())
    phrases = list()
    for i in range(num_phrases):
        phrases.append(input())

    for j in range(num_phrases):
        print(palin_counter(phrases[j]))