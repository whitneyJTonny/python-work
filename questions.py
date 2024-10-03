#The volume of a sphere with radius r is (4/3)* pie * r**2. 
# What is the volume of the sphere with radius 5. 
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places
import math

# Given radius
radius = 5
# Volume of the sphere formula: (4/3) * pi * r^3
volume = (4/3) * math.pi * radius**3
print(volume)

# Create a program to calculate the area of a triangle (1/2 * base * height). 
# Base and height should be entered using the keyboard. 
base = int(input("Enter the base of the triangle"))
height = int(input("Enter the height of the triangle"))
area = 1/2 * base * height
print(area)
#Question One
# WITI has tasked you to automate a simple grading system. 
# As a python student, write a program using  to display the grades that 
# the students will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89%   Grade is  B
# 70% - 79%   Grade is C                                                        
# 60% - 69%   Grade is D                  
# 50% - 59%   Grade is E  
# < 50% Fail 

def grading_system():
    mark = int(input("Enter the mark scored: "))
    if 90 <= mark <= 100:
        grade = "A"
    elif 80 <= mark < 90:
        grade = "B"
    elif 70 <= mark < 80:
        grade = "C"
    elif 60 <= mark < 70:
        grade = "D"
    elif 50 <= mark < 60:
        grade = "E"
    else:
        grade = "Fail"
    print(f"The grade is {grade}")
#  WITI Academy is proposing a Sacco to help students save their money. 
#  Design a platform that will do the following.
#  Welcome to, WITIAcademy Sacco.
#  1. Deposit Money
#  2. Withdraw Money
#  3. Check Balance
#  Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#  If the student selects 3, the account balance should be displayed.

def witi_academy_sacco():
    balance = 0

    while True:
        print("\nWelcome to WITIAcademy Sacco.")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            deposit = int(input("Enter amount to deposit (minimum 1000): "))
            if deposit >= 1000:
                balance += deposit
                print(f"Deposited {deposit}. New balance is {balance}.")
            else:
                print("Minimum deposit is 1000.")
        
        elif choice == '2':
            withdraw = int(input("Enter amount to withdraw (minimum 500): "))
            if withdraw >= 500:
                if withdraw <= balance:
                    balance -= withdraw
                    print(f"Withdrew {withdraw}. New balance is {balance}.")
                else:
                    print("Insufficient balance.")
            else:
                print("Minimum withdrawal is 500.")
        
        elif choice == '3':
            print(f"Current balance is {balance}.")
        
        elif choice == '4':
            print("Exiting. Thank you for using WITIAcademy Sacco.")
            break
        
        else:
            print("Invalid option, please try again.")

witi_academy_sacco()