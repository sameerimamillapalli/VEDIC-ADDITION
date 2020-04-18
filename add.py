n=eval(input("Enter the places till you want to add"))
x=[]
for i in range(n):
    x.append(input("Enter %d digit"%i))
    print(x)
    
print(x[::-1])
sum = []
carry = 0
i=1
for i in range(n,0,-1):
	carry+=int(x[-i])
	sum.append(str(carry%10))
	carry //=10

while carry>0:
	sum.append(str(carry%10))
	carry=carry//10
sum=sum[::-1]
sum="".join(sum)
sum=int(sum)
print(sum)
