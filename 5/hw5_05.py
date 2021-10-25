#!/usr/bin/env python
# coding: utf-8

# In[21]:


def pyramid(rows):
    stars = [""]*rows
    for x in range(rows):
        stars[x] = " "*(rows - (x+1)) + " *"*(x + 1)
    for i in stars:
        print(i)


# In[24]:


pyramid(15)

