# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 17:04:18 2016

@author: 600010000
"""


a=['matteo','mariasolem','xmariangela','stefanos','xgo','ba','me']


def front_x(word_list):
    x_list=[]
    y_list=[]
    for word in word_list:
        if word[0]=='x': 
            x_list.append(word)
        else:
            y_list.append(word)
    x_list.sort()
    y_list.sort()
    x_list=x_list + y_list
    print x_list
    return x_list
    
    
print front_x(a)


