# Author: Justin Huang
# GitHub username: huangjus
# Date: 1/25/23
# Description: Prints a list of all integers that divide a number given by the user evenly

integer = int(input('Please enter a positive integer: '))

print('The factors of', integer, 'are:')

for factor in range(1, integer+1):
    if integer % factor == 0:
        print(factor)
