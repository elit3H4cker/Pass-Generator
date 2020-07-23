#You have Python3 install to use this script 
#Executing command 
#$python3 pass_generator.py
string = input("Enter The Words You Want separated by commos :> ")
a = string.split(",")
n = int(input("Enter number of Words you input above"))
x = n+1
import itertools
for e in range(x):
    for i in itertools.permutations(a,e):
        print(''.join(i))
