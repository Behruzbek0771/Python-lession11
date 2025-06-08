N = int(input(" : "))
a = 0
if N>=1:
    for i in range(1,N+1):
        a +=i*i
elif N<=1:
    for i in range(N,1):
        a+=i*i
print(a)