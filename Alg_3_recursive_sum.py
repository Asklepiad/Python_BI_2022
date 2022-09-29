#!/usr/bin/env python
# coding: utf-8


def recursive_sum (listt):
    if len(listt) == 1:
        return listt[0]
    else:
        return listt[0] + recursive_sum(listt[1::])

