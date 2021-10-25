#!/usr/bin/env python
# coding: utf-8

# In[51]:


def print_tri(rows):
    beg = 1
    end = 2
    count1 = 1
    while count1 <= rows:
        nums = ""
        count2 = 1
        for x in range(beg, end, 1):
            nums += " " + str(x) 
            count2 += 1
        print(nums)
        count1 += 1
        beg = end
        end  = end + count2
        


# In[52]:


print_tri(3)


# In[53]:


print_tri(6)


# In[ ]:




