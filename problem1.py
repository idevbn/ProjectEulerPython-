'''
Multiples of 3 and 5  
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

#multiples of 3 and 5 below 1000

numbers = []

for num in range(0,999):
    num += 1
    if num % 3 == 0 or num % 5 == 0:
        numbers.append(num)

print(numbers) #list of numbers divisible by 3 or 5
print()
print(sum(numbers)) #sum of the list

        

    
    
        
        

