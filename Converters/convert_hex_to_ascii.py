#!/usr/bin/python
# -*- coding: utf-8 -*-

x = '454b4f7b4c614269674265663072647d02578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578202578'

print("".join([chr(int(c,16)) for c in [x[i]+x[i+1] for i in range(0,len(x)-1,2)]]))