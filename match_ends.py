# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:44:23 2016

@author: 600010000
"""

    
def match_ends(words):
    matching=0

    for word in words:
        len_word=len(word)
        first_letter=word[0]
        last_letter=word[len_word-1]
        if len_word>=2 and first_letter==last_letter:
            matching+=1
    return matching



a=['matteo','mariasolem','mariangela','stefanos','ugu','ba','me']
print match_ends(a)
