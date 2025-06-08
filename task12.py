n = int(input("Qancha qiymat kiritmoqchisiz: "))
a = 0
for i in range(1,n+1):
    if i%2==0 :
        a+=i
b = 0
for i in range(1,n+1):
    if i%2!=0 :
        b+=i
print("juft sonlar yig'indisi: ",a)
print("toq sonlar yig'indisi: ",b)