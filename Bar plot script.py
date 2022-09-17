#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


#Bar plot
fig = plt.figure(figsize = (15, 5))
plt.bar(Country2015, Renewable2015, color ='maroon',
        width = 0.1)
 
plt.xlabel("Countries")
plt.ylabel("% renewable energy from total energy")
plt.title("Percent renewable energy for different countries")

plt.show()

