#Extenral Library Colorama imported and intialised
from colorama import init, Fore, Back, Style

init ()

"""
Colorama Testing
"""
print(Fore.CYAN + "Welcome to")
print(Back.LIGHTBLUE_EX + "RepayRite:")
print(Style.DIM + "Mortgage Repayment")
print(Style.RESET_ALL + "Calculator!")

"""
Initial user input that will provide figures for the mortgage repayment formula to be used
"""

loan_amount = float(input("Please enter your full loan amount:"))
print(loan_amount)

annual_interest_rate = float(input("Please enter your annual interest rate:"))
print(annual_interest_rate)

loan_term = int(input("Please enter your loan term in years:"))
print(loan_term)