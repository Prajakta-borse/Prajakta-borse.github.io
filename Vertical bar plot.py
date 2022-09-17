#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


fig, ax = plt.subplots(figsize =(16, 9))
ax.barh(Country2015, Renewable2015)
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)
ax.grid(b = True, color ='grey',linestyle ='-.', linewidth = 0.5,alpha = 0.2)
ax.invert_yaxis()
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5,str(round((i.get_width()), 2)),fontsize = 10,color ='grey')
ax.set_title('Countries and their % renewable energy from total energy',loc ='left', )
plt.xlabel("% Renewable Energy from total energy values") 
plt.ylabel("Countries")
plt.show()

