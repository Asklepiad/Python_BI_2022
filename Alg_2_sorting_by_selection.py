#!/usr/bin/env python
# coding: utf-8


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newarr = []
    x = len(arr)
    for i in range(x):
        smallest = find_smallest(arr)
        newarr.append(arr[smallest])
        del arr[smallest]
    return newarr
        

