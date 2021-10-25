#!/usr/bin/env python
# coding: utf-8

# In[5]:


#In the first section, Python will check if you need to install Pscycopg2 library and install it.
import subprocess
import sys

def install(package):
    #if pip doesn't work, try pip3 in the following statement
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("psycopg2")

import psycopg2

#tweak the database parameters to match your specific postgres database.
#get these values from pgadmin, right click database, click properties, 
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="kickbacksql0", 
                        database="postgres"
                        #You may add the following line if you have schemaa
                        #,options="-c search_path=nfl"
                       )
cur = conn.cursor()
cur.execute(" INSERT INTO employees(SELECT generate_series(1,500) AS id,('{Joe,Bob,Cob}'::text[])[ceil(random()*3)] AS fname,('{Smith,Blith,Zith}'::text[])[ceil(random()*3)] AS lname); ")

conn.commit()
cur.close()
conn.close()


# In[ ]:




