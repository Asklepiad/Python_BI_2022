#!/usr/bin/env python
# coding: utf-8

# In[10]:


coins = [1,5,10,25,50,100]
def greedychange (money):
    change = []
    while money > 0:
        if money >= max(coins):
            change.append(max(coins))
            money -= max(coins)
        else:
            for i in range(len(coins)):
                if coins[i]==money:
                    change.append(coins[i])
                    money -= coins[i]
                    break
                elif coins[i]>money:
                    change.append(coins[i-1])
                    money -= coins[i-1]
                    break
    return(change)

