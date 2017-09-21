print('Введите первое число')
first=int(input())
print('Введите второе число')
second=int(input())
i=null
list []
if first%5==0:
	i=first
	elif (first+1)%5==0:
	    i=first+1
	    elif (first+2)%5==0:
	        i=first+2
		    elif (first+3)%5==0:
	            i=first+3
			    elif (first+4)%5==0:
	                i=first+4
for i in range(i, second):
	list.append(i)
	i+=5
print(list)