print('Введите число')
number=int(input())
numbers=[]
i=null
j=null
for i in range(1, number+1):
    for j in numbers:
	    if i%j==0:
		    break
	else:
	    list.append(i)
print(list)