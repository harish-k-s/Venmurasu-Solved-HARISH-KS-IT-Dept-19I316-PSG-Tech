from sys import exit
try:
    Display = int(input("\nHow Many (Longest) Words To Show? "))
except(ValueError):
    print("\nKindly Try Again With A Valid Natural Number\n")
    exit(1)
with open('Venmurasu Final Text Solution.txt', 'r', encoding='utf-8') as Solution:
    print('\nRank\tLength\tWord\n')
    for Rank in range(1,Display+1):
        print(str(Rank)+'\t'+Solution.readline())