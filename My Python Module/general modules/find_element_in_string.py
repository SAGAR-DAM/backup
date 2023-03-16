# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 09:48:34 2023

@author: sagar
"""
'''
Description:
_____________

This is a code to find some particular elements all indices in a string.
Here the string is: "Sagar Dam is a student in TIFR Mumbai"

which has a in 5 positions. If the index starts from 1 then the positions are: 2,4,8,14,36.

if we pass the string and the required element (i.e. 'a' here) through the function findelement()
the output will be the array of the index or: [2, 4, 8, 14, 36]
'''


def findelement(string,element):
    count=string.count(element)
    #print(count)
    #print (string.find(element))
    
    index_array=[]
    index=0
    
    for i in range(count):
        index=string.find(element,index)
        index_array.append(index+1)
        index=index+1
    return(index_array)

def main():
    string="Sagar Dam is a student in TIFR Mumbai"
    element='a'
    
    index_array=findelement(string,element)
    print(index_array)
    
if __name__=="__main__":
    main()