# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 11:18:41 2016

@author: 600010000
"""

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
    
    
def match_ends(words):
    matching=0
  
    for word in words:
        len_word=len(word)
        if len_word>=2:
            first_letter=word[0]
            last_letter=word[-1]
            if len_word>=2 and first_letter==last_letter:
                matching+=1
    return matching
    
    
def sort_last(tuples):
    #create a list of two elements, containing the last value and the tuple
    element_list=[]
    for a_tuple in tuples:
        #creates a temporary element with the sort order and tuple
        #and appends it to the new list
        temp_list=[a_tuple[-1],a_tuple]
        element_list.append(temp_list)
    #sorts the obtained list
    element_list.sort()
        
    #creates a new list of tuples from the ordered one
    result_list=[]
    for a_list in element_list:
        result_list.append(a_list[1])
    
    return result_list
    
def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)
    
def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    
    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

main()

def linear_merge(list1,list2):
    return (list1+list2).sort
    

def remove_adjacent(a_list):
    output_list=[]
    n_elements=len(a_list)
    if n_elements>0:
        n_element=1
        output_list.append(a_list[0])
        previous=a_list[0]
        while n_element<n_elements:
            current=a_list[n_element]
            if previous <> current:
                output_list.append(current)
            previous=current
            n_element+=1
            
    return output_list

#scanning the two list on a linear as requested
#only works with sorted lists as requested
def linear_merge(list1,list2):
    num1=len(list1)
    num2=len(list2)
    
    #initialise the output list
    output=[]
    
    #initialise the counters
    count1=0
    count2=0
    
    #sets the check flag for the loop
    end=0
    
    #loop:
    while end<1:
        if count1<num1 and count2<num2:
            if list1[count1]<list2[count2]:
                output.append(list1[count1])
                count1+=1
            elif list2[count2]<=list1[count1]:
                output.append(list2[count2])
                count2+=1
        elif count1==num1 and count2<num2:
            output.append(list2[count2])
            count2+=1
        elif count2==num2 and count1<num1:
            output.append(list1[count1])
            count1+=1
        elif count1==num1 and count2==num2:
            end=1
        else:
            end=1
            
    return output
        
#more simple
#works with unsorted lists
def linear_merge1(list1,list2):
    output=list1+list2
    output.sort()
    return output
    


def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])

    print
    print 'linear_merge1'
    test(linear_merge1(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge1(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge1(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])

main()

