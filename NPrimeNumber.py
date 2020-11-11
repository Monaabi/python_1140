#N Prime Number
num = int(input("Enter the number-"))
N = 2
while num!=0:
    for i in range(2,N):
        if N%i==0:
            break
    else:
        print(N,end=" ")
        num -= 1
    N += 1

