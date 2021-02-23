# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:21:52 2021

@author: w7k-j
"""
import math


# loan_principal = int(input("Enter the loan principal"))


def nominal_intrest_rate(percent):
    return ((percent * 1/100) / 12 * 1)
    
def months_to_years(months):
    if months % 12 == 0:
        return months // 12
    else:
        return (months - (months % 12)) / 12 , months % 12

    
while True:
    print("""What do you want to calculate?"
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal:""")
    decision = input()
    if decision == "n":
        loan_principal = int(input("Enter the loan principal"))
        monthly_payment = int(input("Enter the monthly payment:"))
        interest_percent = int(input("Enter the loan interest:"))
        
        intrest = nominal_intrest_rate(interest_percent)
        print(intrest)
        months = (math.log1p(intrest) * (monthly_payment / (monthly_payment - intrest * loan_principal)))
        
        print(months)
        print("--------------")
        # It will take 8 years and 2 months to repay this loan!
        
        
        
        # if loan_principal % m == 0:
        #     p = loan_principal / m
        #     print(f"Your monthly payment = {p}")
        #     break
        # else:
        #     p = math.ceil(loan_principal / m)
        #     p_last = loan_principal - (p * (m - 1))
        #     print(f"Your monthly payment = {p} and the last payment = {p_last}")
        #     break
    elif decision == "p":
        loan_principal = int(input("Enter the loan principal"))
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


