#!/usr/bin/env python
# coding: utf-8

# Function for searching node with lowest cost

def flcn(costs):
    lowest_cost = float("inf")
    lcn = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lcn = node
    return lcn


# Deikstra algorithm

node = flcn(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n]>new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = flcn(costs)
    

