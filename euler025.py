#1000-digit Fibonacci number
#The Fibonacci sequence is defined by the recurrence relation:
#Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:
#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fib(n):
	if n <= 2:
		return 1;
	else:
		return fib(n-1) + fib(n-2);

index = 1;
result = fib(index);
list = [];
list.append(result);
limit = 1000;


while result / pow(10,limit-1) < 1:
	index += 1;
	if (index <= 2):
		result = 1;
	else:
		#print list, index;
		result = list[index-3] + list[index-2];
	list.append(result);

print index,result;
