#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
font1 = {'family':'serif','color':'black','size':15}
font2 = {'family':'serif','color':'darkred','size':15}
x,y=HDI2015,GR2015
plt.scatter(x,y)
plt.title("HDI values vs Gender Ratio values for 2015", fontdict = font1)
plt.xlabel("HDI values for the year 2015", fontdict = font2)
plt.ylabel("Gender Ratio values for 2015", fontdict = font2)
plt.legend(['data','correlatSion is 0.229'])
plt.show()

