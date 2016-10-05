# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 16:34:14 2016

@author: 600010000
"""

def donuts(count):
    if count<10:
        output='Number of donuts: '+str(count)
    else:
        output='Number of donuts: many'
    return output
    
def both_ends(s):
    if len(s)<2:
        output=""
    else:
        output=s[:2]+s[-2:]
    return output
        
    
def fix_start(s):
    start=s[0]
    s=s.replace(start,"*")
    output=start+s[1:]
    return output
    
def mix_up(a,b):
    first_a=a[:2]
    last_a=a[2:]
    first_b=b[:2]
    last_b=b[2:]
    output=first_b+last_a+" "+first_a+last_b
    return output
    


def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')
    
main()


def verbing(s):
    length=len(s)
    if length<3:
        output=s
    elif s.endswith("ing"):
        output=s+"ly"
    else:
        output=s+"ing"
    return output
    
    
def not_bad(s):
    _not=s.find('not')
    _bad=s.find('bad')
    if _not>=0 and _bad>=0 and _bad>_not:
        start=s[:_not]
        _bad+=3
        end=s[_bad:]
        output=start+'good'+end
    else:
        output=s
    return output
    
    
def front_back(a,b):
    len_a=len(a)
    if len_a%2==0:
        half_a=len_a/2
    else:
        half_a=(len_a//2)+1
    front_a=a[:half_a]
    back_a=a[half_a:]
    
    len_b=len(b)
    if len_b%2==0:
        half_b=len_b/2
    else:
        half_b=(len_b//2)+1
    front_b=b[:half_b]
    back_b=b[half_b:]
    
    output=front_a+front_b+back_a+back_b
    return output

def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')
    
main()
    