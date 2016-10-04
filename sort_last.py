# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 17:32:36 2016

@author: 600010000
"""



def sort_last(tuples):
    #create a list of two elements, containing the last value and the tuple
    element_list=[]
    for a_tuple in tuples:
        #creates a temporary element with the sort order and tuple
        #and appends it to the new list
        temp_list=[a_tuple[len(a_tuple)-1],a_tuple]
        element_list.append(temp_list)
    #sorts the obtained list
    element_list.sort()
        
    #creates a new list of tuples from the ordered one
    result_list=[]
    for a_list in element_list:
        result_list.append(a_list[1])
    
    return result_list
    
a=[(1,7),(1,3),(3,4,5),(2,2)]
print a
print sort_last(a)

