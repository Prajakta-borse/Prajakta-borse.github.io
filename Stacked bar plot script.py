#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import matplotlib.pyplot as plt
x = Country2015
y1 = Renewable2015
y2 = Renewable2016
plt.bar(x, y1, color='r', label="2015")
plt.bar(x, y2, bottom=y1, color='b',label="2016")
plt.xlabel("Countries")
plt.ylabel("% renewable energy from total energy")
plt.legend(loc='upper right')
plt.title("Percent renewable energy for the year 2015 and 2016 ")
plt.show()

