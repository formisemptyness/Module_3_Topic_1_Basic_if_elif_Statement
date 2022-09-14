'''
Program: basic_if_elif.py
Author: Joshua M. McGinley
Last date modified: 09/13/2022

In the shell or in a text editor, write a program that asks for the user to sign up for Programmer's Toolkit Monthly
Subscription Box. They must select level of membership they want. Each month is something different, t-shirts,
stickers, figurines, even programming books!
The levels are the following:

    Platinum
    Gold
    Silver
    Bronze
    Free Trial

Write an if statement that prints the cost for each of the level. Platinum is $60, each level below is 10 dollars
cheaper, and the free trial is free.
Submit your .py file.
'''



#Print the varied information about the Programmer's Toolkit
print('Hello and welcome to the Programmer\'s Toolkit Monthly Subscription Box.')
print('Each month is something different, t-shirts, stickers, figurines, even programming books!')
print('There are five different levels you can pick from.')
print('The levels are Platinum, Gold, Silver, Bronze, and Free Trial.')

#Take input from user and store in userSubLevel
userSubLevel = input('To subscribe type one of the five levels (e.g. for Gold type \'Gold\' for Free Trial type \'free\'): ')

#Using and if statement determine which level has been picked by compareing userSubLevel to the five different
#levels (Platinum, Gold, Silver, Bronze, Free Trial (free).
if(userSubLevel == 'Platinum'):
    print('Platinum is $60')
elif(userSubLevel == 'Gold'):
        print('Gold is $50')
elif(userSubLevel == 'Silver'):
        print('Silver is $40')
elif(userSubLevel == 'Bronze'):
        print('Bronze is $30')
elif(userSubLevel == 'free'):
        print('The Free Trial is free.')

################################################################################################
###################################Input of test data and Output################################
####Input: Platinum Output: Platinum is $60##Input: Gold Output: Gold is $50####################
####Input: Silver Output: Silver is $40##Input: Bronze Output: Bronze is $30####################
####Input: free Output: The Free Trial is free.##Input: idk Output:    #########################
