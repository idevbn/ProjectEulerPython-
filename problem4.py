'''
Largest palindrome product 
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
    
i = 0
number = 1
palindrome = []

while i < 3:
    i += 1
    number = 10 ** i

    
for n1 in range(1, number):
    for n2 in range(1, number):
        n = str(n1 * n2).split()[0]
        if n[:] == n[::-1]:
            palindrome.append(n1 * n2)
print(max(palindrome))
    
