#!/usr/bin/env python
# coding: utf-8

# In[115]:


import sys


# In[59]:


# sequential_map
def sequential_map(*args):
    container = args[-1]
    for i in args[:len(args)-1]:
        container = list(map(i, container))
    return(container)


# In[61]:


# consensus_filter
def consensus_filter(*args):
    container = args[-1]
    for i in args[:len(args)-1]:
        container = list(filter(i, container))
    return(container)


# In[64]:


# conditional_reduce
def reduce(func, cont):
    x = cont[0]
    for i in cont[1::]:
        x = func(x, i)
    return(x)
def conditional_reduce(func1, func2, container):
    return reduce(func2, list(filter(func1, container)))


# In[67]:


# func_chain
def func_chain(*args):
    def function(x):
        if type(x) == int or type(x) == float:
            x = [x]
        for i in args[:-1:]:
            x = map(i, x)
        x = list(map(args[-1], x))
        return x
    return function


# In[91]:


# integration to first
def sequential_map2(*args):
    container = args[-1]
    args = args[0:-1:1]
    new_function = func_chain(*args)
    return new_function(container)


# In[ ]:


# multiple_partial
def partial2(func, /, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = {**keywords, **fkeywords}
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
def multiple_partial(*funcs, **kwargs):
    return(list(map(lambda x: partial2(x, **kwargs), funcs)))


# In[108]:


#print
def print(*args, sep=" ", end="\n"):
    for argument in args[:-1:]:
        sys.stdout.write(str(argument))
        sys.stdout.write(sep)
    sys.stdout.write(str(args[-1]))
    sys.stdout.write(end)

