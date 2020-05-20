'''
Largest palindrome product 
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

palindrome = []

for n1 in range(1, 1000):
    for n2 in range(1, 1000):
        n = str(n1 * n2).split()[0]
        if n[:] == n[::-1]:
            palindrome.append(n1 * n2)
print(max(palindrome))
    
