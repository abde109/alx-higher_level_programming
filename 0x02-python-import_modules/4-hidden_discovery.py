#!/usr/bin/python3.8
import hidden_4

names = [name for name in dir(hidden_4) if name[:2] != '__']
for name in sorted(names):
    print(name)
