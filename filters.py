#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# jinja2 filters
# 
# @author:     starenka
# @email:      'moc]tod[liamg].T.E[0aknerats'[::-1]
# @version:    1.0
# @since       Nov 25, 2010

import os

def datetimeformat(value, format='%H:%M %d.%m/%y'):
    return value.as_datetime().strftime(format)

def filename(path):
    try:
        path = os.path.split(path)
        return path[-1]
    except:
        return path