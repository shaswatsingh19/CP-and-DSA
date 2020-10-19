'''
Problem Statement :- 

Two-gram is an ordered pair (i.e. string of length two) of capital Latin letters. For example, "AZ", "AA", "ZA" — three distinct two-grams.

You are given a string s consisting of n capital Latin letters. Your task is to find any two-gram contained in the given string as a substring (i.e. two consecutive characters of the string) maximal number of times. For example, for string s = "BBAABBBA" the answer is two-gram "BB", which contained in s three times. In other words, find any most frequent two-gram.

Note that occurrences of the two-gram can overlap with each other.

Input:-
The first line of the input contains integer number n (2≤n≤100) — the length of string s. The second line of the input contains the string s consisting of n capital Latin letters.

Output:-
Print the only line containing exactly two capital Latin letters — any two-gram contained in the given string s as a substring (i.e. two consecutive characters of the string) maximal number of times.

Examples:-

input:-
7
ABACABA
output:-
AB
input:-
5
ZZZAA
output:-
ZZ
Note
In the first example "BA" is also valid answer.

In the second example the only two-gram "ZZ" can be printed because it contained in the string "ZZZAA" two times.

Solution :-
'''
# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')



t = int(input())
s = input()
di = {}
n = len(s)
for i in range(n-1):
	if s[i]+s[i+1] not in di:
		di[s[i]+s[i+1]] = 1
	else:
		di[s[i]+s[i+1]] += 1

mini = 0
for k,v in di.items():
	if v>mini:
		mini = v
		ans = k
print(ans)
