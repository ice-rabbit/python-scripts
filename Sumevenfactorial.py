def sum_of_factorial(n):
    if n==0:
        print(1) #base case
    else:
        print(n*sum_of_factorial(n-1)) #recursive case





def sum_even_factorials(n):
    total=0
    total_sum=0
    for i in range(n+1):
        if n%2==0:
            total= sum_of_factorial(i) #factorial of each even number
            total_sum=total_sum+total #total sum of the even factorial
    print(total_sum)

sum_of_factorial(3)
