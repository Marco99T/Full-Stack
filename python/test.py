#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    dic = s.split()
    lis = []
    pal = ""
    primero = True
    for palabra in dic:
        cad = palabra
        for letra in cad:
            le  = letra
            if(letra.isalpha and primero == True):
                le = le.upper()
                primero = False
            pal = pal+le
        lis.append(pal)
        pal = ""
        primero = True
        print(len(palabra))
        
    cadena = " ".join(lis)
    return cadena

s = input()
result = solve(s)
print(result)
