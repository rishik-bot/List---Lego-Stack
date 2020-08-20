#!/usr/bin/env python
# coding: utf-8

# In[5]:


#list of side lengths
sides=[5 ,4, 2, 1, 4 ,5] #possible
#sides=[5 ,4, 5, 1, 4 ,5] #Impossible, as when the time comes to pick 3rd element, it is found to be bigger than the earlier blocks set in base
tower=[]
while sides:
    if sides[0]>=sides[-1]:
        tower.append(sides[0])
        sides.pop(0)
    else:
        tower.append(sides[-1])
        sides.pop(-1)

x=True
for i in range(len(tower)-1):
    if tower[i]<tower[i+1]:
        x=False
        break
if x==0:
    print("Impossible")
else:
    print("Possible")


# In[ ]:




