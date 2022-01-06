def length(x):
	if x=='':
		return 0
	else:
		return 1+length(x[1:])
print(length('hello world'))
