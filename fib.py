n=int(input("Enter the limit: "))
a,b=0,1
print("Fibonacci series up to ",n,":")
for i in range(n):
    if a>=n:
        break
    print(a,end=" ")
    a,b=b,a+b
