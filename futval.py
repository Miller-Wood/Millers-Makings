#futval.py
#a program to compute the value of an investment
#carried 10 years into the future
#by Miller Wood, june 13, 2023

def main():
    print("This program calculates the future value of a ten year investment.");
    principal = eval(input("Enter the initial principal:"));
    apr = eval(input("Enter the annual increase rate:"));
    years = eval(input("PLease enter number of years:"))

    for i in range(years):
        principal = principal * (1+apr);
    print("The value in {} years is: {}".format(years, principal));

main();