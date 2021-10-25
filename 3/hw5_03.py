#!/usr/bin/env python
# coding: utf-8

# In[1]:


#check if B can be formed by inserting character in A
def is_insert(A, B):
    test = False
    for x in range(len(B)):  #iterate through length of second word with integer iterator
        if (B[:x] + B[x+1:] == A): #check if B with xth letter removed is equal to A
            test = True
            break    
    return test    

A = "Panera"
B = "Pantera"
is_insert(A, B)


# In[2]:


#check if B can be formed by deleting character in A
def is_delete(A, B):
    return is_insert(B, A) 

is_delete("Zach", "Zac")


# In[3]:


#check if B can be formed by replacing character in A
def is_replace(A, B):
    test = False
    for x in range(len(B)):  
        tempB = B[:x] + B[x+1:]   #set B with xth char removed equal to temp variable
        for y in A:
            if (A[:x] + A[x+1:] == tempB):  #check if A with any letter removed is equal to reduced B
                test = True
                break       
    return(test)


# In[4]:


A = "banana"
B = "banona"
is_replace(A, B)


# In[5]:


#One Away function
def is_one_away (A, B):
    if (is_insert(A, B) | is_delete(A, B) | is_replace(A, B)): 
        return(True)
    else:
        return(False)


# In[6]:


print(is_one_away("pale", "ple"))
print(is_one_away("pales", "pale"))
print(is_one_away("pale", "bale"))
print(is_one_away("pale", "bake"))

