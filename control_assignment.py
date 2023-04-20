# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50.
def even_numbers():
    x=0
    while x<=50:
        x+=1
        if x%2!=0:
            continue
        print(x)
# Write a function that takes an integer argument and prints "Prime" if the number is prime, 
# and "Not prime" if the number is not prime.
def prime_numbers(a):
    if a<=1:
        print("not prime")
    elif a>1:
        for i in range(2,a):
            if a%i==0:
                print("not prime")
                break
        else:
            print("prime")   

# Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list             
def sum_even(nums):
    sum = 0
    for i in nums:
        if i % 2 == 0:
            sum += i
    print(sum)
# sum_even(([1,2,3,4,5,6,7,8,9,10]))
# Write a function that takes any two integers as input,
#  and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3
def even_sums(input1,input2):
    x = 0
    for i in range(input1,input2+1):
        if i % 3 ==0:
            x +=i
print(x)