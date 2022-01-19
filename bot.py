nums_vozr = []
nums_six = 6

while nums_six > 0:
	nums = int(input('Введите 6 чисел:'))
	nums_vozr.append(nums)
	nums_six -= 1
nums_vozr.sort()	
print(nums_vozr)		


