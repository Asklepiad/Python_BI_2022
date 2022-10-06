#!/usr/bin/env python
# coding: utf-8


def elements_array (list):
    if list == []:
        return 0
    else:
        return 1 + elements_array (list[1::])

