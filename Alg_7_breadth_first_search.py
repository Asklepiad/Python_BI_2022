#!/usr/bin/env python
# coding: utf-8


from collections import deque
def person_is_seller(name1):
    if name1[-1] == 'm': 
        return True
    else:
        return False
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched=[]
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

