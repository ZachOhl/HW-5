#!/usr/bin/env python
# coding: utf-8

# In[18]:


def is_palin(string):
    if string[0:1] != string[len(string)-1:len(string)]:
        return(False)
    elif (len(string) == 1) | (len(string) == 0):
        return(True)
    elif string[0:1] == string[len(string)-1:len(string)]:
        return(is_palin(string[1:len(string)-1]))
    


# In[30]:


print(is_palin("kayak"))
print(is_palin("hello"))
print(is_palin("tattarrattat"))


# In[19]:


#plans:
#check 1st vs last letter, then 2nd vs 2nd to last, etc
#stop conditions: 1. non-symmetry found. 2. middle letter(s) reached

