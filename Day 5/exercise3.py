# Implementing the Gaussian Challenge

# Carl Gauss is often called the "Prince of Mathematicians." When he was only in primary school, his teacher gave the
# class the task of adding all the numbers from 1 to 100. While others were struggling, he came up with the brilliant
# idea to pair the numbers: 1+100, 2+99, and 3+98. Instead of summing every single number individually,
# he realized he could simply multiply 101x50.

total = 0
for num in range(1,101):
    total +=  num

print(total)
print(101*50)   