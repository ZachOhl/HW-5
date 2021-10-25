#!/usr/bin/env python
# coding: utf-8

# In[10]:


def punc_remove(string): 
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in string:
        if (x in punctuations):
            string = string.replace(x, "")
    return(string)


# In[13]:


string1 = "what the *!@#^*!!#@$>#.@$'?'@##*)"
punc_remove(string1)

