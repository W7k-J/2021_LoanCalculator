# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:21:52 2021

@author: w7k-j
"""
import math
import argparse
import sys

#functions

def nominal_intrest_rate(percent):
    return ((percent * 1/100) / 12 * 1)
    
def months_to_years(months):
    if months % 12 == 0:
        return months // 12, 0 
    else:
        return int((months - (months % 12)) / 12) , int(months % 12)
    
def incorrect_message(test,text):
    if test == True:
        print(f"Incorrect parameters - {text}")
    else:
        print("Incorrect parameters")
    sys.exit()
    
def variable_checker(var):
    try:
        variable = float(var)
    except:
        incorrect_message(test, ("convertion problem with" + str.var))
    if variable <= 0:
        incorrect_message(test, (str.var + "variable to small"))
    return variable

#problem checker if true extra message pop out
test = True

#parsing file
parser = argparse.ArgumentParser(description="This program... .")

parser.add_argument("--type")
parser.add_argument("--payment")    
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

arg = parser.parse_args()

#Checking rule 1 - check if type is correct.
if arg.type != "annuity" and arg.type != "diff":
    incorrect_message(test,'Type')
    
    
#Interest is specified without a percent sign. it can accept a floating-point value.
#Our loan calculator can't calculate the interest, so it must always be provided     
    
if type(arg.interest) == type(None):
        incorrect_message(test,"lack of intrest rates")
else:
    try:
        intrest = nominal_intrest_rate(float(arg.interest))
        if intrest <= 0:
            incorrect_message(test,'intrest below zero')
    except:
        incorrect_message(test, 'Intrest convertion')
    
#Differentiate payment - base 
if arg.type == "diff":
    if arg.payment != None:
        incorrect_message(test, 'Payment shouldnt be included')
    if arg.principal == None  or arg.periods == None:
        incorrect_message(test, 'principal and periods must exits with diff')
        
    #Conversion to variables 
    try:       
        loan_principal = float(arg.principal)
        months = int(arg.periods)
    except:
        incorrect_message(test, 'Intrest convertion')
        
    #Variables below zero
    if loan_principal <= 0 or months <= 0:
        incorrect_message(test, 'parameters - below zero')
    
    total = 0
    for k in range(1, months + 1, 1):
        diff_payment = math.ceil((loan_principal / months) + intrest * (loan_principal - ((loan_principal*(k - 1))/ months)))
        total += diff_payment
        print(f"Month {k}: payment is {diff_payment}")
    overpayment = math.ceil(total - loan_principal)
    print(f"Overpayment = {overpayment}")



#Annuity payments - base requirements 

if arg.type == "annuity":

    #check if enough variables, if variables ok and what are we calculating.
    total = 0 
    decision = []
    
    if type(arg.payment) != type(None):
        monthly_payment = variable_checker(arg.payment)
    else:
        decision.append("a")
    if type(arg.principal) != type(None):
        loan_principal = variable_checker(arg.principal)
    else:
        decision.append("p")
    if type(arg.periods) != type(None):
        months = variable_checker(arg.periods)
    else:
        decision.append("n")
        
    if len(decision) != 1:
        incorrect_message(test, 'wrong amount of parameters')

    #type "a" for annuity monthly payment amount
    #type "p" for loan principal:""")
    #type "n" for number of monthly payments

    if decision[0] == "n":
        months = math.ceil(math.log(float(monthly_payment) / (float(monthly_payment) - intrest * float(loan_principal)), intrest + 1))
        y, m = months_to_years(months)
        if m == 0:
            if y == 0:
                incorrect_message(test, "wrong data - 0m and 0y to repay")
            if y == 1:
                print("It will take 1 year to repay this loan!")             
            if y > 1:
                print(f"It will take {y} years to repay this loan!")
        else:
            if y == 0:
                print(f"It will {m} months to repay this loan!")
            else:
                print(f"It will take {y} years and {m} months to repay this loan!")
                
        Overpayment = int(math.ceil(monthly_payment * months) - loan_principal)
        print(f"Overpayment = {Overpayment}")
        
        sys.exit()
    
    elif decision[0] == "a":
        monthly_payment = math.ceil(loan_principal * ((intrest * math.pow(1 + intrest, months)) / (math.pow(1 + intrest, months) - 1)))
        print(f"Your annuity payment = {monthly_payment}!")
        Overpayment = int(math.ceil(monthly_payment * months) - loan_principal)
        print(f"Overpayment = {Overpayment}")       
        
        sys.exit()
      
    elif decision[0] == "p":
        loan_principal = math.ceil(monthly_payment / ((intrest * math.pow(1 + intrest, months)) / (math.pow(1 + intrest, months) - 1)))
        
        print(f"Our loan principal = {loan_principal}!")
        Overpayment = int(math.ceil(monthly_payment * months) - loan_principal)
        print(f"Overpayment = {Overpayment}")
        
        sys.exit()
    
    else:
        incorrect_message(test, 'something seriously wrong')


