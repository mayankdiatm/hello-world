def collatz(number):
    if(number%2==0):
        print(number//2)
    else:
        print(3*n+1)

print("Enter number of your choice:")
n = input()
collatz(n)

