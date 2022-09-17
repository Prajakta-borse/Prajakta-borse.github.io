#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


from matplotlib import pyplot as plt
import numpy as np
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(HDI2015 )
plt.xlabel("HDI values for the year 2015")
plt.ylabel("Frequency")
plt.title('Histogram')
plt.show()

