# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:21:52 2021

@author: w7k-j
"""
import math


loan_principal = int(input("Enter the loan principal"))

while True:
    print("""What do you want to calculate?"
    type "m" for number of monthly payments,
    type "p" for the monthly payment:)""")
    decision = input()
    if decision == "m":
        m = int(input("Enter the number of months:"))
        if loan_principal % m == 0:
            p = loan_principal / m
            print(f"Your monthly payment = {p}")
            break
        else:
            p = math.ceil(loan_principal / m)
            p_last = loan_principal - (p * (m - 1))
            print(f"Your monthly payment = {p} and the last payment = {p_last}")
            break
    elif decision == "p":
        p = int(input("Enter the monthly payment:"))
        if loan_principal <= p:
            print("It will take 1 month to repay the loan")
            break
        elif loan_principal % p == 0:
            m = int(loan_principal / p)
            print(f"It will take {m} months to repay the loan")
            break
        elif loan_principal % p != 0:
            m = math.floor(loan_principal / p) + 1
            print(m)
            p_last = loan_principal - (p * (m - 1))
            print(p_last)
            print(f"It will take {m} months to repay the loan and the last payment = {p_last}")
            break
    else:
        continue
