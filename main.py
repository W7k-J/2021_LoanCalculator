# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:21:52 2021

@author: w7k-j
"""
import math
import argparse
import sys

parser = argparse.ArgumentParser(description="This program prints recipes \
consisting of the ingredients you provide.")

parser.add_argument("--type")
parser.add_argument("--payment")    
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if arg.type != 

sys.exit()
#%% 
# def nominal_intrest_rate(percent):
#     return ((percent * 1/100) / 12 * 1)
    
# def months_to_years(months):
#     if months % 12 == 0:
#         return months // 12, 0 
#     else:
#         return int((months - (months % 12)) / 12) , int(months % 12)

    
# while True:
#     print("""What do you want to calculate?"
#     type "n" for number of monthly payments,
#     type "a" for annuity monthly payment amount,
#     type "p" for loan principal:""")
#     decision = input()
#     if decision == "n":
#         loan_principal = float(input("Enter the loan principal"))
#         monthly_payment = float(input("Enter the monthly payment:"))
#         interest_percent = float(input("Enter the loan interest:"))     
        
#         intrest = nominal_intrest_rate(interest_percent)
#         months = math.ceil(math.log(float(monthly_payment) / (float(monthly_payment) - intrest * float(loan_principal)), intrest + 1))

#         y, m = months_to_years(months)
#         if m == 0:
#             if y == 0:
#                 print("wrong data ")
#                 continue
#             if y == 1:
#                 print("It will take 1 year to repay this loan!")             
#             if y > 1:
#                 print(f"It will take {y} years to repay this loan!")
#         else:
#             if y == 0:
#                 print(f"It will {m} months to repay this loan!")
#             else:
#                 print(f"It will take {y} years and {m} months to repay this loan!")
#         break
    
#     if decision == "a":
#         loan_principal = float(input("Enter the loan principal"))
#         months = float(input("Enter the number of periods:"))
#         interest_percent = float(input("Enter the loan interest:"))
        
#         intrest = nominal_intrest_rate(interest_percent)
#         monthly_payment = math.ceil(loan_principal * ((intrest * math.pow(1 + intrest, months)) / (math.pow(1 + intrest, months) - 1)))

#         print(f"Your monthly payment ={monthly_payment}!")
#         break
      
#     elif decision == "p":
#         annuity_payment = float(input("Enter the annuity payment"))
#         months = int(input("Enter the number of periods:"))
#         interest_percent = float(input("Enter the loan interest:"))
        
#         intrest = nominal_intrest_rate(interest_percent)
#         loan_principal = round(annuity_payment / ((intrest * math.pow(1 + intrest, months)) / (math.pow(1 + intrest, months) - 1)))
        
#         print(f"Our loan principal = {loan_principal}!")
#         break
#     else:
#         continue


